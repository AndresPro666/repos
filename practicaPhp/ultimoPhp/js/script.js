$(document).ready(function(){     // esto se va a carrgar cada vez q el documento este listo  la funcion anonima


	$("#buscarDatos").on("click",function(){   // osea traeme el componente con id buscarFact con el numeral nos referimos a un componente por su id .. el hashtack
	   													// on recibe dos parametros la funcion  y el evento	
	 buscarDatosCliente($("#dato").val(),$('input:radio[name=group1]:checked').val());   //como estamos haciendo referencia al id va # 														
												
	});
});   


function buscarDatosCliente(dato, group1){


	$.ajax({ //llamamos a jquery, 
		method:"POST",
		url:'buscarDatos.php',
		data: {q:dato, r:group1}
		//data: 'q='+dato + 'r='+group1	
	}).done(function(response){    // le decimos qe vamos a traerrr
		response = JSON.parse(response);
		console.log("respuesta "+group1);
		console.log("respuesta "+dato);
	          		if(response == null){
	          			$("#error").text("Error, no existe el cliente");
	          			$("#error").show();
	          			document.getElementById('dni').value = '';
	          			document.getElementById('nomYap').value = '';
	          			document.getElementById('direccion').value = '';
	          			document.getElementById('ciudad').value = '';
	          			document.getElementById('telefono').value = '';
	          		}else{
	          			$("#nomYap").val(response['nomYap']);
		          		$("#telefono").val(response['telefono']);
		          		$("#direccion").val(response['direccion']);
		          		$("#ciudad").val(response['ciudad']);
		          		$("#dni").val(response['dni']);
		          		$("#error").text("");
		          		$("#error").show();

	          		}	
	
	}).fail(function(){
		
		$("#error").text("Hubo un error en la obtencion de los datos");
	    $("#error").show();

	
	});      

	}      


// el done se ejecuta cuando todo sale bien