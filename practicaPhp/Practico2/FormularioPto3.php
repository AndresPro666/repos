<html>
<body>

   <form action= "Validate.php" method= "POST"> 
      
      <fieldset>   
      <label>Nombres:</label>
      <input type= "text" name= "nombres"><br>
      
      <label>Apellidos:</label>
      <input type="text" name= "apellidos"><br>
      
      <label>Correo:</label>
      <input type= "text" name= "correo"><br>
      
      <label>Direccion Administrativa:</label>
      <select name= "direccion">
        <option value= "Recursos Humanos" selected= "selected">Recursos Humanos</option>
        <option value= "Ventas">Ventas</option>
        <option value= "Compras">Compras</option>
      </select><br>
      
      <br>
      
      <label>Observaciones:</label><br>
      <textarea rows="4" cols="30"></textarea><br>
      
      <input type= "submit" name= "Enviar Datos" value= "Enviar Datos">
      <input type= "reset" name= "Borrar" value= "Borrar">
     
      </fieldset>
      
   </form>
   
</body>
</html>
      
      
      