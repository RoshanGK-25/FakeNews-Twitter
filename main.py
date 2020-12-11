from flask import Flask, render_template, request, redirect, session, flash, jsonify
from mysqlconnection import MySQLConnector
# from __future__ import print_function
import re
import os
import json
import MySQLdb
import MySQLdb.cursors as cursors

import tweepy
from tweepy import OAuthHandler

db = MySQLdb.connect("localhost", "root", "root", "twitter_data")
cursor = db.cursor()

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'[0-9]')
PASS_REGEX = re.compile(r'.*[A-Z].*[0-9]')

app = Flask(__name__)
app.secret_key = 'twitter'
mysql = MySQLConnector(app, 'twitter_data')
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import twitter_samples, stopwords
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from nltk import FreqDist, classify, NaiveBayesClassifier
import pickle
import re, string, random


def remove_noise(tweet_tokens, stop_words=()):
    cleaned_tokens = []

    for token, tag in pos_tag(tweet_tokens):
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|' \
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', token)
        token = re.sub("(@[A-Za-z0-9_]+)", "", token)

        if tag.startswith("NN"):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'

        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)

        if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words:
            cleaned_tokens.append(token.lower())
    return cleaned_tokens


def get_all_words(cleaned_tokens_list):
    for tokens in cleaned_tokens_list:
        for token in tokens:
            yield token


def get_tweets_for_model(cleaned_tokens_list):
    for tweet_tokens in cleaned_tokens_list:
        yield dict([token, True] for token in tweet_tokens)


def get_pattern(tweet):
    prob = 0
    h = 0
    a = 0
    q = 0
    d = 0
    u = 0
    rt = 0
    emergency = 0
    raw_tweet = tweet
    raw_token = word_tokenize(raw_tweet)
    print(raw_token)
    for tokens in raw_token:
        if '#' in tokens:
            h += 1
            if h > 1:
                prob += 1
        if '@' in tokens:
            a += 1
            if a > 1:
                prob += 1
        if '?' in tokens:
            q += 1
            if q > 1:
                prob += 1
        if '$' in tokens:
            d += 1
            if d > 1:
                prob += 1
        if 'http' in tokens:
            u += 1
            if u > 1:
                prob += 1
        if 'RT' in tokens:
            rt += 1
            if rt > 1:
                prob += 1
        if 'https' in tokens:
            u += 1
            if u > 1:
                prob += 1
        if 'help' in tokens:
            emergency += 1

        if 'emergency' in tokens:
            emergency += 1

        if 'disaster' in tokens:
            emergency += 1

    if prob > 2:
        rmr = 1

    else:
        rmr = 0

    return rmr, emergency


@app.route('/')
def index():
    #print(session)
    return render_template('index.html')


@app.route('/Logout')
def logout():
    #print(session)
    return render_template('index.html')


@app.route('/about')
def about():
    #print(session)
    return render_template('about.html')


@app.route('/ulogin')
def ulogin():
    #print(session)
    return render_template('ulogin.html')


@app.route('/search_tweet')
def search_tweets():
    #print(session)
    return render_template('search.html')


@app.route('/contact')
def contact():
   # print(session)
    return render_template('contact.html')


@app.route('/alogin')
def alogin():
    #print(session)
    return render_template('alogin.html')


@app.route('/reg')
def reg():
    #print(session)
    return render_template('register.html')


@app.route('/regu', methods=['POST'])
def register_user():
    #print("in register")
    input_email = request.form['eid']
    email_query = "SELECT * FROM user WHERE email = :email_id"
    query_data = {'email_id': input_email}
    stored_email = mysql.query_db(email_query, query_data)

    #print(request.form)
    #print(request.form['eid'])
    #print(session)

    for x in request.form:
        if len(request.form[x]) < 1:
            #print(x + " cannot be blank!", 'blank')
            pass

    if NAME_REGEX.search(request.form['fname']):
        #print("First name cannot contain any numbers", 'error')
        pass

    if NAME_REGEX.search(request.form['lname']):
        #print("Last name cannot contain any numbers", 'error')
        pass
    if len(request.form['pwd']) < 5:
        #print("Password must be more than 5 characters", 'password')
        pass
    if not EMAIL_REGEX.match(request.form['eid']):
        #print("Email must be a valid email", 'error')
        #print("Email must be a valid email")
        pass

    if stored_email:
        #print("Email already exists!")
        pass

    if '_flashes' in session:
        #print("error")
        pass

        return redirect('/')
    else:
        #print("All Good!!!!", 'good')
        query = "INSERT INTO user (fname, lname, email, mob, username, password) VALUES (:first_name, :last_name, :email_id, :mob, :uname, :pass )"

        data = {
            'first_name': request.form['fname'],
            'last_name': request.form['lname'],
            'email_id': request.form['eid'],
            'mob': request.form['mno'],
            'uname': request.form['uname'],
            'pass': request.form['pwd']
        }

        mysql.query_db(query, data)

        input_email = request.form['eid']
        email_query = "SELECT * FROM user WHERE email = :email_id"
        query_data = {'email_id': input_email}
        stored_email = mysql.query_db(email_query, query_data)

        #print("This email address you entered " + input_email + " is a valid email address. Thank you!")
        return render_template('ulogin.html')


@app.route('/loginu', methods=['POST'])
def login():
    input_uname = request.form['uname']
    input_password = request.form['pass']
    email_query = "SELECT * FROM user WHERE username = :uname "
    query_data = {'uname': str(input_uname)}
    stored_email = mysql.query_db(email_query, query_data)

    if not stored_email:
        #print("User does not exist!")
        return redirect('/')

    else:
        if request.form['pass'] == stored_email[0]['password']:
         #   print("login success")
            tweets = get_tweets("")
            return render_template('uhome.html', data=tweets)

        else:
          #  print("Wrong password, try again!")
            return redirect('/')


@app.route('/logina', methods=['POST'])
def logina():
    input_uname = request.form['uname']
    input_password = request.form['pass']
    email_query = "SELECT * FROM admin WHERE username = :uname "
    query_data = {'uname': str(input_uname)}
    stored_email = mysql.query_db(email_query, query_data)

    if not stored_email:
        #print("User does not exist!")
        return redirect('/')

    else:
        if request.form['pass'] == stored_email[0]['password']:
         #   print("login success")
            tweets = get_tweets("")
            return render_template('ahome.html', data=tweets)

        else:
          #  print("Wrong password, try again!")
            return redirect('/')


@app.route('/search_user', methods=['POST'])
def search_user():
    input_uname = request.form['keywrd']
    tweets = get_tweets(str(input_uname))
    sql = "SELECT * FROM tweetdata"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
    except Exception as e:
        #print(e)
        pass

    session['keywrd'] = input_uname
    return render_template('search1.html', data=results)


@app.route('/search_user', methods=['POST'])
def search_user1():
    input_uname = request.form['keywrd']
    tweets=get_tweets(str(input_uname))
    sql = "SELECT * FROM tweetdata"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
    except Exception as e:
        #print(e)
        pass

    session['keywrd']=input_uname
    return render_template('search1.html', data=results)


@app.route('/ufake')
def ufake():
    rmr_cnt = 0
    neg_cnt = 0
    pos_cnt = 0
    total_cnt = 0
    pickle_in = open("sentiment_model.pickle", "rb")

    classifier = pickle.load(pickle_in)
    sql = "SELECT * FROM tweetdata"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
    except Exception as e:
        #print(e)
        pass
    for row in results:
        custom_tweet = row[1]
        custom_tokens = remove_noise(word_tokenize(custom_tweet))
        #print(custom_tweet, classifier.classify(dict([token, True] for token in custom_tokens)))
        senti = classifier.classify(dict([token, True] for token in custom_tokens))
        #print(senti)
        if senti == "Negative":
            neg_cnt += 1
            sql = "INSERT INTO negtweet(tweet,keywrd) VALUES ('%s', '%s')" % (row[1], row[2])
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
        if senti == "Positive":
            pos_cnt += 1
            sql = "INSERT INTO postweet(tweet,keywrd) VALUES ('%s', '%s')" % (row[1], row[2])
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()

        patt, emergency = get_pattern(row[1])

        if patt == 1:
            sql = "INSERT INTO rmrtweet(tweet,keywrd,userid) VALUES ('%s', '%s', '%s')" % (row[1], row[2], row[0])
            rmr_cnt += 1
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
        if emergency >= 1:
            sql = "INSERT INTO emergency(tweet,userid) VALUES ('%s', '%s')" % (row[1], row[0])
            rmr_cnt += 1
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()

    total_cnt = neg_cnt + pos_cnt
    session['neg_cnt'] = neg_cnt
    session['pos_cnt'] = pos_cnt
    session['rmr_cnt'] = rmr_cnt
    session['total_cnt'] = total_cnt
    pos_polarity = float(pos_cnt) / total_cnt * 100
    neg_polarity = float(neg_cnt) / total_cnt * 100
    session['pos_polarity'] = pos_polarity
    session['neg_polarity'] = neg_polarity
    sql = "SELECT * FROM postweet"
    try:
        cursor.execute(sql)
        results1 = cursor.fetchall()
    except Exception as e:
        pass
        #print(e)

    sql = "SELECT * FROM negtweet"
    try:
        cursor.execute(sql)
        results2 = cursor.fetchall()
    except Exception as e:
        #print(e)
        pass

    sql = "SELECT * FROM rmrtweet"
    try:
        cursor.execute(sql)
        results3 = cursor.fetchall()
    except Exception as e:
        #print(e)
        pass

    sql = "SELECT * FROM emergency"
    try:
        cursor.execute(sql)
        results4 = cursor.fetchall()
    except Exception as e:
        #print(e)
        pass

    return render_template('view_behv.html', data1=results1, data2=results2, data3=results3, data4=results4)


@app.route('/afake')
def afake():
    rmr_cnt = 0
    neg_cnt = 0
    pos_cnt = 0
    total_cnt = 0
    pickle_in = open("sentiment_model.pickle", "rb")

    classifier = pickle.load(pickle_in)
    sql = "SELECT * FROM tweetdata"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
    except Exception as e:
        #print(e)
        pass
    for row in results:
        custom_tweet = row[1]
        custom_tokens = remove_noise(word_tokenize(custom_tweet))
        #print(custom_tweet, classifier.classify(dict([token, True] for token in custom_tokens)))
        senti = classifier.classify(dict([token, True] for token in custom_tokens))
        #print(senti)
        if senti == "Negative":
            neg_cnt += 1
            sql = "INSERT INTO negtweet(tweet,keywrd) VALUES ('%s', '%s')" % (row[1], row[2])
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
        if senti == "Positive":
            pos_cnt += 1
            sql = "INSERT INTO postweet(tweet,keywrd) VALUES ('%s', '%s')" % (row[1], row[2])
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()

        patt, emergency = get_pattern(row[1])

        if patt == 1:
            sql = "INSERT INTO rmrtweet(tweet,keywrd,userid) VALUES ('%s', '%s', '%s')" % (row[1], row[2], row[0])
            rmr_cnt += 1
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
        if emergency >= 1:
            sql = "INSERT INTO emergency(tweet,userid) VALUES ('%s', '%s')" % (row[1], row[0])
            rmr_cnt += 1
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()

    total_cnt = neg_cnt + pos_cnt
    session['neg_cnt'] = neg_cnt
    session['pos_cnt'] = pos_cnt
    session['rmr_cnt'] = rmr_cnt
    session['total_cnt'] = total_cnt
    pos_polarity = float(pos_cnt) / total_cnt * 100
    neg_polarity = float(neg_cnt) / total_cnt * 100
    session['pos_polarity'] = pos_polarity
    session['neg_polarity'] = neg_polarity
    sql = "SELECT * FROM postweet"
    try:
        cursor.execute(sql)
        results1 = cursor.fetchall()
    except Exception as e:
        pass
        #print(e)

    sql = "SELECT * FROM negtweet"
    try:
        cursor.execute(sql)
        results2 = cursor.fetchall()
    except Exception as e:
        #print(e)
        pass

    sql = "SELECT * FROM rmrtweet"
    try:
        cursor.execute(sql)
        results3 = cursor.fetchall()
    except Exception as e:
        #print(e)
        pass

    sql = "SELECT * FROM emergency"
    try:
        cursor.execute(sql)
        results4 = cursor.fetchall()
    except Exception as e:
        #print(e)
        pass

    return render_template('aview_behv.html', data1=results1, data2=results2, data3=results3, data4=results4)


@app.route('/viewbehv')
def viewb():
    rmr_cnt = 0
    neg_cnt = 0
    pos_cnt = 0
    total_cnt = 0
    pickle_in = open("sentiment_model.pickle", "rb")

    classifier = pickle.load(pickle_in)
    sql = "SELECT * FROM tweetdata"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
    except Exception as e:
        #print(e)
        pass
    for row in results:
        custom_tweet = row[1]
        custom_tokens = remove_noise(word_tokenize(custom_tweet))
        #print(custom_tweet, classifier.classify(dict([token, True] for token in custom_tokens)))
        senti = classifier.classify(dict([token, True] for token in custom_tokens))
        #print(senti)
        if senti == "Negative":
            neg_cnt += 1
            sql = "INSERT INTO negtweet(tweet,keywrd) VALUES ('%s', '%s')" % (row[1], row[2])
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
        if senti == "Positive":
            pos_cnt += 1
            sql = "INSERT INTO postweet(tweet,keywrd) VALUES ('%s', '%s')" % (row[1], row[2])
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()

        patt, emergency = get_pattern(row[1])

        if patt == 1:
            sql = "INSERT INTO rmrtweet(tweet,keywrd,userid) VALUES ('%s', '%s', '%s')" % (row[1], row[2], row[0])
            rmr_cnt += 1
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
        if emergency >= 1:
            sql = "INSERT INTO emergency(tweet,userid) VALUES ('%s', '%s')" % (row[1], row[0])
            rmr_cnt += 1
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()

    total_cnt = neg_cnt + pos_cnt
    session['neg_cnt'] = neg_cnt
    session['pos_cnt'] = pos_cnt
    session['rmr_cnt'] = rmr_cnt
    session['total_cnt'] = total_cnt
    pos_polarity = float(pos_cnt) / total_cnt * 100
    neg_polarity = float(neg_cnt) / total_cnt * 100
    session['pos_polarity'] = pos_polarity
    session['neg_polarity'] = neg_polarity
    sql = "SELECT * FROM postweet"
    try:
        cursor.execute(sql)
        results1 = cursor.fetchall()
    except Exception as e:
        #print(e)
        pass

    sql = "SELECT * FROM negtweet"
    try:
        cursor.execute(sql)
        results2 = cursor.fetchall()
    except Exception as e:
        #print(e)
        pass

    sql = "SELECT * FROM rmrtweet"
    try:
        cursor.execute(sql)
        results3 = cursor.fetchall()
    except Exception as e:
        #print(e)
        pass

    sql = "SELECT * FROM emergency"
    try:
        cursor.execute(sql)
        results4 = cursor.fetchall()
    except Exception as e:
        #print(e)
        pass

    return render_template('view_behv.html', data1=results1, data2=results2, data3=results3, data4=results4)


@app.route('/aview_behv')
def aviewb():
    rmr_cnt = 0
    neg_cnt = 0
    pos_cnt = 0
    total_cnt = 0
    pickle_in = open("sentiment_model.pickle", "rb")

    classifier = pickle.load(pickle_in)
    sql = "SELECT * FROM tweetdata"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
    except Exception as e:
        #print(e)
        pass
    for row in results:
        custom_tweet = row[1]
        custom_tokens = remove_noise(word_tokenize(custom_tweet))
        #print(custom_tweet, classifier.classify(dict([token, True] for token in custom_tokens)))
        senti = classifier.classify(dict([token, True] for token in custom_tokens))
        #print(senti)
        if senti == "Negative":
            neg_cnt += 1
            sql = "INSERT INTO negtweet(tweet,keywrd) VALUES ('%s', '%s')" % (row[1], row[2])
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
        if senti == "Positive":
            pos_cnt += 1
            sql = "INSERT INTO postweet(tweet,keywrd) VALUES ('%s', '%s')" % (row[1], row[2])
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()

        patt, emergency = get_pattern(row[1])

        if patt == 1:
            sql = "INSERT INTO rmrtweet(tweet,keywrd,userid) VALUES ('%s', '%s', '%s')" % (row[1], row[2], row[0])
            rmr_cnt += 1
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()
        if emergency >= 1:
            sql = "INSERT INTO emergency(tweet,userid) VALUES ('%s', '%s')" % (row[1], row[0])
            rmr_cnt += 1
            try:
                cursor.execute(sql)
                db.commit()
            except:
                db.rollback()

    total_cnt = neg_cnt + pos_cnt
    session['neg_cnt'] = neg_cnt
    session['pos_cnt'] = pos_cnt
    session['rmr_cnt'] = rmr_cnt
    session['total_cnt'] = total_cnt
    pos_polarity = float(pos_cnt) / total_cnt * 100
    neg_polarity = float(neg_cnt) / total_cnt * 100
    session['pos_polarity'] = pos_polarity
    session['neg_polarity'] = neg_polarity
    sql = "SELECT * FROM postweet"
    try:
        cursor.execute(sql)
        results1 = cursor.fetchall()
    except Exception as e:
        #print(e)
        pass

    sql = "SELECT * FROM negtweet"
    try:
        cursor.execute(sql)
        results2 = cursor.fetchall()
    except Exception as e:
        #print(e)
        pass

    sql = "SELECT * FROM rmrtweet"
    try:
        cursor.execute(sql)
        results3 = cursor.fetchall()
    except Exception as e:
        #print(e)
        pass
    sql = "SELECT * FROM emergency"
    try:
        cursor.execute(sql)
        results4 = cursor.fetchall()
    except Exception as e:
        #print(e)
        pass

    return render_template('aview_behv.html', data1=results1, data2=results2, data3=results3, data4=results4)


def get_tweets(username):
    #print("query==", username)
    consumer_key = 'nADq6hWpYelr6LNbEwW0KukbP'
    consumer_secret = 'WlaMx8DgqyykPLDsZ8hNf726D5gh9tctAmVgg3P5Ky0jfXuc3m'
    access_key = '2374984802-2LhijeLYF75itTfyjIlF4XoAYRPQB7kr8Dys2s9'
    access_secret = 'fuvJZd2fOOryJxFHmnrnzUghCsn6GHWEDEpohMx9lcUF4'
    # Authorization to consumer key and consumer secret
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

    # Access to user's access key and access secret
    auth.set_access_token(access_key, access_secret)

    # Calling api
    api = tweepy.API(auth)
    number_of_tweets = 20
    if username == "":
        tweets = api.home_timeline()
    else:
        tweets = tweepy.Cursor(api.search, q=username, result_type="recent", lang="en").items(200)
        sql = "DELETE from tweetdata"
        sql1 = "TRUNCATE negtweet"
        sql2 = "TRUNCATE postweet"
        sql3 = "TRUNCATE rmrtweet"
        sql4 = "TRUNCATE emergency"
        try:
            cursor.execute(sql)
            db.commit()
            cursor.execute(sql1)
            db.commit()
            cursor.execute(sql2)
            db.commit()
            cursor.execute(sql3)
            db.commit()
            cursor.execute(sql4)
            db.commit()
        except:
            db.rollback()

    for tweet in tweets:
      #  print(tweet.user.name, " said", tweet.text)

        sql = "INSERT INTO tweetdata(userid,tweets,keywrd) VALUES ('%s', '%s', '%s')" % (
        tweet.user.name, tweet.text, username)
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()

    return tweets


@app.route('/view_users')
def view_user():
    sql = "SELECT * FROM user"
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
    except Exception as e:
       # print(e)
        pass


    return render_template('view_users.html', data=results)


if __name__ == "__main__":
    app.run(debug=True)
