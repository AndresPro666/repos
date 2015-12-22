<?php

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
   	 return d;
   }
   	 
   function mayor ($x, $y){
   	 if ($x > $y){
   	 	return $x;
   	    }
   	    else{
   	    	return $y;
   	        }
   }
   
   function absoluto ($x){
   	  return abs($x);
     }
   	 
   function potenciaConTabla ($x, $y){
   	  $total = pow ($x, $y);
   	  return $total;
   	  
   	  echo "<table border=1>";
   	   for ($n1=1; n1<=4; $n1++){
   	   	 echo "<tr>";
   	   	    for ($n2=1; $n2<=4; $n2++)
   	   	     echo "<td>".potenciaConTabla($n1, $n2)."</td>";
   	   	  echo "<tr>";
   	   }
   	  echo "</table>"; 
   }

   function sumatoria ($x){
   	  $total = 0;
   	  while ($x >= 1){
   	  	$total = $x + $total;
   	  	$n = $n-1;
   	  }
   	  return $total;
   }	

?>