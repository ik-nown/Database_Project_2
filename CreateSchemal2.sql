/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

DROP DATABASE IF EXISTS `TRUONGHOC2`;

CREATE DATABASE TRUONGHOC2 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE `TRUONGHOC2`;

--
-- Table structure for table `TRUONG`
--

DROP TABLE IF EXISTS `TRUONG`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;

CREATE TABLE `TRUONG` (
    `MATR` int NOT NULL,
    `TENTR` varchar(100) DEFAULT NULL,
    `DCHITR` varchar(200) DEFAULT NULL,
    PRIMARY KEY (`MATR`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `HS`
--

DROP TABLE IF EXISTS `HS`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;

CREATE TABLE `HS`(
    `MAHS` INT NOT NULL,
    `HO` varchar(30) DEFAULT NULL,
    `TEN` varchar(100) DEFAULT NULL,
    `CCCD` varchar(12) DEFAULT NULL,
    `NTNS`date DEFAULT NULL,
    `DCHI_HS` varchar(200) DEFAULT NULL,
    PRIMARY KEY (`MAHS`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `HOC`
--

DROP TABLE IF EXISTS `HOC`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;

CREATE TABLE `HOC` (
    `MATR` int NOT NULL,
    `MAHS` int NOT NULL,
    `NAMHOC` varchar(4) NOT NULL,
    `DIEMTB`  float DEFAULT NULL,
    `XEPLOAI`varchar (10) DEFAULT NULL,
    `KQUA` ENUM ("Chưa hoàn thành", "Hoàn thành"),
    PRIMARY KEY (`MATR`, `MAHS`, `NAMHOC`),
    CONSTRAINT `HOC_TRUONG_FK` FOREIGN KEY (`MATR`) REFERENCES `TRUONG` (`MATR`), 
    CONSTRAINT `HOC_HS_FK` FOREIGN KEY (`MAHS`) REFERENCES `HS` (`MAHS`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

-- Drop foreign key constraints
ALTER TABLE `HOC` DROP FOREIGN KEY `HOC_TRUONG_FK`;
ALTER TABLE `HOC` DROP FOREIGN KEY `HOC_HS_FK`;

-- Add foreign key constraints again
ALTER TABLE `HOC` ADD CONSTRAINT `HOC_TRUONG_FK` FOREIGN KEY (`MATR`) REFERENCES `TRUONG` (`MATR`);
ALTER TABLE `HOC` ADD CONSTRAINT `HOC_HS_FK` FOREIGN KEY (`MAHS`) REFERENCES `HS` (`MAHS`);
-- Create index

CREATE INDEX `IDX_TENTR` ON TRUONG (`TENTR`);
CREATE INDEX `IDX_XEPLOAI` ON HOC (`XEPLOAI`);
CREATE INDEX `IDX_NAMHOC` ON HOC (`NAMHOC`);