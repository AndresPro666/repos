-- phpMyAdmin SQL Dump
-- version 4.3.11
-- http://www.phpmyadmin.net
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 05-12-2015 a las 00:30:24
-- Versión del servidor: 5.6.24
-- Versión de PHP: 5.6.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de datos: `informatorio`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `clientes`
--

CREATE TABLE IF NOT EXISTS `clientes` (
  `idCliente` int(11) NOT NULL,
  `dni` varchar(10) NOT NULL,
  `nomYap` varchar(45) NOT NULL,
  `telefono` int(11) NOT NULL,
  `direccion` varchar(150) NOT NULL,
  `ciudad` varchar(100) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `clientes`
--

INSERT INTO `clientes` (`idCliente`, `dni`, `nomYap`, `telefono`, `direccion`, `ciudad`) VALUES
(69, '33945621', ' Akiles Bailo', 2147483647, '9 de julio 1330', 'Resistencia'),
(70, '0', 'loco', 2147483647, 'la lomas 2030', 'resis'),
(71, '33945621', 'Akiles Bailo', 2147483647, '9 de julio 1330', 'Resistencia'),
(72, '33333333', 'Aldo Rico', 2147483647, 'Pelegrini 2032', 'Corrientes'),
(73, '33222333', 'Mosbo Rachos', 2147483647, '9 de julio 330', 'Formosa'),
(74, '32333222', 'Barri Gota', 2147483647, '3 de abril 1820', 'Misiones'),
(75, '25222555', 'el barto', 2147483647, '25 de mayo 1330', 'Resistencia');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `clientes`
--
ALTER TABLE `clientes`
  ADD PRIMARY KEY (`idCliente`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `clientes`
--
ALTER TABLE `clientes`
  MODIFY `idCliente` int(11) NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=76;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
