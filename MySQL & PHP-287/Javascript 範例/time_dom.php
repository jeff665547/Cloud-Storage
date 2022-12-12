<!DOCTYPE html>
<html>
<head>
	<title></title>
</head>
<body>

<div id="display"></div>

<script type="text/javascript">
	var d = document.getElementById('display');
	var t = new Date();
	d.innerHTML = t;
	setInterval(function(){
		var t = new Date();
		d.innerHTML = t;
	}, 1000);
</script>
</body>
</html>