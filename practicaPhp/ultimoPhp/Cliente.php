<?php



class Clientes {

   	private  $idCliente;
	private  $dni;
	private  $nomYap;
	private  $telefono;
	private  $direccion;
	private  $ciudad;
	


public function __construct ($dni, $nomYap, $telefono, $direccion, $ciudad){ # sino viene nada en width empieza con el inicializado estos parametros son obligatorios
	$this->setDni($dni);
	$this->setNomYap($nomYap);
	$this->setTelefono($telefono);
	$this->setTelefono($direccion);
	$this->setTelefono($ciudad);
	
	
}


public function setIdCliente ($idCliente){
	$this->idCliente = $idCliente;
}

public function setDni ($dni){
	$this->dni = $dni;
}

public function setNomYap ($nomYap){
	$this->nomYap = $nomYap;
}

public function setTelefono ($telefono){
	$this->telefono = $telefono;
}

public function setDireccion ($direccion){
	$this->direccion = $direccion;
}


public function setCiudad ($ciudad){
	$this->$ciudad = $ciudad;
}


public function getCiudad(){
	return $this->ciudad;
}

public function getDireccion(){
	return $this->direccion;
}


public function getIdCliente(){
	return $this->idCliente;
}

public function getDni(){
	return $this->dni;
}


public function getNomYap(){
	return $this->nomYap; 
}

public function getTelefono(){
	return $this->telefono; 
}


public function registrarCliente($dni_, $nomYap_ , $telefono_ ,$direccion_ , $ciudad_){

include('connectDB2.php');

$stmt = $connectDB->prepare("INSERT INTO  clientes (dni,nomYap,telefono,direccion,ciudad) VALUES('$dni_','$nomYap_','$telefono_', '$direccion_', '$ciudad_')");
$stmt->execute();


}

}
?>
