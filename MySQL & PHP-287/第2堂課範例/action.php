<?php

echo "名字: ", $_GET['user_name'], "<br>";

echo "性別 (raw): ", $_GET['user_gender'], "<br>";
echo "性別: ";
switch($_GET['user_gender']){
	case 'female':
		echo "女";
		break;
	case 'male':
		echo "男";
		break;
	case 'unknown':
		echo "不明";
		break;
	default:
		echo "錯誤! 無此選項!";
		break;
}
echo "<br>";

echo "語言: ";
$dot = '';
foreach($_GET['user_lang'] as $val){
	echo $dot, $val;
	$dot = ', ';
}
echo "<br>";

echo "教育程度: ", $_GET['user_edu'], "<br>";

echo "程式語言: ";
$dot = '';
foreach($_GET['user_promlang'] as $val){
	echo $dot, $val;
	$dot = ', ';
}
echo "<br>";

echo "自傳: <br>";
echo nl2br($_GET['user_bio']), "<br>";

echo "秘密: ", $_GET['user_secret'], "<br>";
echo "隱藏: ", $_GET['user_hidden'], "<br>";

?>