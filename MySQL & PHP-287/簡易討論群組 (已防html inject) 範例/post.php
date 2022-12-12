<?php
$post_author = $_POST['post_author'];
$post_topic = $_POST['post_topic'];
$post_content = $_POST['post_content'];

// echo $post_author, '<br>';
// echo $post_topic, '<br>';
// echo $post_content, '<br>';

if($post_author=='' || $post_topic == '' || $post_content==''){
	header("Location: error_msg.php?error_code=1");
	exit;
}

$options = array(
	PDO::ATTR_EMULATE_PREPARES => false, 
	PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION);
$db = new PDO('mysql:host=localhost:3306;dbname=forum;charset=utf8',
	'root', '1234', $options);

if(!isset($_POST['reply_to_post_id'])){
	$stmt = $db->prepare(
		"INSERT INTO post (post_author, post_topic, post_content, post_type) VALUES
			(:pauthor, :ptopic, :pcontent, :ptype)");
	$stmt->execute(
		array(
			':pauthor' => $post_author,
			':ptopic' => $post_topic,
			':pcontent' => $post_content,
			':ptype' => TRUE
			));
}else{
	$stmt = $db->prepare(
		"INSERT INTO post (post_author, post_topic, post_content, post_type, reply_to_post_id) VALUES
			(:pauthor, :ptopic, :pcontent, :ptype, :rpid)");
	$stmt->execute(
		array(
			':pauthor' => $post_author,
			':ptopic' => $post_topic,
			':pcontent' => $post_content,
			':ptype' => False,
			':rpid' => $_POST['reply_to_post_id']
			));
}

header('Location: index.php');
?>