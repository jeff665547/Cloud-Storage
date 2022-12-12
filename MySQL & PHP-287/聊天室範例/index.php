<?php
session_start();
if(isset($_SESSION['chat_user_id'])){
	header("Location: room.php");
	exit;
}
?>
<!DOCTYPE html>
<html>
<head>
	<title></title>
	<style type="text/css">
		.container{
			width: 250px;
			margin: auto;
		}
		.box{
			padding: 20px;
			border: lightgrey 1px solid;
		}
		.error-msg{
			text-align: center;
			color: red;
		}
	</style>
</head>
<body>
	<div class="container">
		<div class="box">
			<form action="join.php" method="POST">
				<input type="text" name="chat_user_name"><br>
				<input type="submit" value="加入">
			</form>
		</div>
		<?php if(isset($_GET['error_code'])){?>
		<?php if($_GET['error_code']==1){ ?>
		<div class="error-msg">暱稱不可為空!!</div>
		<?php }elseif($_GET['error_code']==2){ ?>
		<div class="error-msg">暱稱已被使用!!</div>
		<?php }elseif($_GET['error_code']==3){ ?>
		<div class="error-msg">暱稱過長!!</div>
		<?php }} ?>
	</div>
</body>
</html>