  <html> 
  <head>
  	<title> FORM EXAMPLE </title>
  </head>
  		<body>
  			<form action= "calculadora.php" method = "post" >
 				<select name="operacion"> 
					<option value="suma">suma</option> 
					<option value="resta">resta </option> 
					<option value="multiplicacion">multiplicacion </option> 
					<option value="division">division </option> 
				</select> 
 				
 				<input type ="text" value = "" name= "n1"/>
 				<input type ="text" value = "" name= "n2"/>

 				<input type = "submit" value="Calcular" name= "Calcular"/>

  			</form>
  		</body>
  </html> 