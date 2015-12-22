<!DOCTYPE html>
<html> 
  <head>
  	
     <script type="text/javascript"  src= "libs/jquery-1.11.3.js"> </script>
     <script type="text/javascript" src="js/script.js"> </script>

    <title> BUSCAR DATOS DE CLIENTES</title>
  </head>
  		<body>
  			
 				Seleccione el criterio de busqueda... 
        <br>
      <input type="radio"  name="group1" value="dni" checked> Dni <br>
      <input type="radio"  name="group1" value="nombre" > Nombre<br>
 				<br>
 				Ingrese El dato del Cliente <input type ="text" name="dato" id="dato"/> 
 	
         <button id="buscarDatos"  name ="buscarDatos"> Buscar  Datos  </button> <br>
 		
         <p id="error" class="error"></p> 


         <br/>
            <table>
              <tr>
                <td>Dni: </td>
                <td><input type ="text" name="dni" id="dni"/></td>
              </tr>
              <tr>
                <td>Nombre: </td>
                <td><input type ="text" name="nomYap" id="nomYap"/></td>
              </tr>
              <tr>
                <td>Telefono: </td>
                <td><input type ="text" name="telefono" id="telefono"/></td>
              </tr>
              <tr>
                <td>Direccion: </td>
                <td><input type ="text" name="direccion" id="direccion"/></td>
              </tr>
               <tr>
                <td>Ciudad: </td>
                <td><input type ="text" name="ciudad" id="ciudad"/></td>
              </tr>

            </table>
  		
  		</body>
  </html> 

