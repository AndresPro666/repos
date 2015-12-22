<?php


class Productos {

	private  $idProducto;
	private  $descripcion;
	private  $marca;


public function __construct ($descripcion, $marca){ # sino viene nada en width empieza con el inicializado estos parametros son obligatorios
	$this->setDescripcion($descripcion);
	$this->setMarca($marca);

}


public function setIdProducto ($idProducto){
	$this->idProducto = $idProducto;
}

public function setDescripcion ($descripcion){
	$this->descripcion = $descripcion;
}

public function setMarca($marca){
	$this->marca = $marca;
}


public function getIdProdcuto(){
	return $this->idProducto;
}



public function getDescripcion(){
	return $this->descripcion; 
}

public function getMarca(){
	return $this->marca; 
}


public function registrarProducto( $descripcion_ , $marca_){

include('connectDB2.php');

	
$stmt = $connectDB->prepare("INSERT INTO  productos (descripcion,marca) VALUES('$descripcion_','$marca_' )");
$stmt->execute();


}



}
?>
