-- MySQL dump 10.13  Distrib 8.0.35, for Linux (x86_64)
--
-- Host: localhost    Database: HotelMiranda
-- ------------------------------------------------------
-- Server version	8.0.35-0ubuntu0.22.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `amenities`
--

DROP TABLE IF EXISTS `amenities`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `amenities` (
  `id` int NOT NULL AUTO_INCREMENT,
  `amenity` varchar(255) NOT NULL,
  `room_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `room_id` (`room_id`),
  CONSTRAINT `amenities_ibfk_1` FOREIGN KEY (`room_id`) REFERENCES `rooms` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=90 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amenities`
--

LOCK TABLES `amenities` WRITE;
/*!40000 ALTER TABLE `amenities` DISABLE KEYS */;
INSERT INTO `amenities` VALUES (2,'urbanus',5),(3,'tui',5),(4,'fugit',5),(5,'carcer',5),(6,'curiositas',5),(7,'strenuus',6),(8,'uredo',6),(9,'votum',6),(10,'bene',6),(11,'antea',6),(12,'usque',7),(13,'acerbitas',7),(14,'deprimo',7),(15,'aeternus',7),(16,'laudantium',7),(17,'cetera',8),(18,'accedo',8),(19,'comedo',8),(20,'architecto',8),(21,'fugit',8),(22,'maiores',9),(23,'creator',9),(24,'vestrum',9),(25,'vilis',9),(26,'censura',9),(27,'adeo',10),(28,'charisma',10),(29,'careo',10),(30,'peior',10),(31,'doloribus',10),(32,'claudeo',11),(33,'thesis',11),(34,'sub',11),(35,'ait',11),(36,'comis',11),(37,'doloribus',12),(38,'tergo',12),(39,'hic',12),(40,'textor',12),(41,'sperno',12),(42,'tam',13),(43,'spoliatio',13),(44,'omnis',13),(45,'suadeo',13),(46,'vobis',13),(47,'illum',14),(48,'addo',14),(49,'ascisco',14),(50,'alo',14),(51,'denuncio',14),(52,'cohors',15),(53,'venia',15),(54,'ciminatio',15),(55,'viduo',15),(56,'suppellex',15),(57,'ambulo',16),(58,'terminatio',16),(59,'corrumpo',16),(60,'civis',16),(61,'corpus',16),(62,'aiunt',17),(63,'utpote',17),(64,'aranea',17),(65,'adflicto',17),(66,'repellat',17),(67,'velociter',18),(68,'succurro',18),(69,'tonsor',18),(70,'defendo',18),(71,'quam',18),(72,'acsi',19),(73,'somniculosus',19),(74,'maiores',19),(75,'virga',19),(76,'texo',19),(85,'Wifi',53),(86,'TV',53),(88,'Wifi',52),(89,'TV',52);
/*!40000 ALTER TABLE `amenities` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `bookings`
--

DROP TABLE IF EXISTS `bookings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bookings` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `orderDate` date NOT NULL,
  `check_in` date NOT NULL,
  `hour_in` time NOT NULL,
  `check_out` date NOT NULL,
  `hour_out` time NOT NULL,
  `room_id` int NOT NULL,
  `specialRequest` longtext,
  `status` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `room_id` (`room_id`),
  CONSTRAINT `bookings_ibfk_1` FOREIGN KEY (`room_id`) REFERENCES `rooms` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `bookings`
--

LOCK TABLES `bookings` WRITE;
/*!40000 ALTER TABLE `bookings` DISABLE KEYS */;
INSERT INTO `bookings` VALUES (1,'Manuel Oquendo Gutiérrez','2024-01-11','2024-06-30','16:07:24','2024-07-24','04:27:15',16,'Sit spiculum odio tamdiu tollo. Allatus tamen coniecto theatrum cicuta cometes.','Check In'),(2,'Sra. María de los Ángeles Saucedo Viera','2023-12-03','2024-11-03','05:42:05','2024-11-04','09:30:16',15,'Utpote ascit dolor apostolus caveo architecto somniculosus corrumpo. Nulla maiores abstergo angustus spectaculum.','Check In'),(3,'Lorena Salinas Téllez','2023-08-17','2024-03-17','06:09:45','2024-03-24','03:45:21',7,'Patrocinor verbum quam valens cui reiciendis considero. Iure cena solio vinco depono cohaero cado necessitatibus adsum.','Check In'),(4,'Lorena Magaña Reséndez','2024-05-08','2024-08-09','14:43:47','2024-08-15','00:04:36',5,'Dolores denuo volubilis cauda barba vomer culpa tutis casus. Clam pel certus.','Check In'),(5,'Pedro Olivas Ríos','2024-06-25','2024-10-15','16:48:43','2024-11-11','18:48:56',19,'Absorbeo dignissimos paens crur crastinus a. Administratio volaticus doloremque demergo cuppedia bonus laudantium administratio.','Check In'),(6,'Sr. Iván Paredes Montero','2024-01-14','2024-08-07','17:09:23','2024-09-04','17:02:57',11,'Addo vinco omnis derideo odio bardus vesco eligendi tui. Chirographum substantia xiphias nulla infit alioqui suspendo tempora.','Check In'),(7,'Marta Delatorre Matos','2024-05-23','2024-08-01','03:09:05','2024-08-16','08:26:21',10,'Ater deficio eius utique via. Aqua angustus voro.','Check In'),(8,'Laura Bravo Castro','2023-12-27','2024-11-21','15:12:18','2024-12-19','14:52:17',13,'Vespillo vester causa quia. Caste benigne adeptio cras derideo nam claudeo delinquo.','Check In'),(9,'Juan Ramón Solorzano Collazo','2024-03-03','2024-05-24','13:36:34','2024-05-26','14:17:03',9,'Curto verto peior derelinquo statua culpo. Alius sapiente consequatur subiungo adsuesco ventosus villa.','Check In'),(10,'Sta. Matilde Treviño Trujillo','2023-04-30','2024-03-10','16:28:28','2024-03-24','03:30:16',18,'Ullus paulatim atque vinco. Defendo comburo comedo vomer veritatis cursim calamitas paulatim.','Check In'),(11,'Juan Ramón Ochoa Sanabria','2024-02-12','2024-03-12','07:01:26','2024-03-31','03:23:43',8,'Absorbeo molestias terebro fugit tamquam adeo. Averto stultus sublime cohaero adhaero suggero.','Check In'),(12,'Matilde Gallardo Terrazas','2024-12-14','2024-12-19','00:13:15','2024-12-19','12:43:27',17,'Vicissitudo beatae caveo aequitas demergo defessus. Cum commodi crepusculum atqui.','Check In'),(13,'Matilde Cortéz Quiróz','2023-12-18','2024-09-15','02:37:07','2024-09-24','21:05:21',12,'Voluptatum vilicus color. Decor cursus balbus aetas tamquam vae.','Check In'),(14,'Lorena','2023-07-01','2024-02-01','11:30:00','2024-02-12','22:11:21',6,'Arbitro a annus suasoria conqueror conturbo utrum corrigo depopulo debeo. Trucido aegre tristis suscipit sit thorax desidero.','In Progress'),(22,'diego','2024-01-31','2024-02-02','00:00:00','2024-02-07','00:00:00',8,'','Check In');
/*!40000 ALTER TABLE `bookings` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contacts`
--

DROP TABLE IF EXISTS `contacts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contacts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userImg` longtext NOT NULL,
  `name` varchar(100) NOT NULL,
  `surname` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `subject` varchar(100) NOT NULL,
  `message` longtext NOT NULL,
  `stars` int NOT NULL,
  `is_archived` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contacts`
--

LOCK TABLES `contacts` WRITE;
/*!40000 ALTER TABLE `contacts` DISABLE KEYS */;
INSERT INTO `contacts` VALUES (1,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/532.jpg','Tomás','Marroquín Garica','Tomas_MarroquinGarica@yahoo.com','950270182','2023-06-22','Delectus blanditiis tredecim versus tredecim.','Timor clamo amplitudo comes bellum stipes. Acervus deripio nesciunt creator alii harum est ciminatio earum tamquam.',3,0),(2,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/1196.jpg','Carolina','Soto Reyna','Carolina.SotoReyna@yahoo.com','902343031','2023-09-12','Incidunt complectus suppono sollers tertius.','Careo speculum depono tot tres veritas curvo. Administratio caput canto cinis spargo tertius.',2,0),(3,'https://avatars.githubusercontent.com/u/8125461','Carla','Espino Cabán','Carla.EspinoCaban72@yahoo.com','945111022','2023-10-28','Talus ut defero tolero vaco.','Tubineus blandior repudiandae celebrer tribuo. Utique amplexus adinventitias.',1,0),(4,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/847.jpg','Alberto','Elizondo Vázquez','Alberto23@hotmail.com','903689783','2023-08-12','Laborum verus confido advenio somniculosus.','Libero bestia acidus vespillo alius veritatis abstergo tubineus ipsam. Suadeo desidero corona comptus compono denuo degusto.',5,0),(5,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/745.jpg','Diana','Salcedo Rolón','Diana_SalcedoRolon93@hotmail.com','917129656','2023-09-15','Coerceo statim defendo celebrer vix.','Pariatur verbum ventus vigor audeo. Adnuo charisma corroboro.',3,0),(6,'https://avatars.githubusercontent.com/u/94379072','Gabriel','Trujillo Valdés','Gabriel45@yahoo.com','946813070','2023-11-16','Volva apud strues voluptatibus sint.','Spiculum accendo carbo umbra trucido desidero. Arguo eos trepide.',5,0),(7,'https://avatars.githubusercontent.com/u/3269618','María de los Ángeles','Crespo Gaitán','MariadelosAngeles90@hotmail.com','941613224','2023-08-18','Tricesimus vereor apparatus strues nobis.','Suscipit damno cultura. Censura deputo thymum toties suscipio vitium aperio thorax curatio.',5,0),(8,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/99.jpg','María de los Ángeles','Arredondo Armijo','MariadelosAngeles.ArredondoArmijo@yahoo.com','903577150','2023-03-08','Ex victoria subvenio curo nihil.','Placeat sperno aurum commemoro cursim strues subvenio. Coniuratio suffoco consuasor arbitro depopulo.',4,0),(9,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/535.jpg','Joaquín','Anguiano Vallejo','Joaquin4@hotmail.com','981145432','2023-12-21','Vicissitudo utrimque eos aliqua bonus.','Tergeo solutio strues tenuis defluo tabesco ducimus. Amiculum tempore deduco est cur suspendo dignissimos adfectus.',4,0),(10,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/14.jpg','Salvador','Uribe Ozuna','Salvador10@gmail.com','986178856','2023-10-05','Creator vinculum umquam crustulum vestigium.','Minima apparatus vomer provident surculus curriculum tui tristis. Cruentus ut voluptatum conventus.',4,0),(11,'https://avatars.githubusercontent.com/u/5401610','David','Patiño Perales','David_PatinoPerales@gmail.com','917206128','2023-04-26','Cupiditas vinco thermae circumvenio depono.','Adsuesco sed amplitudo labore tepesco desolo a accommodo. Arx neque esse quidem arbor crepusculum arto.',2,0),(12,'https://avatars.githubusercontent.com/u/23651089','Estela','Collazo Cervántez','Estela9@gmail.com','941563346','2023-02-15','Color spectaculum vilicus repellendus studio.','Arbitro nobis arcus abstergo sequi. Laboriosam attero tremo ocer villa supellex templum bene.',5,0),(13,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/521.jpg','Marcela','Negrete Argüello','Marcela_NegreteArguello49@gmail.com','966924284','2023-01-03','Compello vulticulus consequatur contra canto.','Culpo uter vivo. Fugiat tendo corona beneficium ademptio campana vorax utroque auxilium aggero.',4,0),(14,'https://avatars.githubusercontent.com/u/40477847','Juan Carlos','Villegas Candelaria','JuanCarlos_VillegasCandelaria66@gmail.com','923076914','2023-02-02','Adulatio sol cohibeo talio deficio.','Timor consuasor bestia. Capio cauda blanditiis infit tamquam sublime excepturi.',5,0),(15,'https://avatars.githubusercontent.com/u/37886885','Rebeca','Correa Delafuente','Rebeca.CorreaDelafuente@yahoo.com','923927846','2023-07-03','Pel artificiose contabesco vindico celebrer.','Utrimque pecus utrimque truculenter laudantium uterque viriliter. Solutio dolorum veritas cibo complectus creptio autem tenetur at.',2,0),(16,'d','d','d','d','d','2024-02-01','s','s',1,0);
/*!40000 ALTER TABLE `contacts` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rooms`
--

DROP TABLE IF EXISTS `rooms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `rooms` (
  `id` int NOT NULL AUTO_INCREMENT,
  `photos` json NOT NULL,
  `roomType` tinytext NOT NULL,
  `roomNumber` tinytext NOT NULL,
  `description` mediumtext NOT NULL,
  `offer` varchar(10) NOT NULL,
  `priceNight` float NOT NULL,
  `discount` int DEFAULT NULL,
  `cancellation` tinytext NOT NULL,
  `status` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=54 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rooms`
--

LOCK TABLES `rooms` WRITE;
/*!40000 ALTER TABLE `rooms` DISABLE KEYS */;
INSERT INTO `rooms` VALUES (5,'[\"https://loremflickr.com/640/480/hotel,bedroom?lock=8959555882975232\", \"https://loremflickr.com/640/480/hotel,bedroom?lock=5743649769914368\", \"https://loremflickr.com/640/480/hotel,bedroom?lock=8740501763129344\"]','Double Bed','delinquo-358','Utrum et contego. Tot aperiam nulla cattus.','NO',250,NULL,'Catena in adduco vero strenuus tergiversatio volubilis. Accendo minima suffoco approbo aestas eos patria pecco.','Available'),(6,'[\"https://loremflickr.com/640/480/hotel,bedroom?lock=5441948603121664\", \"https://loremflickr.com/640/480/hotel,bedroom?lock=5944478156193792\", \"https://loremflickr.com/640/480/hotel,bedroom?lock=1594460634873856\"]','Double Bed','earum-360','Tam ab minus. A vis spero volup.','YES',166,40,'Subiungo videlicet accedo. Sufficio deserunt aliquid arbitro denique antea taedium.','Available'),(7,'[\"https://loremflickr.com/640/480/hotel,bedroom?lock=8010559284838400\", \"https://loremflickr.com/640/480/hotel,bedroom?lock=1347507919519744\", \"https://loremflickr.com/640/480/hotel,bedroom?lock=8478472519286784\"]','Double Superior','agnosco-98','Abbas defessus dicta atrocitas damno cornu solum considero. Clementia defendo ceno voluptatibus.','NO',224,NULL,'Ipsam delectatio corrigo vir ab demum. Confugo acervus pecus.','Available'),(8,'[\"https://loremflickr.com/640/480/hotel,bedroom?lock=8578892354813952\", \"https://loremflickr.com/640/480/hotel,bedroom?lock=3605480530247680\", \"https://loremflickr.com/640/480/hotel,bedroom?lock=1850350663368704\"]','Double Bed','coniecto-61','Thema thymbra strenuus vomer cometes. Appositus peccatus harum nam ea consuasor depromo valde.','NO',90,NULL,'Tabernus cohaero curriculum comitatus aqua. Amissio vulgus aufero confero peccatus ultio ducimus rem deinde creta.','Available'),(9,'[\"https://loremflickr.com/640/480/hotel,bedroom?lock=3079600903028736\", \"https://loremflickr.com/640/480/hotel,bedroom?lock=1921456755703808\", \"https://loremflickr.com/640/480/hotel,bedroom?lock=6595211257970688\"]','Double Superior','repellendus-477','Comis asperiores curo. Suffragium aetas clibanus absconditus thesis fugiat studio supra cribro.','NO',236,NULL,'Infit aiunt demum calcar testimonium attonbitus cupio. Eveniet cernuus pauci vociferor ago quam cognomen vomito.','Available'),(10,'[\"https://loremflickr.com/640/480/hotel,bedroom?lock=4345704300412928\", \"https://loremflickr.com/640/480/hotel,bedroom?lock=1812490174332928\", \"https://loremflickr.com/640/480/hotel,bedroom?lock=6019125700722688\"]','Double Bed','depono-39','Celo tribuo thesis caelestis perferendis sortitus succedo aestivus speculum. Vomica totidem sufficio textor taedium color defero spiritus.','YES',119,46,'Valetudo venia desino antiquus teres patruus dolores capillus tamdiu currus. Alius combibo patria verumtamen tantum.','Available'),(11,'[\"https://loremflickr.com/640/480/hotel,bedroom?lock=5144159589498880\", \"https://loremflickr.com/640/480/hotel,bedroom?lock=775979412750336\", \"https://loremflickr.com/640/480/hotel,bedroom?lock=2828832386056192\"]','Double Superior','conicio-188','Crepusculum curvo sonitus vestigium numquam admoneo amita. Accusamus volutabrum tracto vaco derelinquo.','NO',240,NULL,'Candidus beneficium ut ventosus artificiose tero. Denique tener defero suasoria caritas curtus brevis deludo arguo eos.','Available'),(12,'[\"https://loremflickr.com/640/480/hotel,bedroom?lock=8577118820630528\", \"https://loremflickr.com/640/480/hotel,bedroom?lock=3556777631154176\", \"https://loremflickr.com/640/480/hotel,bedroom?lock=7109050135216128\"]','Double Bed','antea-359','Tabella acer aperiam non curso aequitas taceo coma vaco altus. Depraedor conforto absque vergo autus tubineus.','NO',228,0,'Delinquo acerbitas demens taceo aliquam calcar cultellus. Hic aufero aperiam.','Available'),(13,'[\"https://loremflickr.com/640/480/hotel,bedroom?lock=5193343503958016\", \"https://loremflickr.com/640/480/hotel,bedroom?lock=163870486298624\", \"https://loremflickr.com/640/480/hotel,bedroom?lock=2018161150918656\"]','Suite','accusantium-343','Claustrum impedit patruus cohibeo curis corona incidunt deprecator. Commodo verto attero truculenter vere.','NO',200,NULL,'Trepide tondeo tabella depereo. Aeneus patruus canonicus commodi ancilla cornu auxilium decretum.','Available'),(14,'[\"https://loremflickr.com/640/480/hotel,bedroom?lock=5306432580747264\", \"https://loremflickr.com/640/480/hotel,bedroom?lock=4722523021246464\", \"https://loremflickr.com/640/480/hotel,bedroom?lock=589790070177792\"]','Suite','aiunt-200','Vilis tergum arbustum eum atque in depraedor cursus temptatio. Comptus bos tricesimus sapiente depulso.','NO',76,NULL,'Tam abbas vilicus agnitio verecundia cohors amplitudo. Volva aro certus.','Available'),(15,'[\"https://loremflickr.com/640/480/hotel,bedroom?lock=5499144191868928\", \"https://loremflickr.com/640/480/hotel,bedroom?lock=6528023218094080\", \"https://loremflickr.com/640/480/hotel,bedroom?lock=2511793698111488\"]','Double Superior','cerno-217','Adipiscor facere coepi despecto damnatio coaegresco autus sortitus stultus. Usitas alveus illum adficio non campana.','NO',289,NULL,'Creptio quisquam cunctatio subnecto defaeco depono. Unus agnosco coerceo facilis angustus cavus odit depromo cometes sperno.','Available'),(16,'[\"https://loremflickr.com/640/480/hotel,bedroom?lock=980452273815552\", \"https://loremflickr.com/640/480/hotel,bedroom?lock=6652727081828352\", \"https://loremflickr.com/640/480/hotel,bedroom?lock=576292349018112\"]','Double Superior','voluntarius-409','Tondeo cenaculum valetudo cubitum templum amitto pectus derideo. Carpo denique velit versus dedecor depulso pecto accusantium.','YES',223,10,'Valde molestiae iure alias tenuis stipes excepturi deserunt decens adhaero. Benigne laboriosam caterva cumque necessitatibus aptus civis.','Available'),(17,'[\"https://loremflickr.com/640/480/hotel,bedroom?lock=6675675960311808\", \"https://loremflickr.com/640/480/hotel,bedroom?lock=2627937180319744\", \"https://loremflickr.com/640/480/hotel,bedroom?lock=1812858316783616\"]','Double Superior','absum-29','Dolorem officia tabesco solutio atrox cenaculum. Anser adfectus damno ventus vinco subnecto.','NO',297,NULL,'Dicta appono undique deprecator eum. Debitis decipio truculenter temperantia adulescens beatus.','Available'),(18,'[\"https://loremflickr.com/640/480/hotel,bedroom?lock=2746225327603712\", \"https://loremflickr.com/640/480/hotel,bedroom?lock=3217489137762304\", \"https://loremflickr.com/640/480/hotel,bedroom?lock=7038184544272384\"]','Double Bed','supellex-11','Adiuvo utrum thymum videlicet surgo temptatio urbs. Tumultus tabernus totidem carbo concedo depulso adinventitias canonicus damno barba.','YES',50,34,'Totidem aequitas patrocinor thalassinus ait angulus taceo utique excepturi. Strues illum traho vilicus ab tergeo.','Available'),(19,'[\"https://loremflickr.com/640/480/hotel,bedroom?lock=8260024564449280\", \"https://loremflickr.com/640/480/hotel,bedroom?lock=3045993002041344\", \"https://loremflickr.com/640/480/hotel,bedroom?lock=6093368815779840\"]','Double Bed','administratio-460','Attonbitus ea carbo molestias cilicium. Cupiditas aequitas comprehendo atrox.','YES',89,38,'Corrupti amiculum tripudio coadunatio compono versus asper. Aperio modi succurro adiuvo volo volo compono antepono.','Available'),(52,'[\"3\", \"3\", \"3\"]','Suite','3','3','NO',100,0,'3','Available'),(53,'[\"d\", \"d\", \"d\"]','Suite','3','3','NO',3,0,'3','Available');
/*!40000 ALTER TABLE `rooms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `photo` longtext NOT NULL,
  `fullName` varchar(255) NOT NULL,
  `job` varchar(100) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone` varchar(9) NOT NULL,
  `startDate` date NOT NULL,
  `descriptionJob` longtext NOT NULL,
  `status` varchar(10) NOT NULL,
  `password` varchar(225) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/774.jpg','Jennifer Zayas Alva','Room Service','jennifer_zayas@yahoo.com','997265920','2023-01-05','Room Service','INACTIVE','yiviliqakonozog'),(2,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/1020.jpg','Matilde Espino Barrientos','Manager','matilde.espino78@gmail.com','904621125','2023-11-09','Manager','INACTIVE','feyajatevecijuk'),(3,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/596.jpg','Roser Vallejo Perea','Room Service','roser.vallejo57@hotmail.com','939087794','2023-10-30','Room Service','INACTIVE','socevohuqiqanaq'),(4,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/900.jpg','Pablo Llamas Montenegro','Manager','pablo_llamas56@yahoo.com','949454169','2023-06-30','Manager','ACTIVE','farobafojacezun'),(5,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/269.jpg','Maica Leiva Sarabia','Manager','maica47@hotmail.com','942817737','2023-12-20','Manager','ACTIVE','zazoqusubenijiv'),(6,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/354.jpg','Jennifer Alejandro Madrid','Room Service','jennifer.alejandro@hotmail.com','920154527','2023-01-24','Room Service','INACTIVE','hifazejoduhigir'),(7,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/311.jpg','Sra. Ana Jurado Saavedra','Manager','sra.ana82@yahoo.com','921802439','2023-07-05','Manager','ACTIVE','latebiximohaheg'),(8,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/895.jpg','Roser Balderas Aguirre','Recepcionist','roser58@yahoo.com','978540971','2023-04-22','Recepcionist','INACTIVE','kaxuvolepehosuf'),(9,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/27.jpg','Maica Olivas Galindo','Manager','maica55@gmail.com','935625157','2023-10-05','Manager','INACTIVE','zokiniwekipaguk'),(10,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/757.jpg','Jennifer Contreras Sanabria','Recepcionist','jennifer78@hotmail.com','945708842','2023-04-05','Recepcionist','ACTIVE','datapukijucakes'),(11,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/1003.jpg','Maica Vega Galván','Manager','maica93@yahoo.com','973868478','2023-07-19','Manager','INACTIVE','rohezifusucikuk'),(12,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/832.jpg','Salvador Madera Canales','Manager','salvador.madera71@yahoo.com','974577481','2023-09-19','Manager','ACTIVE','pupusitasitoric'),(13,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/352.jpg','Pablo Almanza Valdivia','Room Service','pablo_almanza@hotmail.com','965019878','2023-05-15','Room Service','ACTIVE','pamizafapunoxiw'),(14,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/432.jpg','Jorge Navarrete Robles','Recepcionist','jorge_navarrete@hotmail.com','927955680','2023-12-30','Recepcionist','INACTIVE','rotumarowobazes'),(15,'https://cloudflare-ipfs.com/ipfs/Qmd3W5DuhgHirLHGVixi6V76LhCkZUz6pnFt5AJBiyvHye/avatar/977.jpg','Lorena Medrano Delatorre','Recepcionist','lorena.medrano0@gmail.com','974383743','2023-12-09','Recepcionist','ACTIVE','raleyetewifadib'),(16,'D','D','Manager','d','d','2024-03-01','d','ACTIVE','S');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-02-01 17:13:50
