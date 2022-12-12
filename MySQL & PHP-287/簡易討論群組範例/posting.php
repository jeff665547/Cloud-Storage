<?php

$options = array(
	PDO::ATTR_EMULATE_PREPARES => false, 
	PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION);
$db = new PDO(
		'mysql:host=localhost;dbname=naiive_forum;charset=utf8', 
		'root', '1234', $options);

$title = $_POST['post_title'];
$author = $_POST['post_author'];
$content = $_POST['post_content'];
$reply_id = $_POST['post_reply_id'];

if(!isset($reply_id)){

	$stmt = $db->prepare("INSERT INTO posts (post_title, post_author, post_content)
		VALUES (:title, :author, :content)");
	$stmt->execute(array(
			':title' => $title,
			':author' => $author,
			':content' => $content));

}
else{
	$stmt = $db->prepare("INSERT INTO posts (post_author, post_content, post_reply_id, post_reply)
		VALUES (:author, :content, :reply_id, :reply)");
	$stmt->execute(array(
			':author' => $author,
			':content' => $content,
			':reply_id' => $reply_id,
			':reply' => true));

}

header("Location: index.php");


?>