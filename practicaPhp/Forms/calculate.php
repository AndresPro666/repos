<?php

    function calculate ($edad){
        
 	$result = "";  
    if (empty($edad)){
    	$error = "error , tu variable esta vacia GILLLLL"; 
    }else { 
 	  	if (is_numeric($edad)){
 			$result =  $edad;
 		} else {
 			$error = "error, eso no es un entero gilll ";
 		}
    
     } 
     $response = array ();
        if ($error === null){
        	$response= arrray (
        		"status" => true ,
        		"data" => $result
        		);
        }else {
        	$response = array ("status" => false, "data" =>$error);
        }
        return $result
    } 

    // usage 

 	if ($_SERVER["REQUEST_METHOD"] ==="GET"){
 		$value = $_GET  ["edad"];
 	}else {
 	 	$value= $_POST ["edad"];
 	}

 	$res = calculate($value);

    
 ?>		 



 <html>	
   <head></head>
   		<body>  
 			<div>
                 <?php if ($res["status"]) {?>

                 EXITO : <?php echo $res ["data"];?> 

                 <?php } else { ?>

                 ERROR: <?php echo $res ["data"];?>

                 <?php } ?>

 			</div>
   		</body>
 </html>