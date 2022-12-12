<?php include "db.ini.php"; ?>

<?php
$account = $_POST['member_account'];
$password = $_POST['member_password'];
$password_check = $_POST['member_password_check'];
$name = $_POST['member_name'];
$gender = $_POST['member_gender'];
$birth_year = $_POST['member_birth_year'];
$birth_month = $_POST['member_birth_month'];
$birth_date = $_POST['member_birth_date'];
$telephone = $_POST['member_telephone'];
$email = $_POST['member_email'];
$address = $_POST['member_address'];
$job = $_POST['member_job'];
$info = $_POST['member_info'];

$stmt = $db->prepare("SELECT * FROM members WHERE member_account=:maccount");
$stmt->execute(array(":maccount"=>$account));
if($stmt->rowCount() > 0){
	header("Location: error_msg.php?error_code=1");
	exit();
}

if($password != $password_check){
	header("Location: error_msg.php?error_code=2");
	exit();
}
$date_error = False;
switch($birth_month){
	case 4: case 6: case 9: case 11:
		if($birth_date > 30) $date_error = True;
		break;
	case 2:
		if((!(($birth_year%4==0 && $birth_year%100!=0) || $birth_year%400==0) && $birth_date==29) || $birth_date>=30) $date_error = True;
		break;
	default:
		break;
}
if($birth_date > 31 || $birth_date < 0) $date_error = True;
if($date_error){
	header("Location: error_msg.php?error_code=3");
	exit();
}

switch($gender){
	case 'female':
		$gender = 1;
		break;
	case 'male':
		$gender = 2;
		break;
	default:
		$gender = 3;
		break;
}

$stmt = $db->prepare(
	"INSERT INTO `members`(`member_account`, `member_password_hash`, `member_name`, `member_birth_year`, `member_birth_month`, `member_birth_date`, `member_telephone`, `member_address`, `member_info`, `member_gender`, `member_job`, `member_email`)
	VALUES (:macc, :mpwd, :mname, :mbyear, :mbmonth, :mbdate, :mtele, :maddr, :minfo, :mgender, :mjob, :memail)
	");
$stmt->execute(array(
		':macc' => $account,
		':mpwd' => password_hash($password, PASSWORD_DEFAULT),
		':mname' => $name,
		':mbyear' => $birth_year,
		':mbmonth' => $birth_month,
		':mbdate' => $birth_date,
		':mtele' => $telephone,
		':maddr' => $address,
		':minfo' => $info,
		':mjob' => $job,
		':mgender' => $gender,
		':memail' => $email
	));

header("Location: index.php");
exit;
?>