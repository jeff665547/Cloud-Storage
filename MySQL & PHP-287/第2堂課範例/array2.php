<?php

$arr = array("y" => "a", 101 => "b", "c", "xyz");

// $arr[] = array(1,2,3,4,5);

// $arr[] = 188;
// $arr[] = 200;
// $arr[] = 2.33;

// var_dump($arr[104][3]);

$b = 100;

foreach($arr as $key => $val){
	$arr[$key] = $val . ' ' . $val;
}

//var_dump($arr);


$str = 'string';

$str[3] = 'abcdsf';

// echo $str;


function avg(){
	$args = func_get_args();
	$sum = 0;
	foreach($args as $key => $val){
		$sum += $val;
	}
	//return $sum / func_num_args();
	return $sum / sizeof($args);
}

echo avg(93,82,17,1873,281);

// echo $b, "<br>";

?>