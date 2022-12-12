<?php
session_start();
if(!isset($_SESSION['chat_user_id'])){
	header("Location: index.php");
	exit;
}
?>
<!DOCTYPE html>
<html>
<head>
	<title></title>
	<style type="text/css">
		.container{
			width: 450px;
			margin: auto;
		}
		#msg-box{
			border: solid 1px lightgrey;
			padding: 20px;
			height: 400px;
		}
		.msg-input-container{
			margin-top: 20px;
		}
		#msg-input{
			width: 100%;
		}
	</style>
</head>
<body>
	<div class="container">
		<div id="msg-box"></div>
		<div class="msg-input-container">
			<textarea id="msg-input"></textarea>
		</div>
	</div>

	<script type="text/javascript">
		var msg_box = document.getElementById('msg-box'),
			msg_input = document.getElementById('msg-input');

		msg_input.addEventListener('keydown', function(e){
			if(e.keyCode != 13) return;

			var xhr = new XMLHttpRequest();
			xhr.onreadystatechange = function(){
				if(xhr.readyState == 4){
					console.log(xhr.responseText);
				}
			};
			xhr.open("POST", "/chatroom/new_msg.php", true);
			
			var fd = new FormData();
			fd.set('msg', msg_input.value);
			
			xhr.send(fd);

			msg_input.value = '';
		});

		setInterval(function(){
			var xhr = new XMLHttpRequest();
			xhr.onreadystatechange = function(){
				if(xhr.readyState == 4 && xhr.status == 200){
					console.log(xhr.responseText);
					var msgs = JSON.parse(xhr.responseText);
					for(var i=0; i<msgs.length; i++){
						var msg = msgs[i];
						msg_box.innerHTML += 
							"<div>"
							+ msg['chat_user_name'] + ' : '
							+ msg['chat_msg_msg'] + ' --- '
							+ msg['chat_msg_time']
							+ "</div>";
					}
				}
			};
			xhr.open("GET", "/chatroom/update_msgs.php", true);
			xhr.send();
		}, 1000);

	</script>
</body>
</html>