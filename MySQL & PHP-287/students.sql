-- phpMyAdmin SQL Dump
-- version 3.1.2
-- http://www.phpmyadmin.net
--
-- 主機: localhost
-- 建立日期: Feb 07, 2009, 09:17 AM
-- 伺服器版本: 5.1.31
-- PHP 版本: 5.2.8

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 資料庫: `students`
--
CREATE DATABASE `students` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `students`;

-- --------------------------------------------------------

--
-- 資料表格式： `grade`
--

CREATE TABLE IF NOT EXISTS `grade` (
  `no` varchar(8) NOT NULL DEFAULT '',
  `name` varchar(8) NOT NULL DEFAULT '',
  `chinese` tinyint(4) NOT NULL DEFAULT '0',
  `math` tinyint(4) NOT NULL DEFAULT '0',
  `nature` tinyint(4) NOT NULL DEFAULT '0',
  PRIMARY KEY (`no`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 列出以下資料庫的數據： `grade`
--

INSERT INTO `grade` (`no`, `name`, `chinese`, `math`, `nature`) VALUES
('A8608001', '王大明', 88, 96, 92),
('A8608002', '陳小新', 95, 89, 99),
('A8608003', '小紅豆', 80, 86, 89),
('A8608004', '章小倩', 85, 91, 93),
('A8608005', '李青青', 90, 96, 80),
('A8608006', '孫小美', 80, 77, 82),
('A8608007', '陳俊榮', 100, 98, 95),
('A8608008', '張美麗', 79, 87, 86),
('A8608009', '林娟娟', 75, 73, 79),
('A8608010', '鍾玲玲', 78, 83, 84);
