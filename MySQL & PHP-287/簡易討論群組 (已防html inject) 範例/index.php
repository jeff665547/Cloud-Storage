<?php
if( isset($_GET['page_num']) ){
	$page_num = $_GET['page_num'];
}else{
	$page_num = 0;
}
$post_per_page = 2;
$options = array(
	PDO::ATTR_EMULATE_PREPARES => false, 
	PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION);
$db = new PDO('mysql:host=localhost:3306;dbname=forum;charset=utf8',
	'root', '1234', $options);
$stmt = $db->prepare("SELECT * from post WHERE post_type=TRUE ORDER BY post_id DESC LIMIT :start, :length");
$stmt->execute(array(
		':start' => $post_per_page*$page_num,
		':length' => $post_per_page
	));
$posts = $stmt->fetchAll(PDO::FETCH_ASSOC);
?>
<!DOCTYPE html>
<html>
<head>
	<title></title>
	<style type="text/css">
		html, body{
			margin: 0;
			padding: 0;
		}
		.container{
			width: 500px;
			margin: auto;
		}
		.post-group{
			border: 1px lightgrey solid;
			padding: 30px;
		}
		.post{
			border-bottom: 1px lightgrey solid;
		}
		.page-numbers{
			text-align: center;
		}
	</style>
</head>
<body>
	<div class="container">
		<?php
		foreach($posts as $post){
		?>

		<div class="post-group">
			<div class="post">
			主題：<?php echo htmlspecialchars($post['post_topic'],ENT_QUOTES); ?><br>
			作者：<?php echo htmlspecialchars($post['post_author'], ENT_QUOTES); ?><br>
			時間：<?php echo $post['post_time']; ?><br>
			內文：<br>
			<?php echo nl2br(htmlspecialchars($post['post_content'],ENT_QUOTES)); ?>
			</div>

			<?php
			$stmt = $db->prepare("SELECT * FROM post WHERE reply_to_post_id=:rpid AND post_type=:ptype ORDER BY post_id ASC");
			$stmt->execute(
				array(
					':rpid' => $post['post_id'],
					':ptype' => False));
			$replies = $stmt->fetchAll(PDO::FETCH_ASSOC);
			foreach($replies as $reply){
			?>
			<div class="post">
				主題：<?php echo htmlspecialchars($reply['post_topic'], ENT_QUOTES); ?><br>
				作者：<?php echo htmlspecialchars($reply['post_author'], ENT_QUOTES); ?><br>
				時間：<?php echo $reply['post_time']; ?><br>
				內文：<br>
				<?php echo nl2br(htmlspecialchars($reply['post_content'], ENT_QUOTES)); ?>
			</div>
			<?php
			}
			?>

			<form action="post.php" method="POST">
				暱稱：<input type="text" name="post_author"><br>
				標題：<input type="text" name="post_topic"><br>
				內文：<br>
				<textarea name="post_content"></textarea>
				<input type="hidden" name="reply_to_post_id" value="<?php echo $post['post_id']; ?>">
				<input type="submit" value="PO文">
			</form>
		</div>
		<?php
		}
		?>

		<form action="post.php" method="POST">
			暱稱：<input type="text" name="post_author"><br>
			標題：<input type="text" name="post_topic"><br>
			內文：<br>
			<textarea name="post_content"></textarea>
			<input type="submit" value="PO文">
		</form>

		<div class="page-numbers">
		<?php
		$stmt = $db->query("SELECT * FROM post WHERE post_type=TRUE");
		$rcount = $stmt->rowCount();
		$total_page_num = ceil($rcount / $post_per_page);
		for($i=0; $i<$total_page_num; $i++){
			if($i != $page_num){
				echo "<a href=\"index.php?page_num=$i\">", $i+1,"</a>\n";
			}else{
				echo $i+1, "\n";
			}
		}
		?>
		</div>
	</div>
</body>
</html>