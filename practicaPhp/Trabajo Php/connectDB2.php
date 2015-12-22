<?php 

$connectDB = new mysqli('localhost', 'root' , '','informatorio');
if ($connectDB ->connect_errno) {
 printf("Error de conexión: %s\n", $connectDB ->connect_errno);
 exit();
}


?>