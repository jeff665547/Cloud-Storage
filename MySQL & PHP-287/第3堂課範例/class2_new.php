<?php

class Human{
	protected $height;
	protected $weight;
	protected $name;

	function __construct($n,$h=199,$w=200){
		$this->height = $h;
		$this->weight = $w;
		$this->name = $n;
		echo "$n is born!<br>";
	}

	function __destruct(){
		echo $this->name, " is dying!<br>";
	}

	final function get_height(){
		return $this->height;
	}

	function set_height($h){
		$this->height = $h;
	}

	protected function get_weight(){
		return $this->weight;
	}

	function force_get_weight(){
		return $this->get_weight();
	}

	function get_global_population(){
		echo "7 billions!<br>";
	}

	const PI = 3.1415926;
}

class Child extends Human{
	function get_height(){
		// echo parent::get_height(), " cm<br>";
		echo Human::get_height(), " cm<br>";
	}
}


$mike = new Human('Mike',166,170);
$jerry = new Human('Jerry');
$marry = new Child('Marry');

$marry->get_height();

// $mike->set_height(199);

echo "Mike's height: ", $mike->get_height(), "<br>";

echo "Mike's weight: ", $mike->force_get_weight(), "<br>";

$mike = null;
$jerry = null;


Human::get_global_population();
echo "PI = ", Human::PI, "<br>";
?>