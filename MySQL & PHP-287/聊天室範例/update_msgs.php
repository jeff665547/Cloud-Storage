<?php
session_start();

$options = array(
	PDO::ATTR_EMULATE_PREPARES => false, 
	PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION);
$db = new PDO(
	'mysql:host=localhost;dbname=chatroom;charset=utf8', 
	'root', '1234', $options);

$stmt = $db->prepare("SELECT * FROM chat_msgs WHERE chat_msg_id > :cmid ORDER BY chat_msg_id ASC");
$stmt->execute(array(":cmid"=>$_SESSION['newest_msg_id']));

$results = $stmt->fetchAll(PDO::FETCH_ASSOC);

if(count($results) > 0){
	$last_result = $results[count($results)-1];
	$_SESSION['newest_msg_id'] = $last_result['chat_msg_id'];
}

$stmt = $db->prepare("SELECT * FROM chat_users");
$stmt->execute();
$users = $stmt->fetchAll(PDO::FETCH_ASSOC);

$user_id_to_name = array();
foreach($users as $user){
	$user_id_to_name[$user['chat_user_id']] = $user['chat_user_name'];
}

for($i=0; $i<count($results); $i++){
	$results[$i]['chat_user_name'] = $user_id_to_name[$results[$i]['chat_msg_user_id']];
}


echo json_encode($results);

?>