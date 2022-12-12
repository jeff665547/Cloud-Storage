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


$stmt = $db->query("SELECT * FROM grade WHERE 1");
echo $stmt->rowCount(), " rows.<br>";

// $rowCount = $db->exec("
// 	INSERT INTO grade (`no`,name,chinese,math,nature) 
// 	VALUES
// 	('A1000008','Harry',19,20,21),
// 	('A1000009','Mike',22,23,24)");

// echo $rowCount, " modified row(s).<br>";

$stmt = $db->prepare("
	INSERT INTO grade (`no`,name,chinese,math,nature)
	VALUES (:no,:name,:chinese,:math,:nature)");

$stmt->bindParam(':no', $no);
$stmt->bindParam(':name', $name);
$stmt->bindParam(':math', $math);
$stmt->bindParam(':chinese', $chinese);
$stmt->bindParam(':nature', $nature);

$rows = array(
		array('A1000010','a',10,11,12),
		array('A1000011','b',13,17,21),
		array('A1000012','c',14,18,22),
		array('A1000013','d',15,19,23),
		array('A1000014','e',16,20,24)
	);
foreach($rows as $row){
	$no = $row[0]; $name = $row[1]; $chinese = $row[2]; $math = $row[3]; $nature = $row[4];
	$stmt->execute();
}

?>