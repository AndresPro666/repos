<?php 

include('connectDB2.php');


$idCliente= $_GET['q'];

$stmt= $connectDB->prepare('SELECT * FROM facturas f WHERE f.estadoPago=0 AND f.Cliente_idCliente= ? ');

$stmt->bind_param('i',$idCliente);   // ccon la i le dice q el tipo de dato es entero
$stmt->execute();

$result = $stmt->get_result();
// primero preparamaos la consulta. despues cargamos la consulta con los parametros de busqueda y por ultimo ejecutamos la consulta que fue remplazada por el parametro i , id

// la consulta nos devuelve todas las filas por eso filtramos
$row = $result->fetch_assoc();

echo json_encode($row['monto']);   //y acá le decimos que de todas las columnas me traiga el monto




?>