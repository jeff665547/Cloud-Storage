<?php include "header.php"; ?>
<?php 
if(!isset($_SESSION['id'])){
	header("Location: index.php");
	exit;
}
?>
<?php include "db.ini.php"; ?>
<?php
$stmt = $db->prepare("SELECT * FROM members WHERE member_id=:mid");
$stmt->execute(array(':mid'=>$_SESSION['id']));
$result = $stmt->fetch(PDO::FETCH_ASSOC);
?>

<div class="container">
	<a href="logout.php">登出</a> - 
	<a href="delete.php">刪除</a>
	<form action="update.php" method="POST">
		帳號：<?php echo $result['member_account']; ?><br>
		密碼<input type="password" name="member_password"><br>
		再次確認密碼<input type="password" name="member_password_check"><br>
		姓名<input type="text" name="member_name" value="<?php echo $result['member_name']; ?>"><br>
		性別<input type="radio" name="member_gender" value="female" <?php if($result['member_gender']==1) echo "checked"; ?>>女
		<input type="radio" name="member_gender" value="male" <?php if($result['member_gender']==2) echo "checked"; ?>>男
		<input type="radio" name="member_gender" value="unknown" <?php if($result['member_gender']==3) echo "checked"; ?>>不明<br>
		出生年
		<select name="member_birth_year">
		<?php
		for($i=1900; $i<=1999; $i++){
		?>
			<option value="<?php echo $i; ?>" <?php if($i==$result['member_birth_year']) echo 'selected'; ?>>
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
			<option value="<?php echo $i; ?>" <?php if($i==$result['member_birth_month']) echo 'selected'; ?>>
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
			<option value="<?php echo $i; ?>" <?php if($i==$result['member_birth_date']) echo 'selected'; ?>>
			<?php echo $i; ?>
			</option>
		<?php
		}
		?>
		</select><br>
		電話<input type="text" name="member_telephone" value="<?php echo $result['member_telephone']; ?>"><br>
		地址<input type="text" name="member_address" value="<?php echo $result['member_address']; ?>"><br>
		職業<input type="text" name="member_job" value="<?php echo $result['member_job']; ?>"><br>
		資訊<textarea name="member_info"><?php echo $result['member_info']; ?></textarea><br>
		<input type="submit" value="更新">
	</form>
</div>

<?php include "footer.php"; ?>