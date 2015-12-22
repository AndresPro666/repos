<?php



class Clientes {

   	private  $idCliente;
	private  $dni;
	private  $nomYap;
	private  $telefono;


public function __construct ($dni, $nomYap, $telefono){ # sino viene nada en width empieza con el inicializado estos parametros son obligatorios
	$this->setDni($dni);
	$this->setNomYap($nomYap);
	$this->setTelefono($telefono);
	
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


public function registrarCliente($dni_, $nomYap_ , $telefono_){

include('connectDB2.php');

$stmt = $connectDB->prepare("INSERT INTO  clientes (dni,nomYap,telefono) VALUES('$dni_','$nomYap_','$telefono_')");
$stmt->execute();


}

}
?>
