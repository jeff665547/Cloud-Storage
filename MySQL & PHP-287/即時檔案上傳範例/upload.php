<?php

$file_num = count($_FILES['files']['name']);

for($i=0; $i<$file_num; $i++){
	$tmp_name = $_FILES['files']['tmp_name'][$i];
	$file_name_parts = explode('.', $_FILES['files']['name'][$i]);
	$file_type = $file_name_parts[count($file_name_parts)-1];
	$new_file_name = floor(microtime(true)*1000);
	if(!move_uploaded_file($tmp_name, "img/{$new_file_name}.{$file_type}")){
		echo '檔案上傳失敗!';
		exit;
	}
}
echo '檔案上傳成功!';

?>