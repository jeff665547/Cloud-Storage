<?php

$options = array(
	PDO::ATTR_EMULATE_PREPARES => false, 
	PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION);
$db = new PDO(
		'mysql:host=localhost;dbname=students;charset=utf8', 
		'root', '1234', $options);

// foreach($db->query("SELECT * FROM grade") as $row){
// 	echo $row['no'].' '.$row['name'].' '.$row['chinese'].' '.$row['math'].' '.$row['nature']."<br>";
// }

$stmt = $db->query("SELECT * FROM grade");
// while($row = $stmt->fetch(PDO::FETCH_ASSOC)){
// 	echo $row['no'].' '.$row['name'].' '.$row['chinese'].' '.$row['math'].' '.$row['nature']."<br>";
// }

$results = $stmt->fetchAll(PDO::FETCH_ASSOC);

var_dump($results);


?>