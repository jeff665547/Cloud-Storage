<?php

if( !isset($_GET['error_code']) ){
	header('Location: index.php');
	exit;
}

$error_code = $_GET['error_code'];

if($error_code == 1){
?>

請填寫所有欄位!!<br>
<a href="index.php">返回</a>

<?php
?
?>