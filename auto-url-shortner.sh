#!/bin/bash

# URL SHORTENER SCRIPT
# shorts list of urls
# This program is free software; you can redistribute it and/or modify it
# depending on PORL URL SHORTENER SCRIPT API
# http://github.com/cydrobolt/polr
# created by AHMAD HEGAZY <ahegazipro@gmail.com>


function short(){
	key="$1"
        encode=`curl -s -o /dev/null -w %{url_effective} --get --data-urlencode "$2" ""`
        url=${encode##/?}
	reply=`curl -s --request POST "$APILINK" --data "apikey=$key&action=shorten&url=$url"`
	[[ $? != 0 ]] && die "PLEASE CHECK The APILINK" 6
	case "$reply" in
		"401 Unauthorized") die "wrong key .. \npleae check your api key .. or contact to service admin" 2
		;;
		"Hey, slow down! Exeeding your perminute quota. Try again in around a minute.") quota
		;;
                "Error: URL is not valid") echo -e "$url is not valid .. \nwill skip it."
                ;;
		*) showlink
		;;
	esac

}

function showlink(){
	echo "$i) LINK: $url >> $reply" | tee -a "$lst.d"
	echo "$reply" >> "$lst.s"
	i=$(($i+1))
}


function die(){
	err="$1"
	ec="$2"
	echo -e "ERROR: $err"
	exit "$ec"
}

function quota(){
	echo "Exeeding perminute quota."
	echo "will delay the short process 5 sec more.."
	sleep=$(($sleep+5))
	sleep $sleep
	short "$key" "$url"
}

function main(){

	key="$1"
	lst="$2"
	APILINK=`echo "$3" | grep -E '(^https?|ftp|file)://[-A-Za-z0-9\+&@#/%?=~_|!:,.;]*[-A-Za-z0-9\+&@#/%=~_|]'`
        [[ ! -f "$lst" ]] && die " $lst FILE NOT FOUND." 3
	[[ -z "$APILINK" ]] && die "$3 WORNG LINK" 4
	sleep=10
	i=1
	urls=`cat "$lst" | grep -E '(^https?|ftp|file)://[-A-Za-z0-9\+&@#/%?=~_|!:,.;]*[-A-Za-z0-9\+&@#/%=~_|]'`

	for url in $urls
	do
		short "$key" "$url"
		sleep $sleep
	done
}

function hlp(){
	echo -e "Auto Url Shortenr"
	echo -e "\tShort list of urls ..\n\tcreated for polr url shortener script."
	echo ""
	echo -e "\tUSAGE: "
	echo -e "\t\t $0 'APIKEK' 'list' 'APILINK'"
	echo -e "\tEXAMPLE"
	echo -e "\t\t $0 \"mykey\" \"list\" \"https://sphinux.org/s/api.php\""
	echo
	echo -e "\tEND: "
	echo -e "\t\tat the end you'll find 2 files \n\t\t\tlist.s : list of shorted links \n\t\t\tlist.d : detailed list of shorted links with old links"
	exit 0
}

[[ "$1" = "-h" || "$1" = "--help" ]] && hlp
[[ -z "$3" ]] && die "no enough parameters .. \ntry -h , --help" 1

main "$@"
