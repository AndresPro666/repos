<?php 

	$connectDB =  new mysqli('localhost', 'root' , '', 'mydb');

	if (mysqli_connect_errno()){

		printf("Error de conexion %s \n" , mysqli_connect_error());
		exit();
	}

?>