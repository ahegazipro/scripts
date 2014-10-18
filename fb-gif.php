<?php

//Created by Ahmad Hegazy <ahegazipro@gmail.com>

if (isset($_POST['submit'])){
	if ($_POST['pic'] == ""){
		$msg= "Please Enter Pictue Url";
		header("Location: " . "fb-pic.php?msg=$msg");
		exit ;
	}else{
		$pic = $_POST['pic'];
		if (filter_var($pic, FILTER_VALIDATE_URL) === FALSE) {
			$msg= "Please Enter a vaild picture link";
			header("Location: " . "fb-pic.php?msg=$msg");
			exit ;
		}
	
	}
	if (!$_POST['link'] == ""){
		$link=$_POST['link'];
		if (filter_var($link, FILTER_VALIDATE_URL) === FALSE) {
			$msg= "Please Enter a vaild link";
			header("Location: " . "fb-pic.php?msg=$msg");
			exit ;
		}
	}else {
		$link="http://facebook.com/ahegazipro";
	}
	
	$description=isset($_POST['description'])? $_POST['description'] : "";
	$name=isset($_POST['name'])? $_POST['name'] : "";
	$link=isset($_POST['link'])? $_POST['link'] : "https://www.fb.com/ahegazipro";
	$full_link="https://www.facebook.com/dialog/feed?app_id=1500924446822247&link=$link&name=$name&caption=$description&description=http://fb.com/ahegazipro&picture=$pic&source=http://www.youtube.com/v/Tv0y63FinJw?version=3&autohide=1&showinfo=1&autohide=1&autoplay=1&feature=share&attribution_tag=dWryXJNxHac&ref=share&redirect_uri=https://www.twitter.com/ahegazipro";
//&to=$page_id&from=$page_id
	
	$html="<a href=\"$full_link\" target=\"_blank\" >press here</a> <br/> <a href=\"fb-pic.php\">Share another picture<a/>";
	echo $html;
}else{

$msg =isset($_GET['msg']) ? $_GET['msg'] : "";
$msg .=  "<br>Fields with * are Mandatory";
?>

<html>
<head><title>FACEBOOK GIF Sharer ..</title> </head>
<body>
<p style="color:red"><?php echo strip_tags($msg,'<center> <br>');?></p>

Please fill the following form<br>
<form action="fb-pic.php" method="post">


Name: <input type="text" name="name"><br>
Description: <input type="text" name="description"><br>
Picture Link : <input type="text" name="pic" value="https://www.facebook.com/303067703214825"><br>
Link : <input type="text" name="link"><br>

<input type="submit" name="submit" value="submit">

</form>

<br><br><br><center>Created by <a href="http://facebook.com/ahegazipro">Ahmad Hegazy</a> MailME: <a href="mailto:ahegazipro@gmail.com">ahegazipro@gmail.com</a></center>

</body>
</html>

<?php
}

?>
