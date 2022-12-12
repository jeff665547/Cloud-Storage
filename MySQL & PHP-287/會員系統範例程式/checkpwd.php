<?php session_start() ?>
<?php include "db.ini.php"; ?>
<?php
$account = $_POST['member_account'];
$password = $_POST['member_password'];

$stmt = $db->prepare("SELECT * FROM members WHERE member_account=:macc AND member_active=TRUE");
$stmt->execute(array(':macc' => $account));
if($stmt->rowCount() == 0){
	header("Location: error_msg.php?error_code=4");
	exit;
}
$result = $stmt->fetch(PDO::FETCH_ASSOC);
if(!password_verify($password, $result['member_password_hash'])){
	header("Location: error_msg.php?error_code=4");
	exit;
}

$_SESSION['id'] = $result['member_id'];

header("Location: main.php");
exit();
?>