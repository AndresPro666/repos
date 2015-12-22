<?php
	
	include 'Funciones.php';

	$Arreglo= Array();
	
	for($i=0; $i<=10; $i++)
	{
		$Arreglo[$i]=$i * 2;
	}
	
	for($i=1; $i<=10; $i++)
	{
		echo $Arreglo[$i];
		echo "<br>";
		echo "<hr>";
	}
	
	

	
?>
