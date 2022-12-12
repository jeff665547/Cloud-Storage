<?php
session_start();
?>
<?php include "db.ini.php"; ?>
<?php
$stmt = $db->prepare("UPDATE members SET member_active=:mact WHERE member_id=:mid");
$stmt->execute(array(
		":mact" => False,
		":mid" => $_SESSION['id']
	));

unset($_SESSION['id']);
session_destroy();
setcookie(session_name(),'',time()-100000);
header("Location: index.php");
exit;
?>