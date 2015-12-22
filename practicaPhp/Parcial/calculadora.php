<?php
    
            
 	$n1= $_POST ["n1"];
    $n2= $_POST ["n2"];
    $operacion= $_POST ["operacion"];


    function suma ($x, $y){
     $s= $x + $y;
     return $s;
   }
   
   function resta ($x, $y){
     $r = $x - $y;
     return $r;
   }
   
   function mult ($x, $y){
     $m = $x * $y;
     return $m;
   }
   
   function div ($x, $y){
     $d = $x / $y;
     return $d;
   }

    if ($operacion == "suma"){

        $resultado = suma($n1, $n2);
    


    }elseif ($operacion == "resta"){
        $resultado = resta($n1, $n2); 
      


    }elseif ($operacion == "multiplicacion"){
        $resultado = mult($n1, $n2);
   


    }elseif($operacion == "division"){
        
        if ($n2=="0"){

           
            $resultado = " error";
        }else {
             $resultado = div($n1, $n2);
            

         }

        }
?>

<html>
<head>
    <title></title>
</head>
<body>
    <br>
    <table style = "border-style: solid;">
       <thead>
            <tr>
                <th>Resultado </th>
            </tr>
        </thead>
        <tbody style = "border-style: solid;" >
            <tr>
                <td> <b>Operación:</b></td> <td> <?php echo $operacion;  ?>  </td>
            </tr>
            <tr>
                <td> <b>numero 1</b> </td><td> <?php echo $n1;  ?>  </td>
            </tr>
            <tr>
                <td> <b>numero 2</b></td><td> <?php echo $n2;  ?>  </td>
            </tr>
             <tr>
                <td> <b>Resultado  </b></td><td> <?php echo $resultado;  ?>  </td>
            </tr>
        </tbody>
    </table>

</body>
</html>