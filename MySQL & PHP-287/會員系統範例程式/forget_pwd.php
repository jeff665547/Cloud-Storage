<?php include "header.php"; ?>

<?php
if(isset($_SESSION['id'])){
	header("Location: main.php");
	exit;
}
?>

<div class="container">
	<form method="POST" action="send_pwd.php">
		帳號<input type="text" name="member_account"><br>
		信箱<input type="text" name="member_email">
		<input type="submit" value="送出">
	</form>
</div>


<?php include "footer.php"; ?>