Drop database blood_donation_dbms;
CREATE DATABASE IF NOT EXISTS blood_donation_dbms;
USE blood_donation_dbms;
CREATE TABLE IF NOT EXISTS `Admin` (
            `Email` varchar(100) NOT NULL,
            `Password` varchar(100) NOT NULL,
	        PRIMARY KEY(`Email`) );
SELECT * FROM Blood_bank;
CREATE TABLE IF NOT EXISTS  `Blood_bank` (
           `Password` varchar(100) NOT NULL,
           `License_number` varchar(100) NOT NULL,
           `Blood_bank_name` varchar(100) NOT NULL,
           `Owner_name` varchar(100) NOT NULL,
           `Email` varchar(100) NOT NULL,
           `Phone_number` varchar(20) NOT NULL,
           `Street` varchar(100) NOT NULL,
           `Pincode` varchar(20) NOT NULL,
           `City` varchar(100) NOT NULL,
           `District`varchar(100) NOT NULL,
           `State` varchar(100) NOT NULL,
           `Website` varchar(100) ,
           `Verification` varchar(100) NOT NULL DEFAULT 'Not Verified',
           PRIMARY KEY (`License_Number`) );
CREATE TABLE IF NOT EXISTS `Blood_bank_timings` (
		    `License_number` varchar(100) NOT NULL,
            `Opening_time` time NOT NULL,
            `Closing_time` time NOT NULL,
            `Weekday` varchar(50) NOT NULL,
            PRIMARY KEY (`License_Number` , `Weekday`), 
            FOREIGN KEY (`License_Number`) REFERENCES `Blood_bank`(`License_Number`)  ON DELETE CASCADE);

            
CREATE TABLE IF NOT EXISTS `Blood_stock` (
            `Id` int NOT NULL AUTO_INCREMENT,
            `License_Number` varchar(100) NOT NULL,
            `Blood_group` varchar(10) NOT NULL,
            `Adding_date` date ,
            `Removing_date` date,
            `Units_added` int,
            `Units_removed` int,
            PRIMARY KEY (`Id`),
            FOREIGN KEY (`License_Number`) REFERENCES `Blood_bank`(`License_Number`) ON DELETE CASCADE
            ) AUTO_INCREMENT=1;

  CREATE TABLE IF NOT EXISTS `Donor` (
              `Email_id` varchar(100) NOT NULL,
              `Password` varchar(100) NOT NULL ,
              `First_name` varchar(100) NOT NULL,
              `Last_name` varchar(100) ,
              `Age` varchar(10) NOT NULL,
              `Gender` varchar(30) NOT NULL,
              `Blood_group` varchar(20) NOT NULL,
              `Eligibility` varchar(5) NOT NULL DEFAULT 'False',
              `Phone_num` varchar(20) NOT NULL,
              `Street` varchar(100) NOT NULL,
              `City` varchar(30) NOT NULL,
              `District` varchar(50) NOT NULL,
              `Pincode` varchar(20) NOT NULL,
              `State` varchar(100) NOT NULL,
              `Frequent_Donor` varchar(5) NOT NULL DEFAULT 'NO',
              PRIMARY KEY (`Email_id`) );

CREATE TABLE IF NOT EXISTS `Donations` (
		    `Email_id` varchar(100) NOT NULL,
            `Date` date NOT NULL,
            `Units` int NOT NULL,
            `Blood_group` varchar(10) NOT NULL,
            PRIMARY KEY (`Email_id`),
            FOREIGN KEY (`Email_id`) REFERENCES `Donor`(`Email_id`)  ON DELETE CASCADE );

CREATE TABLE IF NOT EXISTS `Notif_Admin_to_Blood_bank` (
            `Id` INT(11) NOT NULL AUTO_INCREMENT,
            `License_Number` varchar(100) NOT NULL,
            `Message` varchar(5000) NOT NULL,
            `Date` date NOT NULL,
            PRIMARY KEY (`Id`),
            FOREIGN KEY (`License_Number`) REFERENCES `Blood_bank`(`License_Number`)  ON DELETE CASCADE ) AUTO_INCREMENT=1;
            
CREATE TABLE IF NOT EXISTS `Notif_Blood_bank_to_Donor` (
            `Id` INT(11) NOT NULL AUTO_INCREMENT,
            `Blood_bank_user` varchar(100) NOT NULL,
            `Donor_user` varchar(100) NOT NULL,
            `Message` varchar(5000) NOT NULL,
            `Date` date NOT NULL,
            PRIMARY KEY (`Id`),
            FOREIGN KEY (`Blood_bank_user`) REFERENCES `Blood_bank`(`License_Number`) ON DELETE CASCADE,
			FOREIGN KEY (`Donor_user`) REFERENCES `Donor`(`Email_id`) ON DELETE CASCADE)AUTO_INCREMENT=1;
            
CREATE TABLE IF NOT EXISTS `Notif_Admin_to_Donor` (
            `Id` INT(11) NOT NULL AUTO_INCREMENT,
            `Donor_user` varchar(100) NOT NULL,
            `Message` varchar(5000) NOT NULL,
            `Date` date NOT NULL,
            PRIMARY KEY (`Id`),
            FOREIGN KEY (`Donor_user`) REFERENCES `Donor`(`Email_id`)  ON DELETE CASCADE) AUTO_INCREMENT=1;
            
CREATE TABLE IF NOT EXISTS `Message_to_admin` (
            `Id` INT(11) NOT NULL AUTO_INCREMENT,
            `Name` varchar(100) NOT NULL,
            `Email_id` varchar(100) NOT NULL,
            `phone_num` varchar(20) NOT NULL,
            `Message` varchar(5000) NOT NULL,
            `Date` date NOT NULL,
            PRIMARY KEY (`Id`) )AUTO_INCREMENT=1;


 CREATE TABLE IF NOT EXISTS `Post_by_admin` (
            `Id` int NOT NULL AUTO_INCREMENT,
            `Heading` varchar(200) NOT NULL,
            `Post` varchar(700) NOT NULL,
            `Date` date NOT NULL,
            PRIMARY KEY (`Id`) )AUTO_INCREMENT=1;