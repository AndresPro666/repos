<?php

include 'Factura.php';
include 'Cliente.php';
include 'Producto.php';


ini_set ('error_reporting', E_ALL); # con esto me muestra los errores en el nav


$Producto = new Productos("",null);
$cliente2 = new Clientes("","","");
$Factura = new Facturas("","","","","",""); 


$cliente2->registrarCliente(33000000," Akiles Bailo", 3722426263);

$Producto->registrarProducto("Cafe","La Virginia");
$Factura->registrarFactura('2001-04-12',"Factura tipo A",False,67,2, 25);



?>