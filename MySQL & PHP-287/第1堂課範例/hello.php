<!DOCTYPE html>
<html>
<head>
	<title>Hello</title>
	<meta charset="utf8">
</head>
<body>
	<?php
		$s = "duash'<br>chuisa\"";
		echo $s;
		echo "<br>";
		$s2 = '" \'';
		echo $s2;
		echo "<br>";

		$a = 1000;
		echo "I have $a apples.<br>";		
		echo "I have \$aapples.<br>";

		if(1 === '1'){
			echo "Equivalent!";
		}else{
			echo "Not equivalent!";
		}
		echo "<br>";

		$x = 0;
		echo ++$x, "<br>";
		echo $x, "<br>";
		$x = 5;
		if($x > 5){
			echo "Greater than 5!!<br>";
		}elseif($x > 4){
			echo "Greater than 4!!<br>";
		}elseif($x > 3){
			echo "Greater than 3!!<br>";
		}elseif($x > 2){
			echo "Greater than 2!!<br>";
		}elseif($x > 1){
			echo "Greater than 1!!<br>";
		}else{
			echo "Greater than nobody!!";
		}

		$month = 13;
		switch ($month) {
			case 1:
			case 3:
			case 5:
			case 7:
			case 8:
			case 10:
			case 12:
				echo "31 days!<br>";
				break;
			case 4:
			case 6:
			case 9:
			case 11:
				echo "30 days!<br>";
				break;
			case 2:
				echo "28 or 29 days!<br>";
				break;
			default:
				echo "No such month!<br>";
				break;
		}


		$i = 0;
		while($i < 10){
			echo $i, "<br>";
			$i++;
		}

		for($i=0; $i < 10; $i++){
			if($i == 5){
				echo "Skip!!<br>";
				continue;
			}
			echo $i, " in for<br>";
		}

		function avg($a, $b, $c){
			$ag = ($a + $b + $c)/3;
			echo "Averaging!<br>";
			return $ag;
		}

		function val($x){
			if($x > 5){
				echo "Greater than 5!!<br>";
				return;
			}
			if($x > 4){
				echo "Greater than 4!!<br>";
				return;
			}
			if($x > 3){
				echo "Greater than 3!!<br>";
				return;
			}
			if($x > 2){
				echo "Greater than 2!!<br>";
				return;
			}
			if($x > 1){
				echo "Greater than 1!!<br>";
				return;
			}

			echo "Greater than nobody!!<br>";
		}

		$e = avg(1,2,3) + 100;
		echo $e, "<br>";

		val(3);
	?>
</body>
</html>