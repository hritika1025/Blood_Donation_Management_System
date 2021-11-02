CREATE DATABASE IF NOT EXISTS blood_donation_dbms;
USE blood_donation_dbms;
CREATE TABLE IF NOT EXISTS  `Blood_bank` (
           `Password` varchar(100) NOT NULL,
           `License_number` varchar(100) NOT NULL,
           `Blood_bank_name` varchar(100) NOT NULL,
           `Owner_name` varchar(100) NOT NULL,
           `Email` varchar(100) NOT NULL,
           `Phone_number` int NOT NULL,
           `Address` varchar(100) NOT NULL,
           `Pincode` int NOT NULL,
           `City` varchar(100) NOT NULL,
           `District`varchar(100) NOT NULL,
           `State` varchar(100) NOT NULL,
           `Website` varchar(100) ,
           `Verification` varchar(100) NOT NULL DEFAULT 'Not Verified',
           PRIMARY KEY (`Username`) );
           
CREATE TABLE IF NOT EXISTS `Blood_bank_timings` (
		    `License_number` varchar(100) NOT NULL,
            `Opening_time` time NOT NULL,
            `Closing_time` time NOT NULL,
            `Weekday` varchar(50) NOT NULL,
            PRIMARY KEY (`Username` , `Weekday`), 
            FOREIGN KEY (`Username`) REFERENCES `Blood_bank`(`Username`));
            
CREATE TABLE IF NOT EXISTS `Blood_stock` (
            `Id` int NOT NULL AUTO_INCREMENT,
            `Username` varchar(100) NOT NULL,
            `Blood_group` varchar(10) NOT NULL,
            `Adding_date` date ,
            `Removing_date` date,
            `Units_added` int,
            `Units_removed` int,
            PRIMARY KEY (`Id`),
            FOREIGN KEY (`Username`) REFERENCES `Blood_bank`(`Username`)
            ) AUTO_INCREMENT=1;
            
  CREATE TABLE IF NOT EXISTS `Donor` (
              `Email_id` varchar(100) NOT NULL,
              `Password` varchar(100) NOT NULL ,
              `First_name` varchar(100) NOT NULL,
              `Last_name` varchar(100) ,
              `Age` int NOT NULL,
              `Gender` varchar(30) NOT NULL,
              `Blood_group` varchar(20) NOT NULL,
              `Eligibility` bool NOT NULL,
              `Phone_num` int NOT NULL,
              `Address` varchar(100) NOT NULL,
              `City` varchar(30) NOT NULL,
              `District` varchar(50) NOT NULL,
              `Pincode` int NOT NULL,
              `State` varchar(100) NOT NULL,
              `Frequent`  bool NOT NULL,
              PRIMARY KEY (`Email_id`) );

CREATE TABLE IF NOT EXISTS `Donations` (
		    `Email_id` varchar(100) NOT NULL,
            `Date` date NOT NULL,
            `Units` int NOT NULL,
            `Blood_group` varchar(10) NOT NULL,
            PRIMARY KEY (`Email_id`),
            FOREIGN KEY (`Email_id`) REFERENCES `Donor`(`Email_id`) );

CREATE TABLE IF NOT EXISTS `Notif_Admin_to_Blood_bank` (
            `Id` int NOT NULL,
            `Username` varchar(100) NOT NULL,
            `Message` varchar(500) NOT NULL,
            `Date` date NOT NULL,
            PRIMARY KEY (`Id`),
            FOREIGN KEY (`Username`) REFERENCES `Blood_bank`(`Username`) );
            
CREATE TABLE IF NOT EXISTS `Notif_Blood_bank_to_Donor` (
            `Id` int NOT NULL,
            `Blood_bank_user` varchar(100) NOT NULL,
            `Donor_user` varchar(100) NOT NULL,
            `Message` varchar(500) NOT NULL,
            `Date` date NOT NULL,
            PRIMARY KEY (`Id`),
            FOREIGN KEY (`Blood_bank_user`) REFERENCES `Blood_bank`(`Username`),
			FOREIGN KEY (`Donor_user`) REFERENCES `Donor`(`Email_id`));
            
CREATE TABLE IF NOT EXISTS `Notif_Admin_to_Donor` (
            `Id` int NOT NULL,
            `Donor_user` varchar(100) NOT NULL,
            `Message` varchar(500) NOT NULL,
            `Date` date NOT NULL,
            PRIMARY KEY (`Id`),
            FOREIGN KEY (`Donor_user`) REFERENCES `Donor`(`Email_id`) );
            
CREATE TABLE IF NOT EXISTS `Message_to_admin` (
            `Id` int NOT NULL,
            `Name` varchar(100) NOT NULL,
            `Email_id` varchar(100) NOT NULL,
            `phone_num` int NOT NULL,
            `Message` varchar(500) NOT NULL,
            `Date` date NOT NULL,
            PRIMARY KEY (`Id`) );
            
 CREATE TABLE IF NOT EXISTS `Post_by_admin` (
            `Id` int NOT NULL,
            `Heading` varchar(200) NOT NULL,
            `Post` varchar(700) NOT NULL,
            `Date` date NOT NULL,
            PRIMARY KEY (`Id`) );