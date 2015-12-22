<?php
   
    $x= $_POST["x"];
    $y= $_POST["y"];
    $SelectedRadio= $_POST["operaciones"];
    
    if(SelectedRadio == "suma"){
    	print "La suma es: ".suma($x, $y);
    }
    
    if(SelectedRadio == "resta"){
    	print "La resta es: ".resta($x, $y);
    }
    
    if(SelectedRadio == "mult"){
    	print "La multiplicaion es: ".mult($x, $y);
    }
    
    if(SelectedRadio == "div"){
    	print "La division es: ".div($x, $y);
    }
    
?>    
