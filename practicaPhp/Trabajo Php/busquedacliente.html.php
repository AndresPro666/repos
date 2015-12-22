<!DOCTYPE html>
<html>
<head>
      
        <script type="text/javascript"  src= "libs/jquery-1.11.3.js"> </script>
        <script type="text/javascript" > 
function  searchClient (dni){
    $.ajax(
    {
      method:"GET",
      url:"busquedaAjax.php",
      data: 'q='+dni,
      dataType:"JSON",
    }
    ).done(
    
    function (response){
   	    response = JSON.parse(response);   
   			if(response == null){
   			$("#error").text("Error, no existe ese cliente");
        $("#error").show();
        
        }else{
   			
        $("#idFactura").val(response['idFactura']);
   			$("#monto").val(response['monto']); // elsegundo valor corresponde ala base de datos
   			$("#idCliente").val(response['idCliente']);
        $("#dni").val(response['dni']);
        $("#monto").show();
         
   		}
   	  }	
      ).fail(
              function(){ 
              $("#error").text("Error, no existe ese cliente");
              $("#error").show();
              }         
             );
      }
    
      $(document).ready(function(){
      $("#error").hide();
      $("#search").on("click", function(){
      $("#idFactura").val("");
      $("#monto").val("");
      $("#idCliente").val("");
      $("#dni").val("");
      searchClient($("#dni").val());         });
                                    });

      
 </script>

</head>
<body>
 <p> Introduzca el dni del Cliente para ver sus facturas impagas 
 <input type= "text" name="dni" id= "dni" />
 <button id="search"  name ="search"> Buscar  Factura  </button>
 </p>

<table>
   
</table>

</body>
</html>


