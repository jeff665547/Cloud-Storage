<?php
session_start();
if(!isset($_SESSION['id']) || !isset($_POST['member_name'])){
	header('Location: index.php');
	exit;
}
?>
<?php include "db.ini.php"; ?>
<?php
$password = $_POST['member_password'];
$password_check = $_POST['member_password_check'];
$name = $_POST['member_name'];
$gender = $_POST['member_gender'];
$birth_year = $_POST['member_birth_year'];
$birth_month = $_POST['member_birth_month'];
$birth_date = $_POST['member_birth_date'];
$telephone = $_POST['member_telephone'];
$address = $_POST['member_address'];
$job = $_POST['member_job'];
$info = $_POST['member_info'];

if(isset($password)){
	if($password != $password_check){
		header("Location: error_msg.php?error_code=2");
		exit;
	}
	$password_hash = password_hash($password, PASSWORD_DEFAULT);
	$stmt = $db->prepare("UPDATE `members` SET `member_password_hash`=:mpwd WHERE member_id=:mid");
	$stmt->execute(array(
		':mpwd' => $password_hash,
		':mid' => $_SESSION['id']));
}

$stmt = $db->prepare("UPDATE `members`
	SET
	`member_name`=:mname,
	`member_birth_year`=:mbyear,
	`member_birth_month`=:mbmonth,
	`member_birth_date`=:mbdate,
	`member_telephone`=:mtele,
	`member_address`=:maddr,
	`member_info`=:minfo,
	`member_gender`=:mgender,
	`member_job`=:mjob WHERE member_id=:mid");
$stmt->execute(array(
		':mname' => $name,
		':mbyear' => $birth_year,
		':mbmonth' => $birth_month,
		':mbdate' => $birth_date,
		':mtele' => $telephone,
		':maddr' => $address,
		':minfo' => $info,
		':mjob' => $job,
		':mgender' => $gender,
		':mid' => $_SESSION['id']
	));

header("Location: main.php");
exit;
?>