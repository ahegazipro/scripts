<?php
header('Content-Type: text/html; charset=UTF-8');

$langs = array( "fr" => "French","es" => "Spanish", "af" => "Afrikans", "hy" => "Armenian", "az" => "Azerbaijani", "eu" => "Basque", "be" => "Balarusian",
         "ca" => "Catalan", "zh-CN" => "Chinese(Simplified)", "zh-TW" => "Chineses(Traditional", "hr" => "Croatin", "cs" => "Czesh", "da" => "Danish", "nl" => "Dutch",
         "et" => "Estonian", "tl" => "Filipino", "fi" => "Finnish", "gl" => "Galician", "ka" => "Georgian", "de" => "German", "el" => "Greek", "iw" => "Hebrew",
         "hi" => "Hindi", "hu" => "Hungarian", "is" => "Icelandic", "id" => "Indonesian", "it" => "Italian", "ja" => "Japanese", "kn" => "Kannada",
         "km" => "Khamer", "ko" => "Korean", "lv" => "Latvian", "lt" => "Lithuanian", "mk" => "Macedonian", "ms" => "Malay", "ml" => "Malayalam", "mr" => "Marathi",
         "mn" => "Mongolian", "ne" => "Nepali", "no" => "Norwegian", "fa" => "Parsian", "pl" => "Polish", "pt" => "Portuguese", "ro" => "Romanian",  "ru" => "Russian",
         "sr" => "Serbian", "si" => "Sinhala", "sk" => "Slovak", "sl" => "Slovenian", "sw" => "Swahili", "sv" => "Swedish", "ta" => "Tamil", "te" => "Telugu", "th" => "Thai",
         "tr" => "Turkish", "uk" => "Ukranian", "vi" => "Vietnamese", "zu" => "Zulu" );
asort ($langs);
function translate($to,$text){

	$ch = curl_init();
	$data=array('sl' => 'en' , 'tl' =>  "$to" , 'text' => "$text");
	$querystring=http_build_query ($data);
	curl_setopt($ch, CURLOPT_URL,'http://www.translate.google.com' . '?' . $querystring);
	curl_setopt($ch,CURLOPT_USERAGENT,'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.13) Gecko/20080311 Firefox/2.0.0.13');
	curl_setopt($ch,CURLOPT_FOLLOWLOCATION,true);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
	curl_setopt($ch, CURLOPT_BINARYTRANSFER, true);
	$s = curl_exec ($ch);
	curl_close ($ch);

	$dom = new DOMDocument; 
	@$dom->loadHTML($s);
	$l = $dom->getElementById('result_box');
	return $l->textContent;
}
?>

<!--- HTML --->
<html><head> <meta http-equiv="content-type" content="application/xhtml+xml; charset=UTF-8">
<title>Translate to 58 langs</title><style>
.divtext {
    border: ridge 2px;
    padding: 5px;
    min-height: 5em;
    overflow: auto;
}
</style>
</head><body>
 <form action="translate.php" method="get">
  TEXT:<br/>
 <textarea name="txt" id="txt" style="width:500px;height:200px;";></textarea> 
  <input type="submit" value="Submit">
</form> 
<br/>

<?php
	if(isset($_GET['txt'])){
		$text=$_GET['txt'];
		$i=1;
		foreach($langs as $key=>$lang){
			$f=translate($key,$text);
			echo "$i \ $lang : <br/><div class=\"divtext\" contentEditable>" . nl2br($f) . " </div> <br/><br/>";
			$i++;
		}
	}
?>
<br/><br/> <div id="footer">created By Ahmad Hegazy {ahegazipro@live.com}.</div>
</body></html>


