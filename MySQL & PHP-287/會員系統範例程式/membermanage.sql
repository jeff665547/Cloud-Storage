-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- 主機: 127.0.0.1
-- 產生時間： 2017-08-11 04:06:37
-- 伺服器版本: 10.1.21-MariaDB
-- PHP 版本： 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `membermanage`
--
CREATE DATABASE IF NOT EXISTS `membermanage` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE `membermanage`;

-- --------------------------------------------------------

--
-- 資料表結構 `members`
--

CREATE TABLE IF NOT EXISTS `members` (
  `member_id` int(11) NOT NULL AUTO_INCREMENT,
  `member_account` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `member_password_hash` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `member_name` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `member_birth_year` smallint(6) NOT NULL,
  `member_birth_month` tinyint(4) NOT NULL,
  `member_birth_date` tinyint(4) NOT NULL,
  `member_telephone` varchar(15) COLLATE utf8_unicode_ci NOT NULL,
  `member_email` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `member_address` varchar(200) COLLATE utf8_unicode_ci NOT NULL,
  `member_info` varchar(500) COLLATE utf8_unicode_ci NOT NULL,
  `member_gender` tinyint(4) NOT NULL,
  `member_job` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `member_create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `member_login_time` datetime NOT NULL,
  `member_active` tinyint(1) NOT NULL DEFAULT '1',
  PRIMARY KEY (`member_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 資料表的匯出資料 `members`
--

INSERT INTO `members` (`member_id`, `member_account`, `member_password_hash`, `member_name`, `member_birth_year`, `member_birth_month`, `member_birth_date`, `member_telephone`, `member_email`, `member_address`, `member_info`, `member_gender`, `member_job`, `member_create_time`, `member_login_time`, `member_active`) VALUES
(1, 'aaa', '$2y$10$Sx99LMEfU5XVHbQKCFbaz.rWkE/4YnSLBs2YCbP9yPjHV/sBNYVoS', 'abc', 1999, 12, 31, '12345', '', 'jdfiosdjo', 'abcdefg', 0, 'dvjos', '2017-06-30 11:59:03', '0000-00-00 00:00:00', 0),
(2, 'abc', '$2y$10$Ou6URwlsVa6OHbz0DxLCJ.7nRlNYa8sdbaJ9kBoBH1UO4vO5YQQWW', '', 1900, 1, 1, '', 'proxy.murderer@outlook.com', '', '', 1, '', '2017-07-03 11:19:09', '0000-00-00 00:00:00', 1);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
