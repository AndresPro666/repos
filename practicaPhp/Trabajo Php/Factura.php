<?php 


class Facturas  {

	private $idFactura;
 	private $idCliente; 
 	private $idProducto;
	private $fecha;
	private $descripcion;
	private $estadoPago;
	private $monto;


	public function __construct( $fecha, $descripcion, $estadoPago, $idCliente, $idProducto, $monto){

	
		$this->setFecha($fecha);
		$this->setDescripcion($descripcion);
		$this->setEstadoPago($estadoPago);
		$this->setIdCliente($idCliente);
		$this->setIdProducto($idProducto);
		$this->setMonto($monto);
	} 


	public function setIdFactura ($idFactura){
		$this->idFactura = $idFactura;
	}


	public function setIdCliente ($idCliente){
		$this->idCliente = $idCliente;
	}

	public function setIdProducto ($idProducto){
		$this->idProducto = $idProducto;
	}
	public function setFecha($fecha){
		$this->fecha = $fecha;
	}
	public function setDescripcion($descripcion){
		$this->descripcion = $descripcion;
	}
	public function setEstadoPago($estadoPago){
		$this->estadoPago = $estadoPago;
	}
	public function setMonto($monto){
		$this->monto = $monto;
	}
	

    public function getIdFactura(){
	return $this->idFactura; }

	public function getIdCliente(){
	return $this->idCliente; }

	public function getIdProducto(){
	return $this->idProducto; }

	public function getFecha(){
	return $this->fecha; }

	public function getDescripcion(){
	return $this->descripcion; }

	public function getEstadoPago(){
	return $this->estadoPago; }

	public function getMonto(){
	return $this->monto; }


public function registrarFactura( $fecha_, $descripcion_, $estadoPago_,$idCliente_, $idProducto_,$monto_){

include('connectDB2.php');

$stmt = $connectDB->prepare("INSERT INTO facturas (fecha,descripcion,estadoPago,Cliente_idCliente,Producto_idProducto,monto) VALUES('$fecha_' , '$descripcion_' , '$estadoPago_','$idCliente_','$idProducto_','monto_')");
$stmt->execute();


#-> ingresamos a metodos o atributos  y  :: ... nos sirve para acceder a las constantes 

		}

}

?>