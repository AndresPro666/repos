$(document).ready(function(){     // esto se va a carrgar cada vez q el documento este listo  la funcion anonima


	$("#buscarFact").on("click",function(){   // osea traeme el componente con id buscarFact con el numeral nos referimos a un componente por su id .. el hashtack
	   													// on recibe dos parametros la funcion  y el evento	
	 buscarFacturasImpagas($("#Cliente_idCliente").val());   //como estamos haciendo referencia al id va # 														
												
	});
});   


function buscarFacturasImpagas(idCliente){

	$.ajax({ //llamamos a jquery, 
		method:"GET",
		url:'buscarFacturasImpagas.php',
		data:'q='+idCliente	
	}).done(function(montoDeuda){    // le decimos qe vamos a traerrr
		console.log("el cliente debe "+montoDeuda);	
	
	}).fail(function(){
		
		alert("ha fallado");	
	
	});      

	}      




// el done se ejecuta cuando todo sale bien