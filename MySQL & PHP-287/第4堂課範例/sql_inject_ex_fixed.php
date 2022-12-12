<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title></title>
</head>
<body>
	<?php

		if( isset($_POST['hidden']) ){

			$db_options = array(PDO::ATTR_EMULATE_PREPARES => false, PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION);

			$db = new PDO('mysql:host=localhost;dbname=students;charset=utf8', 'root', '1234', $db_options);

			// $stmt = $db->query("SELECT * FROM grade WHERE name='{$_POST['user']}' AND no='{$_POST['pwd']}'");

			$stmt = $db->prepare("SELECT * FROM grade WHERE name=:name AND no=:no");
			$stmt->execute(array(
					':no' => $_POST['pwd'],
					':name' => $_POST['user']
				));

			if( !$stmt->rowCount() ){
				echo "密碼錯誤或帳號不存在!<br>";
			}
			else{
				foreach($stmt as $row)
					echo "{$row['name']} {$row['no']} {$row['chinese']} {$row['math']} {$row['nature']}<br>";
			}

		}
		else{

	?>
		<form method="POST" action="sql_inject_ex.php">
			姓名：<input name="user" type="text"><br>
			密碼：<input name="pwd" type="password"><br>
			<input name="hidden" type="hidden" value="hidden">
			<input value="Login" type="submit">
		</form>

	<?php

		}

	?>
</body>
</html>