<?php
//SHORTEN GOOGLE DRIVE FOLDERS INSIDE A FOLDER 
//USING GOOGLE API ,
//IT NEEDS GOOGLE DRIVE PERMISSION AND GOOGLE SHORTEN URL PERMISSION FOR THE APP YOUR ARE USING IT'S KEY .


//READS IT AS A GET REQUEST id=[FOLDER ID]
//shorten_drive.php?id=[FOLDER ID]

header('Content-Type: text/html; charset=utf-8');
$key="YOUR GOOGLE API KEY HERE";


function grab_data($id){
	global $key;
	$url="https://www.googleapis.com/drive/v2/files?q=%27" . $id . "%27+in+parents&key=" . $key;
        $ch = curl_init();

	curl_setopt($ch, CURLOPT_URL,$url);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_BINARYTRANSFER, true);

        $json= curl_exec($ch);
        $json = str_replace('\n',"<br/>",$json);


        $data = json_decode($json,TRUE,JSON_UNESCAPED_UNICODE);
	$items = $data['items'];

	foreach($items as $item){
		$type=$item['mimeType'];
		if(strpos($type, 'folder') !== false){
			$plink=$item['alternateLink'];
			$title=$item['title'];
			$id=$item['id'];
			$short =  shortLnk($plink);
			echo "FOLDER $title : " . $short['id'];
			echo "<br/>";
			grab_data($id);
		}
	}
}


function shortLnk($url){
	global $key;
	$postData = array('longUrl' => $url);
	$curlObj = curl_init();

	$jsonData = json_encode($postData); 
	curl_setopt($curlObj, CURLOPT_URL, 'https://www.googleapis.com/urlshortener/v1/url?key=' . $key);
	curl_setopt($curlObj, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($curlObj, CURLOPT_SSL_VERIFYPEER, 0);
	curl_setopt($curlObj, CURLOPT_HEADER, 0);
	curl_setopt($curlObj, CURLOPT_HTTPHEADER, array('Content-type:application/json'));
	curl_setopt($curlObj, CURLOPT_POST, 1);
	curl_setopt($curlObj, CURLOPT_POSTFIELDS, $jsonData);
 
	$response = curl_exec($curlObj);

//change the response json string to object
	$json = json_decode($response,TRUE,JSON_UNESCAPED_UNICODE);
	curl_close($curlObj);
	return $json;
}

if(isset($_GET['id'])){
        $short = shortLnk('https://drive.google.com/open?id=' . $_GET['id']);
	echo "FOLDER :" . $short['id'];
	echo "<br/>";
	grab_data($_GET['id']);
}else{
	die('gfy');
}


?>
