<?php

//Created by Ahmad Hegazy <ahegazipro@gmail.com>
//Get more scripts from my scripts repository : https://github.com/ahegazipro/scripts

$output="";
if (!empty($_POST['link'])){

	$link=$_POST['link'];
	$uname=(null != strtok(strrchr( $link , '/' ),"?") ? strtok(strrchr( $link , '/' ),"?") : $link);

        $url="https://graph.facebook.com/" . $uname;
	function is_exsit($url){

		$h=get_headers($url);
		$header=substr($h['0'], 9, 3);

		if ($header !== '200'){
			return false;
		}else{
			$fb_json=file_get_contents($url);
			$arr=json_decode($fb_json,true);
			$arr['pp'] = $url . "/picture";
			return $arr;

		}
	}

	function get_html($arr){
		if($arr == false){
			$html="USER HAS DEACTIVATED HIS ACCOUNT , OR NOT EXSIT.";
			return $html;
		}else{

			if(isset($arr['likes'])){
				$html = "PLEASE ENTER USER NOT PAGE";
				return $html;
			}

			$html = "USER: " . $arr['first_name'] . " " . $arr['last_name'];
			$html .= "<br/>IS EXSITED AND BLOCKED YOU.<br/>";
			$pic = '<br/><img src="' . $arr['pp'] . '"></src>';
			$html .= "<br/>HIS PP : " . $pic ;
			return $html;
		}
	}

        $arr = is_exsit($url);
        $output=get_html($arr);

}

	echo "<html><head><meta charset=\"UTF-8\"><title>AM I BLOCKED</title></head><body><center>";
	echo $output;
?>
	<br>
	<br>
	<h>CHECK IF YOUR FRIEND BLOCKED YOU OR CLOSED/DEACTIVATED HIS ACCOUNT.<br>JUST ENTER HIS USERNAME OR PROFILE URL OR MESSAGE URL.</h>
	<br>
	<br>
	<form action="fb-block.php" method="POST">
		USERNAME OR ID:<br>
		<br>
		<input type="text" name="link">
		<input type="submit" value="Submit">
	</form>
</center></body></html>
