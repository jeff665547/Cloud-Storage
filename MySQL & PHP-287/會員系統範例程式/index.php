<?php include "header.php"; ?>
<?php 
if(isset($_SESSION['id'])){
	header("Location: main.php");
	exit;
}
?><div class="login-container">
	<div class="login-box">
		<form action="checkpwd.php" method="POST">
			<div>帳號</div>
			<div><input type="text" name="member_account"></div>
			<div>密碼</div>
			<div><input type="password" name="member_password"></div>
			<div><input type="submit" value="登入"></div>
		</form>
	</div>
	<div>
		<a href="join.php">註冊</a> - 
		<a href="forget_pwd.php">忘記密碼</a>
	</div>
</div>

<?php include "footer.php"; ?>