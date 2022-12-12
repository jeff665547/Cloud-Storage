<?php

$options = array(
	PDO::ATTR_EMULATE_PREPARES => false, 
	PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION);
$db = new PDO(
		'mysql:host=localhost;dbname=naiive_forum;charset=utf8', 
		'root', '1234', $options);

if(!isset($_GET['page'])){
	$current_page = 0;
}else{
	$current_page = $_GET['page'];
}

?>
<!DOCTYPE html>
<html>
<head>
	<title></title>
	<style type="text/css">
		body, html{
			margin: 0;
			padding: 0;
			min-height: 100%;
		}
		.box {
			width: 550px;
			margin: auto;
			padding: 10px;
			min-height: 100%;
			border-left: 1px solid lightgrey;
			border-right: 1px solid lightgrey;
		}
		.post_group{
			padding: 20px;
			margin: 20px 10px;
			border: 1px solid lightgrey;
		}
		.post{
			padding-bottom: 15px;
			margin-bottom: 15px;
			border-bottom: 1px solid lightgrey;
		}
	</style>
</head>
<body>
	
	<div class="box">
		<form method="POST" action="posting.php">
			標題: <input type="text" name="post_title"><br>
			暱稱: <input type="text" name="post_author"><br>
			內文: <br>
			<textarea name="post_content"></textarea><br>
			<input type="submit" value="PO文">
		</form>

		<div>
		<?php
		$stmt = $db->query("SELECT * FROM posts WHERE NOT post_reply");
		$row_num = $stmt->rowCount();
		$page_row_num = 2;
		$page_num = ceil($row_num / $page_row_num);
		for($i=0; $i<$page_num; $i++){
			if($i==$current_page){
				echo $i+1, " ";
			}else{
				echo "<a href='index.php?page=$i'>", $i+1, "</a> ";
			}
		}
		?>
		</div>

		<?php

		$row_start = $current_page * $page_row_num;

		$stmt = $db->prepare("SELECT * FROM posts WHERE NOT post_reply ORDER BY post_time DESC LIMIT :start, :num");
		$stmt->execute(array(':start' => $row_start, ':num' => $page_row_num));

		foreach($stmt as $row){
		?>

		<div class="post_group">
			<div class="post">
				主題: <?php echo $row['post_title']; ?><br>
				作者: <?php echo $row['post_author']; ?><br>
				時間: <?php echo $row['post_time']; ?><br>
				<br>
				<?php echo nl2br($row['post_content']); ?><br>
			</div>
			<?php
			$stmt2 = $db->prepare("SELECT * FROM posts WHERE post_reply AND post_reply_id=:prid ORDER BY post_time ASC");
			$stmt2->execute(array(':prid' => $row['post_id']));
			foreach($stmt2 as $row2){
			?>
			<div class="post">
				作者: <?php echo $row2['post_author']; ?><br>
				時間: <?php echo $row2['post_time']; ?><br>
				<br>
				<?php echo nl2br($row2['post_content']); ?><br>
			</div>
			<?php } ?>
			<form method="POST" action="posting.php">
				暱稱: <input type="text" name="post_author"><br>
				內文: <br>
				<textarea name="post_content"></textarea>
				<input type="hidden" name="post_reply_id" value="<?php echo $row['post_id']; ?>"><br>
				<input type="submit" value="PO文">
			</form>
		</div>
		<?php } ?>
	</div>

</body>
</html>