<?php
function gen_password($pwd_len){
	$password_char = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
	$new_password = '';
	for($i=0; $i<$pwd_len; $i++){
		$char_key = rand(0, strlen($password_char)-1);
		$new_password .= $password_char[$char_key];
	}
	return $new_password;
}

$account = $_POST['member_account'];
$email = $_POST['member_email'];
if(!isset($account) && !isset($email)){
	header("Location: error_msg.php?error_code=5");
	exit;
}
?>
<?php include "db.ini.php"; ?>
<?php
if(isset($account)){
	$stmt = $db->prepare("SELECT * FROM members WHERE member_account=:macc");
	$stmt->execute(array(":macc"=>$account));
}elseif(isset($email)){
	$stmt = $db->prepare("SELECT * FROM members WHERE member_email=:memail");
	$stmt->execute(array(":memail"=>$email));
}
$results = $stmt->fetchAll(PDO::FETCH_ASSOC);
if(count($results) == 0){
	header("Location: error_msg.php?error_code=5");
	exit;
}

$result = $results[0];
$new_password = gen_password(10);
$new_password_hash = password_hash($new_password, PASSWORD_DEFAULT);
$stmt = $db->prepare("UPDATE members SET member_password_hash=:mph WHERE member_id=:mid");
$stmt->execute(array(
		':mph' => $new_password_hash,
		':mid' => $result['member_id']
	));

$content="帳號: ".$result['member_account']." 新密碼: ".$new_password;
mail($result["member_email"], "新密碼", $content);

header("Location: index.php");
exit;

?>