-- MySQL dump 10.13  Distrib 5.7.29, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: twitter_data
-- ------------------------------------------------------
-- Server version	5.7.29-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin` (
  `idadmin` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idadmin`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'admin','admin'),(2,'a','a');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `emergency`
--

DROP TABLE IF EXISTS `emergency`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `emergency` (
  `idemergency` int(11) NOT NULL AUTO_INCREMENT,
  `tweet` varchar(500) DEFAULT NULL,
  `username` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`idemergency`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `emergency`
--

LOCK TABLES `emergency` WRITE;
/*!40000 ALTER TABLE `emergency` DISABLE KEYS */;
/*!40000 ALTER TABLE `emergency` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `negtweet`
--

DROP TABLE IF EXISTS `negtweet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `negtweet` (
  `tweet` text,
  `keywrd` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `negtweet`
--

LOCK TABLES `negtweet` WRITE;
/*!40000 ALTER TABLE `negtweet` DISABLE KEYS */;
INSERT INTO `negtweet` VALUES ('RT @DrizzyJeri: Before we all die by corona virus\n            anyone wanna... yunno.. https://t.co/dqOlXs8gIH','corona virus'),('RT @all_smilesss: Magic Johnson watching the NBA get canceled due to the corona virus https://t.co/5vtmr49q0D','corona virus'),('Corona virus and global warming coordinating before ending humanity. https://t.co/2UNi4TDG2t','corona virus'),('RT @desimojito: No Fatwa against Corona Virus yet ?','corona virus'),('RT @bainjal: Kamalnath has asked the governor to delay his floor test citing the corona virus epidemic','corona virus'),('RT @midnitewalks: corona virus: yOU READY TO FUCKING DIE\nme: https://t.co/EMUk0DuXIf','corona virus'),('RT @midnitewalks: corona virus: yOU READY TO FUCKING DIE\nme: https://t.co/EMUk0DuXIf','corona virus'),('RT @nayeli_parra: Corona virus: \n\nCollege students: https://t.co/Kk7cJJ3WDj','corona virus'),('RT @Marco_Acortes: Corona virus....its coming','corona virus'),('@SaketGokhale @sudhirchaudhary This guy @sudhirchaudhary is a scu#bag, a virus worse than corona...shud be put to rest ASAP....','corona virus'),('RT @Marco_Acortes: Corona virus....its coming','corona virus'),('RT @tarrikittyartt: this corona virus shit really got bitches acting fully different. https://t.co/8yneXNtqX6','corona virus'),('So I had swine flu does this mean imma get corona virus?','corona virus'),('RT @midnitewalks: corona virus: yOU READY TO FUCKING DIE\nme: https://t.co/EMUk0DuXIf','corona virus'),('If you have the corona virus and drink a modelo they cancel out','corona virus'),('@nautalii Can you not i dont want the corona virus...thanks','corona virus'),('RT @CSharbonow: If you played football at Valencia high school and drank from the trough, your immune to corona virus.','corona virus'),('RT @Tife_fabunmi: Callum Hudson Odoi also tested positive for Corona virus? \nPremier League should cancel this season please. Please!','corona virus'),('Can we get corona virus if we played in one of these before? https://t.co/NmxiFW8ctX','corona virus'),('RT @midnitewalks: corona virus: yOU READY TO FUCKING DIE\nme: https://t.co/EMUk0DuXIf','corona virus'),('Not got corona virus but think am gonna stick myself in isolation anyway','corona virus'),('RT @VH1PNUT___: THIS CORONA VIRUS SONG HARD AF LOL\n\n https://t.co/PDIrNNNeko','corona virus'),('RT @Thomasfinesse23: If a girl with Corona Virus gets her period, is that a Michelada ?','corona virus');
/*!40000 ALTER TABLE `negtweet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `postweet`
--

DROP TABLE IF EXISTS `postweet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `postweet` (
  `tweet` text,
  `keywrd` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `postweet`
--

LOCK TABLES `postweet` WRITE;
/*!40000 ALTER TABLE `postweet` DISABLE KEYS */;
INSERT INTO `postweet` VALUES ('RT @NiggazWILIN: Corona virus, Flu Virus, Miley Cyrus IDGAF\n\nThey bet not close the liquor store','corona virus'),('RT @AlbertsStuff: hey mr @LILUZIVERT can you drop part 2 so i have something to listen to trying to find corona virus supplies','corona virus'),('RT @valerieornelass: my man got the corona virus...everyone needa stay away from him','corona virus'),('RT @KB_Ban88: The corona virus started in the Ivy Pool you all swim in every sunday','corona virus'),('RT @NoelCastanza: Someone should start a rumour that oral sex cures Corona virus\n\nYeah boy!!!\nTalk about sloppy toppy','corona virus'),('RT @kennagq: Fabrizio Romano announcing corona virus like  transfers','corona virus'),('@RightWingWatch Amen, I am now immune from Corona. I receive by faith and will never take the Corona Virus, in Jesus Name!','corona virus'),('We defeat Corona Virus by having the Mustang Pub filled weekly !','corona virus'),('@WhatIsSecks in the corona virus WHAT','corona virus'),('RT @pksayyy: corona virus ruined a lot of opportunities and once in a life time experience','corona virus'),('RT @lilearthangelk: Stocking up on shrooms for the corona virus','corona virus'),('RT @pksayyy: corona virus ruined a lot of opportunities and once in a life time experience','corona virus'),('RT @herapatra: The Corona virus will not touch me in Jesus name!!! I rebuke such evil','corona virus'),('If the internet gets down because of the corona virus,  are you well stacked with resources for the rest of the year to make you happy','corona virus'),('RT @MohamedAlshaiba: Friday the 13th Corona Virus edition','corona virus'),('RT @NiggazWILIN: Corona virus, Flu Virus, Miley Cyrus IDGAF\n\nThey bet not close the liquor store','corona virus');
/*!40000 ALTER TABLE `postweet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rmrtweet`
--

DROP TABLE IF EXISTS `rmrtweet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rmrtweet` (
  `tweet` text,
  `keywrd` varchar(100) DEFAULT NULL,
  `userid` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rmrtweet`
--

LOCK TABLES `rmrtweet` WRITE;
/*!40000 ALTER TABLE `rmrtweet` DISABLE KEYS */;
/*!40000 ALTER TABLE `rmrtweet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tweetdata`
--

DROP TABLE IF EXISTS `tweetdata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tweetdata` (
  `userid` varchar(100) DEFAULT NULL,
  `tweets` text,
  `keywrd` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tweetdata`
--

LOCK TABLES `tweetdata` WRITE;
/*!40000 ALTER TABLE `tweetdata` DISABLE KEYS */;
INSERT INTO `tweetdata` VALUES ('Adebanjo oluwapelumi','RT @DrizzyJeri: Before we all die by corona virus\n            anyone wanna... yunno.. https://t.co/dqOlXs8gIH','corona virus'),('Brandon','RT @all_smilesss: Magic Johnson watching the NBA get canceled due to the corona virus https://t.co/5vtmr49q0D','corona virus'),('a solid 5, vibin','Corona virus and global warming coordinating before ending humanity. https://t.co/2UNi4TDG2t','corona virus'),('Devika','RT @desimojito: No Fatwa against Corona Virus yet ?','corona virus'),('Rachit Gupta','RT @bainjal: Kamalnath has asked the governor to delay his floor test citing the corona virus epidemic','corona virus'),('Rub','RT @NiggazWILIN: Corona virus, Flu Virus, Miley Cyrus IDGAF\n\nThey bet not close the liquor store','corona virus'),('Edgy_vibes','RT @AlbertsStuff: hey mr @LILUZIVERT can you drop part 2 so i have something to listen to trying to find corona virus supplies','corona virus'),('CHA$LYN','RT @valerieornelass: my man got the corona virus...everyone needa stay away from him','corona virus'),('_southwestconfidential','RT @KB_Ban88: The corona virus started in the Ivy Pool you all swim in every sunday','corona virus'),('tierra','RT @midnitewalks: corona virus: yOU READY TO FUCKING DIE\nme: https://t.co/EMUk0DuXIf','corona virus'),('Da 4:20 Poet','RT @NoelCastanza: Someone should start a rumour that oral sex cures Corona virus\n\nYeah boy!!!\nTalk about sloppy toppy','corona virus'),('KPANTI','RT @kennagq: Fabrizio Romano announcing corona virus like  transfers','corona virus'),('Millions Think Like Me','@RightWingWatch Amen, I am now immune from Corona. I receive by faith and will never take the Corona Virus, in Jesus Name!','corona virus'),('Matty Ciezki','We defeat Corona Virus by having the Mustang Pub filled weekly !','corona virus'),('Delaina','RT @midnitewalks: corona virus: yOU READY TO FUCKING DIE\nme: https://t.co/EMUk0DuXIf','corona virus'),('Honeybeetch','RT @nayeli_parra: Corona virus: \n\nCollege students: https://t.co/Kk7cJJ3WDj','corona virus'),('brown jeezus','RT @Marco_Acortes: Corona virus....its coming','corona virus'),('Mozart','@SaketGokhale @sudhirchaudhary This guy @sudhirchaudhary is a scu#bag, a virus worse than corona...shud be put to rest ASAP....','corona virus'),('yudha ewo','RT @Marco_Acortes: Corona virus....its coming','corona virus'),('Nyne','RT @tarrikittyartt: this corona virus shit really got bitches acting fully different. https://t.co/8yneXNtqX6','corona virus'),('Alexandra Jeann','So I had swine flu does this mean imma get corona virus?','corona virus'),('jacobo','RT @midnitewalks: corona virus: yOU READY TO FUCKING DIE\nme: https://t.co/EMUk0DuXIf','corona virus'),('ro','@WhatIsSecks in the corona virus WHAT','corona virus'),('cristal','If you have the corona virus and drink a modelo they cancel out','corona virus'),('betty','RT @pksayyy: corona virus ruined a lot of opportunities and once in a life time experience','corona virus'),('addicted to my own self destruction','RT @lilearthangelk: Stocking up on shrooms for the corona virus','corona virus'),('Varelas','@nautalii Can you not i dont want the corona virus...thanks','corona virus'),('gean mae','RT @pksayyy: corona virus ruined a lot of opportunities and once in a life time experience','corona virus'),('Brian Malette','RT @CSharbonow: If you played football at Valencia high school and drank from the trough, your immune to corona virus.','corona virus'),('Vianey','RT @herapatra: The Corona virus will not touch me in Jesus name!!! I rebuke such evil','corona virus'),('N-Kira','If the internet gets down because of the corona virus,  are you well stacked with resources for the rest of the year to make you happy','corona virus'),('Mustafa Y. Fakhoury','RT @MohamedAlshaiba: Friday the 13th Corona Virus edition','corona virus'),('Leo','RT @Tife_fabunmi: Callum Hudson Odoi also tested positive for Corona virus? \nPremier League should cancel this season please. Please!','corona virus'),('xBizco','Can we get corona virus if we played in one of these before? https://t.co/NmxiFW8ctX','corona virus'),('rachel','RT @midnitewalks: corona virus: yOU READY TO FUCKING DIE\nme: https://t.co/EMUk0DuXIf','corona virus'),('The Aslamic State','Not got corona virus but think am gonna stick myself in isolation anyway','corona virus'),('mr. hotspot','RT @VH1PNUT___: THIS CORONA VIRUS SONG HARD AF LOL\n\n https://t.co/PDIrNNNeko','corona virus'),('emsxcv','RT @NiggazWILIN: Corona virus, Flu Virus, Miley Cyrus IDGAF\n\nThey bet not close the liquor store','corona virus'),('Lizz Romo','RT @Thomasfinesse23: If a girl with Corona Virus gets her period, is that a Michelada ?','corona virus');
/*!40000 ALTER TABLE `tweetdata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `iduser` int(11) NOT NULL AUTO_INCREMENT,
  `fname` varchar(45) DEFAULT NULL,
  `lname` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `mob` varchar(45) DEFAULT NULL,
  `username` varchar(45) DEFAULT NULL,
  `password` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`iduser`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'suraj','c','sur@gmail.com','9730592659','suraj','12345678'),(5,'sumedh','j','sum@gmail.com','9876543210','sumedh','12345678'),(7,'a','a','a','a','a','a');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-03-13 12:18:48
