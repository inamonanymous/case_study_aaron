-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 15, 2023 at 01:15 AM
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
-- Table structure for table `inventory`
--

CREATE TABLE `inventory` (
  `id` int(11) NOT NULL,
  `supply_id` int(11) NOT NULL,
  `qty` int(11) NOT NULL,
  `stock_type` smallint(6) NOT NULL,
  `date_created` datetime NOT NULL,
  `main` smallint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `inventory`
--

INSERT INTO `inventory` (`id`, `supply_id`, `qty`, `stock_type`, `date_created`, `main`) VALUES
(1, 5, 25, 0, '2023-10-14 02:20:40', 1),
(2, 6, 10, 0, '2023-10-14 02:18:04', 1),
(11, 7, 6, 0, '2023-10-14 02:36:25', 1),
(14, 5, 1, 1, '2023-10-14 02:48:12', 0),
(15, 5, 1, 1, '2023-10-14 02:49:03', 0),
(16, 5, 1, 1, '2023-10-14 02:49:58', 0),
(17, 5, 5, 1, '2023-10-14 02:50:04', 0),
(18, 5, 50, 0, '2023-10-14 02:53:29', 0),
(19, 5, 5, 0, '2023-10-14 02:54:34', 0),
(20, 6, 1, 0, '2023-10-14 03:06:09', 0),
(21, 6, 1, 1, '2023-10-14 03:10:09', 0),
(22, 6, 7, 1, '2023-10-14 03:10:26', 0),
(23, 8, 15, 0, '2023-10-14 03:14:27', 1),
(24, 8, 15, 1, '2023-10-14 03:14:46', 0);

-- --------------------------------------------------------

--
-- Table structure for table `laundry_categories`
--

CREATE TABLE `laundry_categories` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `price` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `laundry_categories`
--

INSERT INTO `laundry_categories` (`id`, `name`, `price`) VALUES
(1, 'Bed Sheets', 30),
(2, 'Clothes', 25),
(3, 'Maong', 50),
(6, 'Blanket', 100),
(7, 'Polo', 15);

-- --------------------------------------------------------

--
-- Table structure for table `laundry_items`
--

CREATE TABLE `laundry_items` (
  `id` int(11) NOT NULL,
  `laundry_category_id` int(11) NOT NULL,
  `weight` double NOT NULL,
  `laundry_id` int(11) NOT NULL,
  `unit_price` double NOT NULL,
  `amount` double NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `laundry_items`
--

INSERT INTO `laundry_items` (`id`, `laundry_category_id`, `weight`, `laundry_id`, `unit_price`, `amount`) VALUES
(1, 2, 11, 2, 25, 275),
(2, 2, 12, 3, 25, 300),
(3, 1, 3, 4, 30, 90),
(4, 2, 12, 5, 25, 300),
(5, 3, 1, 6, 50, 50),
(6, 6, 21, 7, 100, 2100),
(7, 7, 1, 8, 15, 15),
(8, 2, 12, 9, 25, 300),
(9, 2, 12, 10, 25, 300),
(10, 2, 12, 11, 25, 300),
(11, 2, 12, 12, 25, 300);

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
(5, 'Derrick Rose', 0, 1, 300, 0, 0, 0, 'none', '2023-10-11 01:04:32'),
(6, 'Aaron Torres', 0, 1, 50, 0, 0, 0, 'noneasdf', '2023-10-11 01:13:12'),
(9, 'Derrick Rose', 0, 1, 300, 0, 0, 0, '444', '2023-10-14 01:26:52'),
(11, 'Derrick Rose', 0, 1, 300, 1, 123213123, 123212823, 'none', '2023-10-15 05:41:48'),
(12, 'asdf', 0, 1, 300, 1, 2222, 1922, '444', '2023-10-15 05:42:06');

-- --------------------------------------------------------

--
-- Table structure for table `supply_list`
--

CREATE TABLE `supply_list` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `supply_list`
--

INSERT INTO `supply_list` (`id`, `name`) VALUES
(5, 'Clorox-colorsafe'),
(6, 'Fabric'),
(7, 'Detergent'),
(8, 'Baking Soda');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(200) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(200) NOT NULL,
  `type` smallint(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `username`, `password`, `type`) VALUES
(1, 'example', 'admin', 'admin', 1),
(2, 'Aaron Torres', 'aaron', 'password', 0),
(3, 'Alyza Aliman', 'aliali', 'password', 0);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `inventory`
--
ALTER TABLE `inventory`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `laundry_categories`
--
ALTER TABLE `laundry_categories`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `laundry_items`
--
ALTER TABLE `laundry_items`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `laundry_list`
--
ALTER TABLE `laundry_list`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `supply_list`
--
ALTER TABLE `supply_list`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `inventory`
--
ALTER TABLE `inventory`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `laundry_categories`
--
ALTER TABLE `laundry_categories`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `laundry_items`
--
ALTER TABLE `laundry_items`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `laundry_list`
--
ALTER TABLE `laundry_list`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `supply_list`
--
ALTER TABLE `supply_list`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
