<?php 

include('connectDB2.php');


$dato = $_POST['q'];
$criterio = $_POST['r'];


			 


if ($criterio=='dni'){


$consulta= 'SELECT * FROM clientes c WHERE c.dni=?';

}else{


$consulta= 'SELECT * FROM clientes c WHERE c.nomYap=?';

}



$stmt= $connectDB->prepare($consulta);


$stmt->bind_param('s',$dato);   // ccon la i o s le dice q el tipo de dato es entero o string 
$stmt->execute();

$result = $stmt->get_result();
// primero preparamaos la consulta. despues cargamos la consulta con los parametros de busqueda y por ultimo ejecutamos la consulta que fue remplazada por el parametro i , id

// la consulta nos devuelve todas las filas por eso filtramos
//$row = $result->fetch_assoc();

//echo json_encode($row['nomYap']);   //y acá le decimos que de todas las columnas me traiga el monto


echo json_encode($result->fetch_assoc());
	
?>