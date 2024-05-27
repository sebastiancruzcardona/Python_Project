-- Adminer 4.8.1 MySQL 8.3.0 dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

CREATE DATABASE `agenda_digital` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `agenda_digital`;

DROP TABLE IF EXISTS `agenda_digital_contacto`;
CREATE TABLE `agenda_digital_contacto` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(60) NOT NULL,
  `apellido` varchar(60) NOT NULL,
  `telefono` varchar(10) NOT NULL,
  `email` varchar(60) NOT NULL,
  `favorito` tinyint(1) NOT NULL,
  `id_usuario_id` int NOT NULL,
  `categoria` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `agenda_digital_conta_id_usuario_id_15f216df_fk_agenda_di` (`id_usuario_id`),
  CONSTRAINT `agenda_digital_conta_id_usuario_id_15f216df_fk_agenda_di` FOREIGN KEY (`id_usuario_id`) REFERENCES `agenda_digital_usuario` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `agenda_digital_contacto` (`id`, `nombre`, `apellido`, `telefono`, `email`, `favorito`, `id_usuario_id`, `categoria`) VALUES
(3,	'dasd',	'prueb',	'prueba',	'dsad',	0,	2,	'sda'),
(4,	'pruebita',	'pruebita',	'6565',	'pruebita@gmail.com',	1,	2,	'pruebita'),
(5,	'Sebas',	'Cruz',	'31111',	'sebastian@gmail.com',	1,	4,	'amigos'),
(6,	'pruebaIdOculto',	'pruebaIdOculto',	'qwertyuiop',	'pruebaIdOculto',	1,	4,	'pruebaIdOculto'),
(7,	'pruebaNoFavorito',	'pruebaNoFavorito',	'1234567890',	'pruebaNoFavorito@gmail.com',	0,	4,	'Enemigos');

DROP TABLE IF EXISTS `agenda_digital_usuario`;
CREATE TABLE `agenda_digital_usuario` (
  `id` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(60) NOT NULL,
  `email` varchar(60) NOT NULL,
  `telefono` varchar(10) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `agenda_digital_usuario_email_69938401_uniq` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `agenda_digital_usuario` (`id`, `nombre`, `email`, `telefono`, `password`) VALUES
(2,	'Sebastian',	'sebastian@gmail.com',	'3187492128',	'prueba'),
(4,	'test2',	'test2@gmail.com',	'5555',	'test2'),
(5,	'otro test',	'otrotest@gmail.com',	'666',	'otro'),
(6,	'pepito',	'pepito@gmail.com',	'777',	'pepito'),
(7,	'Test2605',	'test2605@gmail.com',	'2605',	'2605'),
(9,	'nuevito',	'nuevito@gmail.com',	'9999',	'nuevito');

DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1,	'Can add log entry',	1,	'add_logentry'),
(2,	'Can change log entry',	1,	'change_logentry'),
(3,	'Can delete log entry',	1,	'delete_logentry'),
(4,	'Can view log entry',	1,	'view_logentry'),
(5,	'Can add permission',	2,	'add_permission'),
(6,	'Can change permission',	2,	'change_permission'),
(7,	'Can delete permission',	2,	'delete_permission'),
(8,	'Can view permission',	2,	'view_permission'),
(9,	'Can add group',	3,	'add_group'),
(10,	'Can change group',	3,	'change_group'),
(11,	'Can delete group',	3,	'delete_group'),
(12,	'Can view group',	3,	'view_group'),
(13,	'Can add user',	4,	'add_user'),
(14,	'Can change user',	4,	'change_user'),
(15,	'Can delete user',	4,	'delete_user'),
(16,	'Can view user',	4,	'view_user'),
(17,	'Can add content type',	5,	'add_contenttype'),
(18,	'Can change content type',	5,	'change_contenttype'),
(19,	'Can delete content type',	5,	'delete_contenttype'),
(20,	'Can view content type',	5,	'view_contenttype'),
(21,	'Can add session',	6,	'add_session'),
(22,	'Can change session',	6,	'change_session'),
(23,	'Can delete session',	6,	'delete_session'),
(24,	'Can view session',	6,	'view_session'),
(25,	'Can add usuario',	7,	'add_usuario'),
(26,	'Can change usuario',	7,	'change_usuario'),
(27,	'Can delete usuario',	7,	'delete_usuario'),
(28,	'Can view usuario',	7,	'view_usuario'),
(29,	'Can add contacto',	8,	'add_contacto'),
(30,	'Can change contacto',	8,	'change_contacto'),
(31,	'Can delete contacto',	8,	'delete_contacto'),
(32,	'Can view contacto',	8,	'view_contacto');

DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1,	'pbkdf2_sha256$720000$UV2vUJ67dseae6G5rHXfqG$fUsr9lYI+YeU3ISdl4t2vFmPX70VoJKiQ+z1lTmJWfw=',	'2024-05-11 23:31:42.934606',	1,	'root',	'',	'',	'sebastiancruzcardona90@gmail.com',	1,	1,	'2024-05-11 23:31:13.695460');

DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;


DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1,	'2024-05-17 00:00:46.151808',	'1',	'usuario object (1)',	1,	'[{\"added\": {}}]',	7,	1),
(2,	'2024-05-17 00:08:00.708292',	'1',	'id: 1 | nombre: Sebastian | email: sebastian@gmail.com | telefono: 3187492128 | password: prueba',	3,	'',	7,	1),
(3,	'2024-05-17 00:08:13.672874',	'2',	'id: 2 | nombre: Sebastian | email: sebastian@gmail.com | telefono: 3187492128 | password: prueba',	1,	'[{\"added\": {}}]',	7,	1);

DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1,	'admin',	'logentry'),
(8,	'agenda_digital',	'contacto'),
(7,	'agenda_digital',	'usuario'),
(3,	'auth',	'group'),
(2,	'auth',	'permission'),
(4,	'auth',	'user'),
(5,	'contenttypes',	'contenttype'),
(6,	'sessions',	'session');

DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1,	'contenttypes',	'0001_initial',	'2024-05-11 23:18:30.347889'),
(2,	'auth',	'0001_initial',	'2024-05-11 23:18:31.739168'),
(3,	'admin',	'0001_initial',	'2024-05-11 23:18:32.083558'),
(4,	'admin',	'0002_logentry_remove_auto_add',	'2024-05-11 23:18:32.098023'),
(5,	'admin',	'0003_logentry_add_action_flag_choices',	'2024-05-11 23:18:32.118205'),
(6,	'agenda_digital',	'0001_initial',	'2024-05-11 23:18:32.191102'),
(7,	'contenttypes',	'0002_remove_content_type_name',	'2024-05-11 23:18:32.377788'),
(8,	'auth',	'0002_alter_permission_name_max_length',	'2024-05-11 23:18:32.504449'),
(9,	'auth',	'0003_alter_user_email_max_length',	'2024-05-11 23:18:32.549299'),
(10,	'auth',	'0004_alter_user_username_opts',	'2024-05-11 23:18:32.565817'),
(11,	'auth',	'0005_alter_user_last_login_null',	'2024-05-11 23:18:32.679905'),
(12,	'auth',	'0006_require_contenttypes_0002',	'2024-05-11 23:18:32.690254'),
(13,	'auth',	'0007_alter_validators_add_error_messages',	'2024-05-11 23:18:32.711822'),
(14,	'auth',	'0008_alter_user_username_max_length',	'2024-05-11 23:18:32.863302'),
(15,	'auth',	'0009_alter_user_last_name_max_length',	'2024-05-11 23:18:33.018631'),
(16,	'auth',	'0010_alter_group_name_max_length',	'2024-05-11 23:18:33.065898'),
(17,	'auth',	'0011_update_proxy_permissions',	'2024-05-11 23:18:33.090162'),
(18,	'auth',	'0012_alter_user_first_name_max_length',	'2024-05-11 23:18:33.237654'),
(19,	'sessions',	'0001_initial',	'2024-05-11 23:18:33.342689'),
(20,	'agenda_digital',	'0002_alter_usuario_email_alter_usuario_nombre_and_more',	'2024-05-15 00:47:55.790909'),
(21,	'agenda_digital',	'0003_contacto',	'2024-05-16 21:15:54.491932'),
(22,	'agenda_digital',	'0004_alter_usuario_email',	'2024-05-16 23:45:54.535152'),
(23,	'agenda_digital',	'0005_contacto_categoria_alter_contacto_favorito',	'2024-05-18 04:24:40.324450');

DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('u76nhxrndwg5mfvgj82xlijqvg5xb43k',	'.eJxVjEEOwiAQAP_C2RCgQLsevfcNZHehUjWQlPZk_Lsh6UGvM5N5i4DHnsPR0hbWKK5Ci8svI-RnKl3EB5Z7lVzLvq0keyJP2-RcY3rdzvZvkLHlvgVO5GGaNChM0VtP0YLDYVFAI_FAMIJxdtCa0XuMLhlka-xiURF78fkC4lQ4AA:1s5wBq:XsUGCdYbci5e1vZIveEYC3C_kqu0672Q7VItZi0U400',	'2024-05-25 23:31:42.955531');

-- 2024-05-27 02:32:23
