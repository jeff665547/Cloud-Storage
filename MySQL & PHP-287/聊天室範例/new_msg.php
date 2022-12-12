<?php
session_start();

$options = array(
	PDO::ATTR_EMULATE_PREPARES => false, 
	PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION);
$db = new PDO(
	'mysql:host=localhost;dbname=chatroom;charset=utf8', 
	'root', '1234', $options);

$stmt = $db->prepare(
	"INSERT INTO chat_msgs
		(chat_msg_user_id, chat_msg_msg) VALUES
		(:cmuid, :cmm)");
$stmt->execute(
	array(
		":cmuid"=>$_SESSION['chat_user_id'],
		":cmm"=>htmlentities($_POST['msg'])));

echo $_POST['msg'];
?>