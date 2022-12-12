<?php
	
function avg(&$a,&$b,$c,$d=100,$e=100){
	$a=10000;
	return ($a+$b+$c+$d)/4;
}

$t=100;
$w=200;
$x=300;

avg($t,$w,$x);

echo $t;

?>