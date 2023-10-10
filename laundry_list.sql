-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 10, 2023 at 07:15 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `laundry_aaron`
--

-- --------------------------------------------------------

--
-- Table structure for table `laundry_list`
--

CREATE TABLE `laundry_list` (
  `id` int(11) NOT NULL,
  `customer_name` varchar(255) NOT NULL,
  `status` smallint(6) NOT NULL COMMENT '0=pending, 1=ongoing, 2=ready, 3=claimed',
  `queue` int(11) NOT NULL,
  `total_amount` double NOT NULL,
  `pay_status` smallint(6) DEFAULT NULL,
  `amount_tendered` double NOT NULL,
  `amount_change` double NOT NULL,
  `remarks` varchar(255) NOT NULL,
  `date_created` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `laundry_list`
--

INSERT INTO `laundry_list` (`id`, `customer_name`, `status`, `queue`, `total_amount`, `pay_status`, `amount_tendered`, `amount_change`, `remarks`, `date_created`) VALUES
(1, 'James Smith', 3, 1, 555, 1, 555, 0, 'None', '2023-10-10 04:41:58'),
(2, 'asdf', 0, 1, 275, 0, 0, 0, '', '2023-10-10 14:52:43'),
(3, 'gfh', 0, 1, 300, 0, 0, 0, '444', '2023-10-10 15:07:03'),
(4, 'sample', 0, 1, 90, 0, 0, 0, 'none', '2023-10-10 15:08:06'),
(5, 'Derrick Rose', 0, 1, 300, 0, 0, 0, 'none', '2023-10-11 01:04:32'),
(6, 'Aaron Torres', 0, 1, 50, 0, 0, 0, 'noneasdf', '2023-10-11 01:13:12');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `laundry_list`
--
ALTER TABLE `laundry_list`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `laundry_list`
--
ALTER TABLE `laundry_list`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
