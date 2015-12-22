$(document).ready(function(){
    $("#search").on ("click", function () {// jquery utiliza esata terminoologia 
	//console.log("Button Words"); con esto imprime por consola.

	searchClient($("#id").val());    //# con esto le pega al componente por el id, con el punto se le puede pegar por la clase.
	}); 
});

function  searchClient (str){
    
    var xmlhttp = new XMLHttpRequest();  // este es una var nativa de js

    xmlhttp.onreadystatechange = function (){
   	if(xmlhttp.readyState == 4 && xmlhttp.status == 200){// esto es un estandar para saber si todo sale bien :D   
   			var response = JSON.parse(xmlhttp.responseText);
   			
   			console.log ("respuesta" +response);
   			$("#descripcion").val(response['descripcion']);
   			$("#monto").val(response['monto']); // elsegundo valor corresponde ala base de datos
   	

   			//console.log(xmlhttp.responseText);
   		}

   	}	
    xmlhttp.open("GET", "busquedaAjax.php?q=" +str,true);  // aca le damos metodo, nombre del archivo. ajax. y el paramatro de la consulta que le vmos a pasar
    xmlhttp.send(); // con esto mandamos la consulta.
}