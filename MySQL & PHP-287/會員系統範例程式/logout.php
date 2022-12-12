<?php
session_start();
unset($_SESSION['id']);
session_destroy();
setcookie(session_name(),'',time()-100000);
header("Location: index.php");
exit;
?>