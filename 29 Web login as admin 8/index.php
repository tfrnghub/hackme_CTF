<?php
require('config.php');
require('session.php');

// class Session { ... }

// sorry, no source code this time. :P

$session = Session::load();
$login_failed = false;

if($_GET['show_source'] === '1') {
    highlight_file(__FILE__);
    exit;
}

if($_GET['debug'] === '1') {
    $session->debug();
}

if(isset($_POST['name'])) {
    $login_failed = !Session::login($_POST['name'], $_POST['password']);
} else if(isset($_POST['logout'])) {
    $session = new Session();
}