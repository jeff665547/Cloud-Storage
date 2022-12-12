<?php
session_start();
if(isset($_SESSION['chat_user_id'])){
	header("Location: room.php");
	exit;
}

$user_name = htmlentities($_POST['chat_user_name'], ENT_QUOT);

if(!isset($user_name) || $user_name == ''){
	header("Location: index.php?error_code=1");
	exit;
}
if(strlen($user_name) > 14){
	header("Location: index.php?error_code=3");
	exit;
}

$options = array(
	PDO::ATTR_EMULATE_PREPARES => false, 
	PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION);
$db = new PDO(
	'mysql:host=localhost;dbname=chatroom;charset=utf8', 
	'root', '1234', $options);

$stmt = $db->prepare("SELECT * FROM chat_users WHERE chat_user_name=:cuname");
$stmt->execute(array(':cuname'=>$user_name));

if($stmt->rowCount() > 0){
	header("Location: index.php?error_code=2");
	exit;
}

$stmt = $db->prepare("INSERT INTO chat_users (chat_user_name) VALUES (:cuname)");
$stmt->execute(array(':cuname'=>$user_name));

$stmt = $db->prepare("SELECT * FROM chat_users WHERE chat_user_name=:cuname");
$stmt->execute(array(':cuname'=>$user_name));
$user = $stmt->fetch(PDO::FETCH_ASSOC);

$_SESSION['chat_user_id'] = $user['chat_user_id'];
$_SESSION['newest_msg_id'] = 0;

header("Location: room.php");
exit;
?>