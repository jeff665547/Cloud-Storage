<?php include "header.php"; ?>
<?php
if(isset($_SESSION['id'])){
	header("Location: index.php");
	exit;
}
?>
<div class="container">
	<form action="addmember.php" method="POST">
		帳號<input type="text" name="member_account"><br>
		密碼<input type="password" name="member_password"><br>
		再次確認密碼<input type="password" name="member_password_check"><br>
		姓名<input type="text" name="member_name"><br>
		性別<input type="radio" name="member_gender" value="female" checked>女
		<input type="radio" name="member_gender" value="male">男
		<input type="radio" name="member_gender" value="unknown">不明<br>
		出生年
		<select name="member_birth_year">
		<?php
		for($i=1900; $i<=1999; $i++){
		?>
			<option value="<?php echo $i; ?>">
			<?php echo $i; ?>
			</option>
		<?php
		}
		?>
		</select><br>
		出生月
		<select name="member_birth_month">
		<?php
		for($i=1; $i<=12; $i++){
		?>
			<option value="<?php echo $i; ?>">
			<?php echo $i; ?>
			</option>
		<?php
		}
		?>
		</select><br>
		出生日
		<select name="member_birth_date">
		<?php
		for($i=1; $i<=31; $i++){
		?>
			<option value="<?php echo $i; ?>">
			<?php echo $i; ?>
			</option>
		<?php
		}
		?>
		</select><br>
		電話<input type="text" name="member_telephone"><br>
		信箱<input type="text" name="member_email"><br>
		地址<input type="text" name="member_address"><br>
		職業<input type="text" name="member_job"><br>
		資訊<textarea name="member_info"></textarea><br>
		<input type="submit" value="註冊">
	</form>
</div>

<?php include "footer.php"; ?>