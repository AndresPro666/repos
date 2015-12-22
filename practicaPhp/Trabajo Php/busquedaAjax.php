<?php

include("connectDB2.php");

$dni= $_GET['q'];  // este es el paramatro q del otro archivo gralmente se usa q de query 

$stmt = $connectDB -> prepare('SELECT f.idFactura , f.monto , c.idCliente , c.dni FROM facturas f  inner join clientes c on f.Cliente_idCliente = c.idCliente where F.estadoPago = 0 and c.dni = ? ');

$stmt-> bind_param('i', $dni);
$stmt-> execute();

$result = $stmt->get_result();
// primero preparamaos la consulta. despues cargamos la consulta con los parametros de busqueda y por ultimo ejecutamos la consulta que fue remplazada por el parametro i , id

echo json_encode($result->fetch_assoc());


					    # esto nos devuelve el resultado como un array asociativo clave-valor	
//     


?>





