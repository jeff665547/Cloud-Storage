<?php
$options = array(
	PDO::ATTR_EMULATE_PREPARES => false, 
	PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION);
$db = new PDO(
	'mysql:host=localhost;dbname=MemberManage;charset=utf8', 
	'root', '1234', $options);
?>