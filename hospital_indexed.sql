CREATE DATABASE  IF NOT EXISTS `hospital` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `hospital`;
-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: localhost    Database: hospital
-- ------------------------------------------------------
-- Server version	8.0.18

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admit`
--

DROP TABLE IF EXISTS `admit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admit` (
  `Outpatient_Treatment_ID` int(11) NOT NULL,
  `Inpatient_Treatment_ID` int(11) NOT NULL,
  `Description` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`Outpatient_Treatment_ID`,`Inpatient_Treatment_ID`),
  KEY `Admit_Inpatient_idx` (`Inpatient_Treatment_ID`),
  CONSTRAINT `Admit_Inpatient` FOREIGN KEY (`Inpatient_Treatment_ID`) REFERENCES `inpatient` (`Treatment_ID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `Admit_Outpatient` FOREIGN KEY (`Outpatient_Treatment_ID`) REFERENCES `outpatient` (`Treatment_ID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admit`
--

LOCK TABLES `admit` WRITE;
/*!40000 ALTER TABLE `admit` DISABLE KEYS */;
/*!40000 ALTER TABLE `admit` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `appointment`
--

DROP TABLE IF EXISTS `appointment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `appointment` (
  `Appointment_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Appointed_Date` date NOT NULL,
  `Appointed_Time` time DEFAULT NULL,
  `Description` varchar(180) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `Patient_ID` int(11) NOT NULL,
  PRIMARY KEY (`Appointment_ID`),
  KEY `Appointment_Patient_idx` (`Patient_ID`),
  CONSTRAINT `Appointment_Patient` FOREIGN KEY (`Patient_ID`) REFERENCES `patient` (`Patient_ID`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `appointment`
--

LOCK TABLES `appointment` WRITE;
/*!40000 ALTER TABLE `appointment` DISABLE KEYS */;
/*!40000 ALTER TABLE `appointment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bed`
--

DROP TABLE IF EXISTS `bed`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bed` (
  `Room_ID` int(11) NOT NULL,
  `Bed_ID` int(11) NOT NULL,
  PRIMARY KEY (`Room_ID`,`Bed_ID`),
  CONSTRAINT `Bed_Room` FOREIGN KEY (`Room_ID`) REFERENCES `room` (`Room_ID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bed`
--

LOCK TABLES `bed` WRITE;
/*!40000 ALTER TABLE `bed` DISABLE KEYS */;
INSERT INTO `bed` VALUES (4001,1),(4002,1),(4003,1),(4004,1),(4005,1),(5001,1),(5001,2),(5001,3),(5001,4),(5001,5),(5002,1),(5002,2),(5003,2),(5004,1),(5005,1);
/*!40000 ALTER TABLE `bed` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `correspond_to`
--

DROP TABLE IF EXISTS `correspond_to`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `correspond_to` (
  `Appointment_ID` int(11) NOT NULL,
  `Treatment_ID` int(11) NOT NULL,
  PRIMARY KEY (`Appointment_ID`,`Treatment_ID`),
  KEY `Correspond_To_Treatment_idx` (`Treatment_ID`),
  CONSTRAINT `Correspond_To_Appiontment` FOREIGN KEY (`Appointment_ID`) REFERENCES `appointment` (`Appointment_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Correspond_To_Treatment` FOREIGN KEY (`Treatment_ID`) REFERENCES `treatment` (`Treatment_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `correspond_to`
--

LOCK TABLES `correspond_to` WRITE;
/*!40000 ALTER TABLE `correspond_to` DISABLE KEYS */;
/*!40000 ALTER TABLE `correspond_to` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `department` (
  `Dept_ID` int(11) NOT NULL,
  `Dept_Name` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`Dept_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES (1,'Cardiology'),(2,'Emergency'),(3,'Intensive care unit'),(4,'Neurology'),(5,'Oncology'),(6,'Obstetrics and gynaecology'),(7,'Outpatient');
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `diagnose`
--

DROP TABLE IF EXISTS `diagnose`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `diagnose` (
  `Treatment_ID` int(11) NOT NULL,
  `Disease_ID` int(11) NOT NULL,
  PRIMARY KEY (`Treatment_ID`,`Disease_ID`),
  KEY `Diagnose_Disease_idx` (`Disease_ID`),
  CONSTRAINT `Diagnose_Disease` FOREIGN KEY (`Disease_ID`) REFERENCES `disease` (`Disease_ID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `Diagnose_Treatment` FOREIGN KEY (`Treatment_ID`) REFERENCES `treatment` (`Treatment_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `diagnose`
--

LOCK TABLES `diagnose` WRITE;
/*!40000 ALTER TABLE `diagnose` DISABLE KEYS */;
/*!40000 ALTER TABLE `diagnose` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `disease`
--

DROP TABLE IF EXISTS `disease`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `disease` (
  `Disease_ID` int(11) NOT NULL,
  `Disease_Name` varchar(180) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`Disease_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `disease`
--

LOCK TABLES `disease` WRITE;
/*!40000 ALTER TABLE `disease` DISABLE KEYS */;
INSERT INTO `disease` VALUES (1,'Cholera'),(2,'ADHD'),(3,'Arthritis'),(4,'Asthma'),(5,'Autism'),(6,'Avian Influenza'),(7,'Birth Defects'),(8,'Cancer'),(9,'Chlamydia'),(10,'Chronic Fatigue Syndrome'),(11,'Chronic Obstructive Pulmonary Disease (COPD)'),(12,'Diabetes'),(13,'Ebola (Ebola Virus Disease)'),(14,'Epilepsy'),(15,'Fetal Alcohol Syndrome'),(16,'Flu (Influenza)'),(17,'Genital Herpes (Herpes Simplex Virus)'),(18,'Giardiasis'),(19,'Gonorrhea'),(20,'Heart Disease'),(21,'Hepatitis'),(22,'HIV/AIDS'),(23,'Human papillomavirus (HPV)'),(24,'Kidney Disease (Chronic Kidney Disease)'),(25,'Meningitis'),(26,'Methicillin-resistant Staphylococcus aureus (MRSA)'),(27,'Microcephaly'),(28,'Middle East Respiratory Syndrome (MERS)'),(29,'Overweight and Obesity'),(30,'Parasites – Scabies'),(31,'Salmonella'),(32,'Scabies'),(33,'Sexually Transmitted Diseases'),(34,'Stroke'),(35,'Traumatic Brain Injury (TBI)'),(36,'Trichomonas Infection (Trichomoniasis)'),(37,'Tuberculosis (TB)'),(38,'Water-related Diseases'),(39,'Zika Virus');
/*!40000 ALTER TABLE `disease` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `disease_specialty`
--

DROP TABLE IF EXISTS `disease_specialty`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `disease_specialty` (
  `Disease_ID` int(11) NOT NULL,
  `Specialty` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`Disease_ID`,`Specialty`),
  CONSTRAINT `Disease_Specialty_Disease` FOREIGN KEY (`Disease_ID`) REFERENCES `disease` (`Disease_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `disease_specialty`
--

LOCK TABLES `disease_specialty` WRITE;
/*!40000 ALTER TABLE `disease_specialty` DISABLE KEYS */;
INSERT INTO `disease_specialty` VALUES (1,'Infectious'),(2,'Pediatrics'),(2,'Psychiatry'),(3,'Rheumatology'),(4,'Pulmonology'),(5,'Psychiatry'),(6,'Infectious'),(7,'Genetics'),(7,'Pediatrics'),(8,'Oncology'),(9,'Gynecology'),(9,'Infectious'),(9,'Urology'),(10,'Neurology'),(10,'Psychiatry'),(10,'Rheumatology'),(11,'Pulmonology'),(12,'Endocrinology'),(13,'Infectious'),(14,'Neurology'),(15,'Pediatrics'),(15,'Psychiatry'),(15,'Toxicology'),(16,'Infectious'),(17,'Infectious'),(18,'Infectious'),(19,'Infectious'),(20,'Cardiology'),(21,'Gastroenterology'),(21,'Hepatology'),(21,'Infectious'),(22,'Infectious'),(23,'Gynecology'),(23,'Infectious'),(23,'Oncology'),(24,'Nephrology'),(24,'Urology'),(25,'Infectious'),(25,'Neurology'),(26,'Infectious'),(27,'Genetics'),(27,'Neurology'),(27,'Psychiatry'),(28,'Infectious'),(29,'Endocrinology'),(30,'Dermatology'),(30,'Infectious'),(31,'Infectious'),(32,'Dermatology'),(32,'Infectious'),(33,'Infectious'),(34,'Neurology'),(35,'Neurosurgery'),(35,'Pediatrics'),(36,'Infectious'),(37,'Infectious'),(37,'Pulmonology'),(39,'Infectious');
/*!40000 ALTER TABLE `disease_specialty` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctor`
--

DROP TABLE IF EXISTS `doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctor` (
  `Employee_ID` int(11) NOT NULL,
  PRIMARY KEY (`Employee_ID`),
  CONSTRAINT `Doctor_Employee` FOREIGN KEY (`Employee_ID`) REFERENCES `employee` (`Employee_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor`
--

LOCK TABLES `doctor` WRITE;
/*!40000 ALTER TABLE `doctor` DISABLE KEYS */;
INSERT INTO `doctor` VALUES (101),(102),(103),(104),(105),(106),(107);
/*!40000 ALTER TABLE `doctor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctor_certification`
--

DROP TABLE IF EXISTS `doctor_certification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctor_certification` (
  `Employee_ID` int(11) NOT NULL,
  `Certification` varchar(180) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`Employee_ID`,`Certification`),
  CONSTRAINT `Doctor_Certification_Doctor` FOREIGN KEY (`Employee_ID`) REFERENCES `doctor` (`Employee_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor_certification`
--

LOCK TABLES `doctor_certification` WRITE;
/*!40000 ALTER TABLE `doctor_certification` DISABLE KEYS */;
INSERT INTO `doctor_certification` VALUES (101,'Certificate in Interventional Cardiology University Hospital Leiden, The Netherlands '),(104,'Cert. in SPECT and PET imaging. (University of Pennsylvania, USA)');
/*!40000 ALTER TABLE `doctor_certification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `doctor_degree`
--

DROP TABLE IF EXISTS `doctor_degree`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `doctor_degree` (
  `Employee_ID` int(11) NOT NULL,
  `Degree` varchar(180) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`Employee_ID`,`Degree`),
  CONSTRAINT `Doctor_Degree_Doctor` FOREIGN KEY (`Employee_ID`) REFERENCES `doctor` (`Employee_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `doctor_degree`
--

LOCK TABLES `doctor_degree` WRITE;
/*!40000 ALTER TABLE `doctor_degree` DISABLE KEYS */;
INSERT INTO `doctor_degree` VALUES (101,'B.SC. Medicine, Faculty of Medicine, Siriraj Hospital. Mahidol University, Bangkok, Thailand'),(101,'M.D. Medicine, Faculty of Medicine Siriraj Hospital. Mahidol University, Bangkok, Thailand '),(102,'M.D. (First Class Honors), Faculty of Medicine, Siriraj Hospital, Mahidol University, 2011'),(103,'Doctor of Medicine, Faculty of Medicine, Rangsit University, 2005'),(105,'Medical Degree (First degree honor) Faculty of Medicine, Siriraj Hospital, Mahidol University, 2006'),(106,'Doctor of Medicine degree (M.D.) Faculty of Medicine Siriraj Hospital, Mahidol University, Thailand 1984'),(107,'Doctor of Medicine,  Faculty of Medicine, Siriraj Hospital, Mahidol University, 2011');
/*!40000 ALTER TABLE `doctor_degree` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `drug`
--

DROP TABLE IF EXISTS `drug`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `drug` (
  `Drug_ID` int(11) NOT NULL,
  `Drug_Name` varchar(180) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`Drug_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `drug`
--

LOCK TABLES `drug` WRITE;
/*!40000 ALTER TABLE `drug` DISABLE KEYS */;
INSERT INTO `drug` VALUES (1,'Abacavir'),(2,'Abacavir / dolutegravir / lamivudine'),(3,'Abacavir / lamivudine'),(4,'Acyclovir'),(5,'Alemtuzumab'),(6,'Alendronate'),(7,'Allopurinol'),(8,'Amifostine'),(9,'Amikacin'),(10,'Aminocaproic Acid'),(11,'Amitriptyline'),(12,'Amlodipine'),(13,'Amoxicillin'),(14,'Amoxicillin / clavulanic acid'),(15,'Amphotericin B'),(16,'Ampicillin'),(17,'Anti-Inhibitor Coagulant Complex (FEIBA)'),(18,'Anti-thymocyte globulin'),(19,'Aprepitant'),(20,'Asparaginase'),(21,'Atazanavir'),(22,'Atenolol'),(23,'Atovaquone'),(24,'Azithromycin'),(25,'Baclofen'),(26,'Bleomycin'),(27,'Bortezomib'),(28,'Bosentan'),(29,'Busulfan'),(30,'Calcium'),(31,'Captopril'),(32,'Carbamazepine'),(33,'Carboplatin'),(34,'Carmustine'),(35,'Cefaclor'),(36,'Cefepime'),(37,'Cefixime'),(38,'Ceftazidime'),(39,'Cefuroxime'),(40,'Celecoxib'),(41,'Cephalexin'),(42,'Cidofovir'),(43,'Cisplatin'),(44,'Cladribine'),(45,'Clarithromycin'),(46,'Clindamycin'),(47,'Clobazam'),(48,'Clofarabine'),(49,'Codeine'),(50,'Crizotinib'),(51,'Cyclobenzaprine'),(52,'Cyclophosphamide'),(53,'Cyclosporine'),(54,'Cyproheptadine'),(55,'Cytarabine'),(56,'Dacarbazine'),(57,'Dactinomycin'),(58,'Dapsone'),(59,'Darunavir'),(60,'Dasatinib'),(61,'Daunorubicin'),(62,'Deferasirox'),(63,'Desmopressin'),(64,'Dexamethasone'),(65,'Diclofenac'),(66,'Didanosine'),(67,'Dinutuximab'),(68,'Dobutamine'),(69,'Dopamine'),(70,'Dornase alfa'),(71,'Doxorubicin'),(72,'Dronabinol'),(73,'Efavirenz'),(74,'Efavirenz / emtricitabine / tenofovir'),(75,'Eltrombopag'),(76,'Elvitegravir / cobicistat / emtricitabine / tenofovir'),(77,'Elvitegravir / cobicistat / emtricitabine / tenofovir alafenamide'),(78,'Emicizumab'),(79,'Emtricitabine (Emtriva®)'),(80,'Emtricitabine / rilpivirine / tenofovir alafenamide'),(81,'Emtricitabine / tenofovir'),(82,'Emtricitabine / tenofovir alafenamide'),(83,'Enalapril'),(84,'Enoxaparin'),(85,'Erlotinib'),(86,'Erythromycin'),(87,'Erythropoietin'),(88,'Etonogestrel (Nexplanon®)'),(89,'Etoposide'),(90,'Etravirine (Intelence®)'),(91,'Factor IX complex'),(92,'Factor IX concentrate'),(93,'Factor VIIa (Recombinant)'),(94,'Factor VIII (Human) and von Willebrand Factor'),(95,'Factor VIII (Recombinant)'),(96,'Famciclovir'),(97,'Fluconazole'),(98,'Fludarabine'),(99,'Fluorouracil'),(100,'Foscarnet'),(101,'Furosemide'),(102,'G-CSF (Filgrastim)'),(103,'Gabapentin'),(104,'Ganciclovir'),(105,'Gefitinib'),(106,'Gemcitabine'),(107,'Gemtuzumab ozogamicin'),(108,'GM-CSF (Sargramostim)'),(109,'Granisetron'),(110,'Heparin Lock Flush for children and young adults'),(111,'Heparin Lock Flush for infants'),(112,'Hydralazine'),(113,'Hydrocodone with acetaminophen'),(114,'Hydrocortisone'),(115,'Hydromorphone'),(116,'Hydroxyurea'),(117,'Hydroxyurea for sickle cell disease'),(118,'Ifosfamide'),(119,'Imatinib'),(120,'Imipenem / cilastatin'),(121,'Immune globulin'),(122,'Interferon alfa-2a and alfa-2b'),(123,'Interferon alfa-2b for melanoma'),(124,'Interleukin-2 (Aldesleukin)'),(125,'Irinotecan'),(126,'Isotretinoin'),(127,'Itraconazole'),(128,'Ketoconazole'),(129,'L-glutamine'),(130,'Labetalol'),(131,'Lamivudine'),(132,'Leucovorin with high dose methotrexate (HDMTX)'),(133,'Levothyroxine'),(134,'Linezolid'),(135,'Lomustine'),(136,'Lopinavir / Ritonavir'),(137,'Lorazepam'),(138,'Magnesium'),(139,'Maraviroc'),(140,'Mechlorethamine'),(141,'Megestrol acetate'),(142,'Meloxicam'),(143,'Melphalan'),(144,'Meperidine'),(145,'Mercaptopurine'),(146,'Meropenem'),(147,'Mesna'),(148,'Methadone'),(149,'Methotrexate'),(150,'Methylphenidate'),(151,'Metronidazole'),(152,'Micafungin'),(153,'Mitotane'),(154,'Mitoxantrone'),(155,'Modafinil'),(156,'Morphine'),(157,'Muromonab – CD3'),(158,'Mycophenolate mofetil'),(159,'Nelarabine'),(160,'Nelfinavir'),(161,'Neuromuscular blockers'),(162,'Nevirapine'),(163,'Norepinephrine'),(164,'Omeprazole'),(165,'Ondansetron'),(166,'Oxycodone'),(167,'Paclitaxel'),(168,'PEGaspargase'),(169,'Pegfilgrastim'),(170,'Pemetrexed'),(171,'Penicillin VK'),(172,'Pentamidine'),(173,'Phenobarbital'),(174,'Phenytoin'),(175,'Phosphorus'),(176,'Posaconazole'),(177,'Potassium'),(178,'Prednisone'),(179,'Probenecid'),(180,'Procarbazine'),(181,'Promethazine'),(182,'Propoxyphene'),(183,'Ranitidine'),(184,'Rasburicase'),(185,'Ritonavir'),(186,'Rituximab'),(187,'Rivaroxaban'),(188,'Ruxolitinib'),(189,'Saquinavir'),(190,'Sirolimus'),(191,'Sorafenib'),(192,'Stavudine'),(193,'Sucralfate'),(194,'Sugammadex'),(195,'Sunitinib'),(196,'Tacrolimus'),(197,'Temozolomide'),(198,'Teniposide'),(199,'Tenofovir'),(200,'Thioguanine'),(201,'Thiotepa'),(202,'Tobramycin'),(203,'Topotecan'),(204,'Tretinoin – applied to the skin'),(205,'Tretinoin – by mouth'),(206,'Trimethoprim / sulfamethoxazole'),(207,'Valproic acid'),(208,'Vancomycin'),(209,'Vinblastine'),(210,'Vincristine'),(211,'Voriconazole'),(212,'Vorinostat'),(213,'Warfarin'),(214,'Zidovudine');
/*!40000 ALTER TABLE `drug` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `Employee_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Employee_NID` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `Employee_Name` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `Employee_Gender` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `Employee_DoB` date DEFAULT NULL,
  `Dept_ID` int(11) DEFAULT NULL,
  `Join_Date` date DEFAULT NULL,
  `Salarly` int(11) DEFAULT NULL,
  `Job_Type` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`Employee_ID`),
  UNIQUE KEY `Employee_NID_UNIQUE` (`Employee_NID`),
  KEY `Employee_Department_idx` (`Dept_ID`),
  CONSTRAINT `Employee_Department` FOREIGN KEY (`Dept_ID`) REFERENCES `department` (`Dept_ID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=310 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (101,'1111111111111','Damrat Treesukosol','Male','1965-06-06',6,NULL,NULL,'Doctor'),(102,'1111111111112','Darika Songwut','Female','1976-05-04',4,NULL,NULL,'Doctor'),(103,'1111111111113','Chakmedech Sethanan','Male',NULL,5,NULL,NULL,'Doctor'),(104,'1111111111114','Jiraporn Sriprapaporn','Male',NULL,2,NULL,NULL,'Doctor'),(105,'1111111111115','Chayaporn Chotiyanwong','Female',NULL,3,NULL,NULL,'Doctor'),(106,'1111111111116','Cholawate Shavasiri','Female',NULL,1,NULL,NULL,'Doctor'),(107,'1111111111117','Chaiyawat Sripirom','Female',NULL,7,NULL,NULL,'Doctor'),(201,'2222222222221','Nurse 1','Female',NULL,7,NULL,NULL,'Nurse'),(202,'2222222222222','Nurse 2','Female',NULL,3,NULL,NULL,'Nurse'),(203,'2222222222223','Nurse 3','Female',NULL,2,NULL,NULL,'Nurse'),(204,'2222222222224','Nurse 4','Female',NULL,7,NULL,NULL,'Nurse'),(301,'3333333333331','Employee 1','Female',NULL,2,NULL,NULL,'Other'),(302,'3333333333332','Employee 2','Female',NULL,7,NULL,NULL,'Other'),(303,'3333333333333','Employee 3','Male',NULL,7,NULL,NULL,'Other'),(305,'3333333333335','Employee 5','Male',NULL,7,NULL,NULL,'Other'),(306,'3333333333336','Employee 6','Male',NULL,2,NULL,NULL,'Other'),(309,'3333333333339','Employee 9','Female',NULL,2,NULL,NULL,'Other');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee_phone`
--

DROP TABLE IF EXISTS `employee_phone`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee_phone` (
  `Employee_ID` int(11) NOT NULL,
  `Phone` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`Employee_ID`,`Phone`),
  CONSTRAINT `Employee_Phone_Employee` FOREIGN KEY (`Employee_ID`) REFERENCES `employee` (`Employee_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_phone`
--

LOCK TABLES `employee_phone` WRITE;
/*!40000 ALTER TABLE `employee_phone` DISABLE KEYS */;
/*!40000 ALTER TABLE `employee_phone` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inpatient`
--

DROP TABLE IF EXISTS `inpatient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inpatient` (
  `Treatment_ID` int(11) NOT NULL,
  `Inpatient_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Attention_Level` int(11) NOT NULL,
  `Discharged_Date` date DEFAULT NULL,
  `Room` int(11) NOT NULL,
  `Bed` int(11) NOT NULL,
  PRIMARY KEY (`Treatment_ID`),
  UNIQUE KEY `Inpatient_ID_UNIQUE` (`Inpatient_ID`),
  KEY `Inpatient_Bed_idx` (`Room`,`Bed`),
  CONSTRAINT `Inpatient_Bed` FOREIGN KEY (`Room`, `Bed`) REFERENCES `bed` (`Room_ID`, `Bed_ID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `Inpatient_Treatment` FOREIGN KEY (`Treatment_ID`) REFERENCES `treatment` (`Treatment_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inpatient`
--

LOCK TABLES `inpatient` WRITE;
/*!40000 ALTER TABLE `inpatient` DISABLE KEYS */;
/*!40000 ALTER TABLE `inpatient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inpatient_assigned_nurse`
--

DROP TABLE IF EXISTS `inpatient_assigned_nurse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inpatient_assigned_nurse` (
  `Treatment_ID` int(11) NOT NULL,
  `Employee_ID` int(11) NOT NULL,
  PRIMARY KEY (`Treatment_ID`,`Employee_ID`),
  KEY `Inpatient_Assigned_Nurse_idx` (`Employee_ID`),
  CONSTRAINT `Inpatient_Assigned_Nurse_Inpatient` FOREIGN KEY (`Treatment_ID`) REFERENCES `inpatient` (`Treatment_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Inpatient_Assigned_Nurse_Nurse` FOREIGN KEY (`Employee_ID`) REFERENCES `nurse` (`Employee_ID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inpatient_assigned_nurse`
--

LOCK TABLES `inpatient_assigned_nurse` WRITE;
/*!40000 ALTER TABLE `inpatient_assigned_nurse` DISABLE KEYS */;
/*!40000 ALTER TABLE `inpatient_assigned_nurse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nurse`
--

DROP TABLE IF EXISTS `nurse`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `nurse` (
  `Employee_ID` int(11) NOT NULL,
  PRIMARY KEY (`Employee_ID`),
  CONSTRAINT `Nurse_Employee` FOREIGN KEY (`Employee_ID`) REFERENCES `employee` (`Employee_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nurse`
--

LOCK TABLES `nurse` WRITE;
/*!40000 ALTER TABLE `nurse` DISABLE KEYS */;
INSERT INTO `nurse` VALUES (201),(202),(203),(204);
/*!40000 ALTER TABLE `nurse` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `observational_stay_at`
--

DROP TABLE IF EXISTS `observational_stay_at`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `observational_stay_at` (
  `Patient_ID` int(11) NOT NULL,
  `Room_ID` int(11) NOT NULL,
  `Bed_ID` int(11) NOT NULL,
  PRIMARY KEY (`Patient_ID`,`Room_ID`,`Bed_ID`),
  KEY `Observational_Stay_At_Bed_idx` (`Room_ID`,`Bed_ID`),
  CONSTRAINT `Observational_Stay_At_Bed` FOREIGN KEY (`Room_ID`, `Bed_ID`) REFERENCES `bed` (`Room_ID`, `Bed_ID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `Observational_Stay_At_Outpatient` FOREIGN KEY (`Patient_ID`) REFERENCES `outpatient` (`Treatment_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `observational_stay_at`
--

LOCK TABLES `observational_stay_at` WRITE;
/*!40000 ALTER TABLE `observational_stay_at` DISABLE KEYS */;
/*!40000 ALTER TABLE `observational_stay_at` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `outpatient`
--

DROP TABLE IF EXISTS `outpatient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `outpatient` (
  `Treatment_ID` int(11) NOT NULL,
  PRIMARY KEY (`Treatment_ID`),
  CONSTRAINT `Outpatient_Treatment` FOREIGN KEY (`Treatment_ID`) REFERENCES `treatment` (`Treatment_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `outpatient`
--

LOCK TABLES `outpatient` WRITE;
/*!40000 ALTER TABLE `outpatient` DISABLE KEYS */;
/*!40000 ALTER TABLE `outpatient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient`
--

DROP TABLE IF EXISTS `patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient` (
  `Patient_ID` int(11) NOT NULL,
  `Patient_NID` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `Patient_Name` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `Patient_Gender` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `Patient_DoB` date DEFAULT NULL,
  `Blood_Group` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `Status` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`Patient_ID`),
  KEY `Patient_DoB_idx` (`Patient_DoB`) USING BTREE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient`
--

LOCK TABLES `patient` WRITE;
/*!40000 ALTER TABLE `patient` DISABLE KEYS */;
INSERT INTO `patient` VALUES (1,'0000000000001','Patient 1','Male','2000-01-01','A','Discharged'),(2,'0000000000002','Patient 2','Female','2000-02-02','B','Discharged'),(3,'0000000000003','Patient 3','Male','2000-03-03','O','Discharged'),(4,'0000000000004','Patient 4','Female','2000-04-04','AB','Discharged'),(5,'0000000000005','Patient 5','Male','2000-05-05','A','Discharged'),(6,'0000000000006','Patient 6','Female','2000-06-06','B','Discharged'),(7,'0000000000007','Patient 7','Male','2000-07-07','O','Discharged'),(8,'0000000000008','Patient 8','Female','2000-08-08','AB','Discharged'),(9,'0000000000009','Patient 9','Male','2000-09-09','A','Discharged'),(10,'0000000000010','Patient 10','Female','2000-10-10','B','Discharged'),(51,'9888877777665','Illish Catus','Female','0001-01-01','A','Deceased'),(52,'8777766666554','Illish Catmeow','Female','9999-12-31','AB','Discharged'),(53,'7666655555443','Intrachit Bidbuengayin','Male','1996-06-16','O','Discharged'),(54,'6555544444332','Muenong Amarin','Male','1995-05-15','B','Discharged'),(55,'5444433333221','Raghu Ramakrishnan','Male','1961-01-01','A','Discharged'),(56,'4333322222110','Prafuen Tuennon','Male','1963-02-28','A','Discharged'),(57,'3222211111009','Klaiphra Nakorn','Female','1968-03-31','B','Discharged'),(58,'2111100000998','Satorn Thornthai','Female','1973-04-26','O','Discharged'),(59,'1000099999887','Shaotu Suriyon','Male','1978-05-21','AB','Discharged'),(60,'0999988888776','Kuenphon Marukrai','Male','1983-06-16','B','Discharged'),(62,'3210987654321','Meekrum Jumpai','Male','1988-05-11','O','Discharged'),(99,'2109876543210','Naipa Ar-run','Female','1993-07-06','A','Discharged'),(255,'3155852073011','Sunthorn Phu','Male','1998-08-01','AB','Deceased');
/*!40000 ALTER TABLE `patient` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient_allergic`
--

DROP TABLE IF EXISTS `patient_allergic`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient_allergic` (
  `Patient_ID` int(11) NOT NULL,
  `Allergic` varchar(180) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`Patient_ID`,`Allergic`),
  CONSTRAINT `Patient_Allergic_Patient` FOREIGN KEY (`Patient_ID`) REFERENCES `patient` (`Patient_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient_allergic`
--

LOCK TABLES `patient_allergic` WRITE;
/*!40000 ALTER TABLE `patient_allergic` DISABLE KEYS */;
/*!40000 ALTER TABLE `patient_allergic` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient_med_history`
--

DROP TABLE IF EXISTS `patient_med_history`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient_med_history` (
  `Patient_ID` int(11) NOT NULL,
  `Med_History` varchar(180) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`Patient_ID`,`Med_History`),
  CONSTRAINT `Patient_Med_History_Patient` FOREIGN KEY (`Patient_ID`) REFERENCES `patient` (`Patient_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient_med_history`
--

LOCK TABLES `patient_med_history` WRITE;
/*!40000 ALTER TABLE `patient_med_history` DISABLE KEYS */;
/*!40000 ALTER TABLE `patient_med_history` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `patient_phone`
--

DROP TABLE IF EXISTS `patient_phone`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient_phone` (
  `Patient_ID` int(11) NOT NULL,
  `Patient_Phone` varchar(45) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`Patient_ID`,`Patient_Phone`),
  KEY `Patient_Phone_idx` (`Patient_Phone`) USING BTREE,
  CONSTRAINT `Patient_Phone_Patient` FOREIGN KEY (`Patient_ID`) REFERENCES `patient` (`Patient_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient_phone`
--

LOCK TABLES `patient_phone` WRITE;
/*!40000 ALTER TABLE `patient_phone` DISABLE KEYS */;
/*!40000 ALTER TABLE `patient_phone` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `required_service`
--

DROP TABLE IF EXISTS `required_service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `required_service` (
  `Treatment_ID` int(11) NOT NULL,
  `Service_ID` int(11) NOT NULL,
  PRIMARY KEY (`Treatment_ID`,`Service_ID`),
  KEY `Required_Service_Service_idx` (`Service_ID`),
  CONSTRAINT `Required_Service_Service` FOREIGN KEY (`Service_ID`) REFERENCES `service` (`Service_ID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `Required_Service_Treatment` FOREIGN KEY (`Treatment_ID`) REFERENCES `treatment` (`Treatment_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `required_service`
--

LOCK TABLES `required_service` WRITE;
/*!40000 ALTER TABLE `required_service` DISABLE KEYS */;
/*!40000 ALTER TABLE `required_service` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `room`
--

DROP TABLE IF EXISTS `room`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `room` (
  `Room_ID` int(11) NOT NULL,
  PRIMARY KEY (`Room_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `room`
--

LOCK TABLES `room` WRITE;
/*!40000 ALTER TABLE `room` DISABLE KEYS */;
INSERT INTO `room` VALUES (4001),(4002),(4003),(4004),(4005),(5001),(5002),(5003),(5004),(5005);
/*!40000 ALTER TABLE `room` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schedule`
--

DROP TABLE IF EXISTS `schedule`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `schedule` (
  `Employee_ID` int(11) NOT NULL,
  `Work_Date` date NOT NULL,
  `Start_Time` time NOT NULL,
  `End_Time` time DEFAULT NULL,
  PRIMARY KEY (`Employee_ID`,`Work_Date`,`Start_Time`),
  CONSTRAINT `Schedule_Employee` FOREIGN KEY (`Employee_ID`) REFERENCES `employee` (`Employee_ID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schedule`
--

LOCK TABLES `schedule` WRITE;
/*!40000 ALTER TABLE `schedule` DISABLE KEYS */;
INSERT INTO `schedule` VALUES (101,'2019-11-24','08:00:00','16:00:00'),(101,'2019-11-25','08:00:00','16:00:00'),(101,'2019-11-26','08:00:00','16:00:00'),(101,'2019-11-27','08:00:00','16:00:00'),(101,'2019-11-28','08:00:00','16:00:00'),(101,'2019-11-29','08:00:00','16:00:00'),(101,'2019-11-30','08:00:00','16:00:00'),(102,'2019-11-24','08:00:00','16:00:00'),(102,'2019-11-25','08:00:00','16:00:00'),(102,'2019-11-26','08:00:00','16:00:00'),(102,'2019-11-27','08:00:00','16:00:00'),(102,'2019-11-28','08:00:00','16:00:00'),(102,'2019-11-29','08:00:00','16:00:00'),(102,'2019-11-30','08:00:00','16:00:00'),(103,'2019-11-24','08:00:00','16:00:00'),(103,'2019-11-25','08:00:00','16:00:00'),(103,'2019-11-26','08:00:00','16:00:00'),(103,'2019-11-27','08:00:00','16:00:00'),(103,'2019-11-28','08:00:00','16:00:00'),(103,'2019-11-29','08:00:00','16:00:00'),(103,'2019-11-30','08:00:00','16:00:00'),(104,'2019-11-24','08:00:00','16:00:00'),(104,'2019-11-25','08:00:00','16:00:00'),(104,'2019-11-26','08:00:00','16:00:00'),(104,'2019-11-27','08:00:00','16:00:00'),(104,'2019-11-28','08:00:00','16:00:00'),(104,'2019-11-29','08:00:00','16:00:00'),(104,'2019-11-30','08:00:00','16:00:00'),(105,'2019-11-24','08:00:00','16:00:00'),(105,'2019-11-25','08:00:00','16:00:00'),(105,'2019-11-26','08:00:00','16:00:00'),(105,'2019-11-27','08:00:00','16:00:00'),(105,'2019-11-28','08:00:00','16:00:00'),(105,'2019-11-29','08:00:00','16:00:00'),(105,'2019-11-30','08:00:00','16:00:00'),(106,'2019-11-24','08:00:00','16:00:00'),(106,'2019-11-25','08:00:00','16:00:00'),(106,'2019-11-26','08:00:00','16:00:00'),(106,'2019-11-27','08:00:00','16:00:00'),(106,'2019-11-28','08:00:00','16:00:00'),(106,'2019-11-29','08:00:00','16:00:00'),(106,'2019-11-30','08:00:00','16:00:00'),(107,'2019-11-24','08:00:00','16:00:00'),(107,'2019-11-25','08:00:00','16:00:00'),(107,'2019-11-26','08:00:00','16:00:00'),(107,'2019-11-27','08:00:00','16:00:00'),(107,'2019-11-28','08:00:00','16:00:00'),(107,'2019-11-29','08:00:00','16:00:00'),(107,'2019-11-30','08:00:00','16:00:00'),(201,'2019-11-24','08:00:00','16:00:00'),(201,'2019-11-25','08:00:00','16:00:00'),(201,'2019-11-26','08:00:00','16:00:00'),(201,'2019-11-27','08:00:00','16:00:00'),(201,'2019-11-28','08:00:00','16:00:00'),(201,'2019-11-29','08:00:00','16:00:00'),(201,'2019-11-30','08:00:00','16:00:00'),(202,'2019-11-24','08:00:00','16:00:00'),(202,'2019-11-25','08:00:00','16:00:00'),(202,'2019-11-26','08:00:00','16:00:00'),(202,'2019-11-27','08:00:00','16:00:00'),(202,'2019-11-28','08:00:00','16:00:00'),(202,'2019-11-29','08:00:00','16:00:00'),(202,'2019-11-30','08:00:00','16:00:00'),(203,'2019-11-24','08:00:00','16:00:00'),(203,'2019-11-25','08:00:00','16:00:00'),(203,'2019-11-26','08:00:00','16:00:00'),(203,'2019-11-27','08:00:00','16:00:00'),(203,'2019-11-28','08:00:00','16:00:00'),(203,'2019-11-29','08:00:00','16:00:00'),(203,'2019-11-30','08:00:00','16:00:00'),(204,'2019-11-24','08:00:00','16:00:00'),(204,'2019-11-25','08:00:00','16:00:00'),(204,'2019-11-26','08:00:00','16:00:00'),(204,'2019-11-27','08:00:00','16:00:00'),(204,'2019-11-28','08:00:00','16:00:00'),(204,'2019-11-29','08:00:00','16:00:00'),(204,'2019-11-30','08:00:00','16:00:00'),(301,'2019-11-24','08:00:00','16:00:00'),(301,'2019-11-25','08:00:00','16:00:00'),(301,'2019-11-26','08:00:00','16:00:00'),(301,'2019-11-27','08:00:00','16:00:00'),(301,'2019-11-28','08:00:00','16:00:00'),(301,'2019-11-29','08:00:00','16:00:00'),(301,'2019-11-30','08:00:00','16:00:00'),(302,'2019-11-24','08:00:00','16:00:00'),(302,'2019-11-25','08:00:00','16:00:00'),(302,'2019-11-26','08:00:00','16:00:00'),(302,'2019-11-27','08:00:00','16:00:00'),(302,'2019-11-28','08:00:00','16:00:00'),(302,'2019-11-29','08:00:00','16:00:00'),(302,'2019-11-30','08:00:00','16:00:00'),(303,'2019-11-24','08:00:00','16:00:00'),(303,'2019-11-25','08:00:00','16:00:00'),(303,'2019-11-26','08:00:00','16:00:00'),(303,'2019-11-27','08:00:00','16:00:00'),(303,'2019-11-28','08:00:00','16:00:00'),(303,'2019-11-29','08:00:00','16:00:00'),(303,'2019-11-30','08:00:00','16:00:00'),(305,'2019-11-24','08:00:00','16:00:00'),(305,'2019-11-25','08:00:00','16:00:00'),(305,'2019-11-26','08:00:00','16:00:00'),(305,'2019-11-27','08:00:00','16:00:00'),(305,'2019-11-28','08:00:00','16:00:00'),(305,'2019-11-29','08:00:00','16:00:00'),(305,'2019-11-30','08:00:00','16:00:00'),(306,'2019-11-24','08:00:00','16:00:00'),(306,'2019-11-25','08:00:00','16:00:00'),(306,'2019-11-26','08:00:00','16:00:00'),(306,'2019-11-27','08:00:00','16:00:00'),(306,'2019-11-28','08:00:00','16:00:00'),(306,'2019-11-29','08:00:00','16:00:00'),(306,'2019-11-30','08:00:00','16:00:00'),(309,'2019-11-24','08:00:00','16:00:00'),(309,'2019-11-25','08:00:00','16:00:00'),(309,'2019-11-26','08:00:00','16:00:00'),(309,'2019-11-27','08:00:00','16:00:00'),(309,'2019-11-28','08:00:00','16:00:00'),(309,'2019-11-29','08:00:00','16:00:00'),(309,'2019-11-30','08:00:00','16:00:00');
/*!40000 ALTER TABLE `schedule` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `service`
--

DROP TABLE IF EXISTS `service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `service` (
  `Service_ID` int(11) NOT NULL,
  `Service_Name` varchar(180) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `Service_Type` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Dept_ID` int(11) NOT NULL,
  PRIMARY KEY (`Service_ID`),
  KEY `Service_Department_idx` (`Dept_ID`),
  CONSTRAINT `Service_Department` FOREIGN KEY (`Dept_ID`) REFERENCES `department` (`Dept_ID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `service`
--

LOCK TABLES `service` WRITE;
/*!40000 ALTER TABLE `service` DISABLE KEYS */;
INSERT INTO `service` VALUES (101,'Atrial septal defect','Diagnostic',1),(102,'Ventricular septal defect','Diagnostic',1),(103,'Patent ductus arteriosus','Diagnostic',1),(104,'Transposition of the great arteries','Surgical',1),(105,'Hypoplastic left heart syndrome and tetralogy of Fallot','Medical care',1),(201,'Emergency medical','Medical care',2),(301,'Intensive care','Medical care',3),(401,'Electroencephalography','Diagnostic',4),(402,'Electromyography','Diagnostic',4),(403,'Neuroradiology','Diagnostic',4),(404,'Neuromascular respiratory','Medical care',4),(501,'Diagnostic testing','Diagnostic',5),(502,'Surgical oncology services','Surgical',5),(503,'Biopsies / Clinical Pathology','Medical care',5),(504,'Laboratory testing services','Diagnostic',5),(505,'Limited chemotherapy services','Medical care',5),(506,'IV blood transfusion / platelets','Blood',5),(507,'Lymphedema management therapy','Medical care',5),(601,'Birth control management','Medical care',6),(602,'Hormone treatment','Medical care',6),(603,'Osteoporosis screening','Diagnostic',6),(604,'Pellet therapy','Medical care',6),(605,'Pelvic pain','Medical care',6),(606,'Abnormal menstrual bleeding','Medical care',6),(607,'Menopause management','Medical care',6);
/*!40000 ALTER TABLE `service` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `treatment`
--

DROP TABLE IF EXISTS `treatment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `treatment` (
  `Treatment_ID` int(11) NOT NULL AUTO_INCREMENT,
  `Arrival_Date` date DEFAULT NULL,
  `Emergency_Level` varchar(45) COLLATE utf8_unicode_ci DEFAULT NULL,
  `Patient_ID` int(11) NOT NULL,
  `Patient_Type` int(11) NOT NULL,
  PRIMARY KEY (`Treatment_ID`),
  KEY `Treatment_Patient_idx` (`Patient_ID`),
  KEY `Arrival_Date_idx` (`Arrival_Date`) USING BTREE,
  CONSTRAINT `Treatment_Patient` FOREIGN KEY (`Patient_ID`) REFERENCES `patient` (`Patient_ID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `treatment`
--

LOCK TABLES `treatment` WRITE;
/*!40000 ALTER TABLE `treatment` DISABLE KEYS */;
/*!40000 ALTER TABLE `treatment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `treatment_assigned_doctor`
--

DROP TABLE IF EXISTS `treatment_assigned_doctor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `treatment_assigned_doctor` (
  `Treatment_ID` int(11) NOT NULL,
  `Employee_ID` int(11) NOT NULL,
  PRIMARY KEY (`Treatment_ID`,`Employee_ID`),
  KEY `Treatment_Assigned_Doctor_Doctor_idx` (`Employee_ID`),
  CONSTRAINT `Treatment_Assigned_Doctor_Doctor` FOREIGN KEY (`Employee_ID`) REFERENCES `doctor` (`Employee_ID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `Treatment_Assigned_Doctor_Treatment` FOREIGN KEY (`Treatment_ID`) REFERENCES `treatment` (`Treatment_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `treatment_assigned_doctor`
--

LOCK TABLES `treatment_assigned_doctor` WRITE;
/*!40000 ALTER TABLE `treatment_assigned_doctor` DISABLE KEYS */;
/*!40000 ALTER TABLE `treatment_assigned_doctor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `treatment_symptom`
--

DROP TABLE IF EXISTS `treatment_symptom`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `treatment_symptom` (
  `Treatment_ID` int(11) NOT NULL,
  `Symptom` varchar(180) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`Treatment_ID`,`Symptom`),
  CONSTRAINT `Treatment_Symptom_Treatment` FOREIGN KEY (`Treatment_ID`) REFERENCES `treatment` (`Treatment_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `treatment_symptom`
--

LOCK TABLES `treatment_symptom` WRITE;
/*!40000 ALTER TABLE `treatment_symptom` DISABLE KEYS */;
/*!40000 ALTER TABLE `treatment_symptom` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `used_drug`
--

DROP TABLE IF EXISTS `used_drug`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `used_drug` (
  `Treatment_ID` int(11) NOT NULL,
  `Drug_ID` int(11) NOT NULL,
  PRIMARY KEY (`Treatment_ID`,`Drug_ID`),
  KEY `Used_Drug_Drug_idx` (`Drug_ID`),
  CONSTRAINT `Used_Drug_Drug` FOREIGN KEY (`Drug_ID`) REFERENCES `drug` (`Drug_ID`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `Used_Durg_Treatment` FOREIGN KEY (`Treatment_ID`) REFERENCES `treatment` (`Treatment_ID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `used_drug`
--

LOCK TABLES `used_drug` WRITE;
/*!40000 ALTER TABLE `used_drug` DISABLE KEYS */;
/*!40000 ALTER TABLE `used_drug` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `with_respect_to`
--

DROP TABLE IF EXISTS `with_respect_to`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `with_respect_to` (
  `Appointment_ID` int(11) NOT NULL,
  `Employee_ID` int(11) NOT NULL,
  `Work_Date` date NOT NULL,
  `Start_Time` time NOT NULL,
  PRIMARY KEY (`Appointment_ID`,`Employee_ID`,`Work_Date`,`Start_Time`),
  KEY `With_Respect_To_Schedule_idx` (`Employee_ID`,`Work_Date`,`Start_Time`),
  CONSTRAINT `With_Respect_To_Appointment` FOREIGN KEY (`Appointment_ID`) REFERENCES `appointment` (`Appointment_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `With_Respect_To_Schedule` FOREIGN KEY (`Employee_ID`, `Work_Date`, `Start_Time`) REFERENCES `schedule` (`Employee_ID`, `Work_Date`, `Start_Time`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `with_respect_to`
--

LOCK TABLES `with_respect_to` WRITE;
/*!40000 ALTER TABLE `with_respect_to` DISABLE KEYS */;
/*!40000 ALTER TABLE `with_respect_to` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `works_on`
--

DROP TABLE IF EXISTS `works_on`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `works_on` (
  `Employee_ID` int(11) NOT NULL,
  `Service_ID` int(11) NOT NULL,
  PRIMARY KEY (`Employee_ID`,`Service_ID`),
  KEY `Works_On_Employee_idx` (`Employee_ID`),
  KEY `Works_On_Service_idx` (`Service_ID`),
  CONSTRAINT `Works_On_Employee` FOREIGN KEY (`Employee_ID`) REFERENCES `employee` (`Employee_ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `Works_On_Service` FOREIGN KEY (`Service_ID`) REFERENCES `service` (`Service_ID`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `works_on`
--

LOCK TABLES `works_on` WRITE;
/*!40000 ALTER TABLE `works_on` DISABLE KEYS */;
INSERT INTO `works_on` VALUES (101,601),(102,403),(103,501),(202,301),(203,201);
/*!40000 ALTER TABLE `works_on` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'hospital'
--

--
-- Dumping routines for database 'hospital'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-11-25  0:52:54
