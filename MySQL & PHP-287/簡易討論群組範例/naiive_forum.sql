-- phpMyAdmin SQL Dump
-- version 4.6.5.2
-- https://www.phpmyadmin.net/
--
-- 主機: 127.0.0.1
-- 產生時間： 2017-08-10 05:55:28
-- 伺服器版本: 10.1.21-MariaDB
-- PHP 版本： 5.6.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `naiive_forum`
--
CREATE DATABASE IF NOT EXISTS `naiive_forum` DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci;
USE `naiive_forum`;

-- --------------------------------------------------------

--
-- 資料表結構 `posts`
--

CREATE TABLE IF NOT EXISTS `posts` (
  `post_id` int(11) NOT NULL AUTO_INCREMENT,
  `post_reply_id` int(11) NOT NULL,
  `post_title` varchar(255) COLLATE utf8_unicode_ci NOT NULL DEFAULT '無標題',
  `post_author` varchar(30) COLLATE utf8_unicode_ci NOT NULL DEFAULT '無作者',
  `post_content` varchar(1000) COLLATE utf8_unicode_ci NOT NULL DEFAULT '無內文',
  `post_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `post_reply` tinyint(1) NOT NULL DEFAULT '0',
  PRIMARY KEY (`post_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- 資料表的匯出資料 `posts`
--

INSERT INTO `posts` (`post_id`, `post_reply_id`, `post_title`, `post_author`, `post_content`, `post_time`, `post_reply`) VALUES
(1, 0, '123', '123', 'vmdislvms\r\ndvjsiodjvs', '2017-08-10 11:49:15', 0),
(2, 0, 'jdfiodsj', 'fndsifnu', 'fsdufsd\'fjidsfks\'\r\ndfiosdjofis', '2017-08-10 11:49:58', 0);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
