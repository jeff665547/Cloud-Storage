<?php

setcookie("cook1[0]", "a");
setcookie("cook1[1]", "b");
setcookie("cook1[abc]", "c");

echo $_COOKIE['cook1'][0], "<br>";
echo $_COOKIE['cook1'][1], "<br>";
echo $_COOKIE['cook1']['abc'], "<br>";


?>