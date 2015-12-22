<?php


include 'Cliente.php';



ini_set ('error_reporting', E_ALL); # con esto me muestra los errores en el nav



$cliente = new Clientes("","","","","");
$cliente1 = new Clientes("","","","","");
$cliente2= new Clientes("","","","","");
$cliente3 = new Clientes("","","","","");
$cliente4 = new Clientes("","","","","");



$cliente->registrarCliente(33945621,"Akiles Bailo", 3722426263,"9 de julio 1330" , "Resistencia");
$cliente1->registrarCliente(33333333,"Aldo Rico", 3722426263,"Pelegrini 2032" , "Corrientes");
$cliente2->registrarCliente(33222333,"Mosbo Rachos", 3722426263,"9 de julio 330" , "Formosa");
$cliente3->registrarCliente(32333222,"Barri Gota", 3722426263,"3 de abril 1820" , "Misiones");
$cliente4->registrarCliente(25222555,"el barto", 3722426263,"25 de mayo 1330" , "Resistencia");




?>