<?php
$error_code = $_GET['error_code'];
if($error_code == 1){
	echo "帳號已被註冊!<br>";
}elseif($error_code == 2){
	echo "重複輸入密碼不合!<br>";
}elseif($error_code == 3){
	echo "出生年月日不合理!<br>";
}elseif($error_code==4){
	echo "帳號密碼不符!<br>";
}elseif($error_code==5){
	echo "帳號或信箱不存在!<br>";
}
?>
<a href="index.php">返回首頁</a>