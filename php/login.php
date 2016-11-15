<?php
    $result = validateLogin();
	print $result;
	function validateLogin(){
			$email = $_GET["email"];
			$password = $_GET["password"];
			if(($username=="sarahwatson@gmail.com" && $password=="sarah")){
					session_start();
					$_SESSION['firstname'] = 'Sarah';
					$_SESSION['lastname'] = 'Watson';
					return 'true';
			}
			else{
				return 'false';
			}
	}
?>