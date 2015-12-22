<html>
<head>
  <title> TABLA FIBONACCI </title>
</head>
<body>
  
     <h1>Programa para calcular una serie de fibonacci </h1> 
        <form action= "fibonacci.html.php" method = "POST" > Ingrese el limite de numeros de la serie:
        <input type ="text " value = "" name= "limit"/>
        <input type = "submit" value="Calcular Serie" name= "Calculate"/>

        </form>


  <table style = "border-style : inset; ">
    <thead>  <h2> TABLA FIBONACCI </h2> </thead><br>
  <tbody>
  
     <?php include ("./fibonacci.php");   // include_once si muchos archivos llaman a fibonacci , se cargara  todas las veces q se llame con esto se carga solo una vez.
      // require  se usa para lo mismo que include ,  solamente que si hay un error en el codigo va a detener la ejecucion y te va a avisar.
     //require_once  agrega la caracteristica del once 
      $limit= $_POST["limit"];
      $ser = fibonacci ($limit);  
 
     foreach ($ser as $x){  ?> 
       
     <tr><td style = "border-style: solid;"> <h3> 
      <?php echo $x ; ?> </h3> </td></tr>
      <?php
     }
     
   
    ?> 
  </tbody>

</table>
</body>
</html>


