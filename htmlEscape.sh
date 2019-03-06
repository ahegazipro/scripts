#!/bin/bash


if [ -r $1 ] && [ ! -z $1 ] # check if the file exists and we have read permission
then
	sed 's/&/\&amp;/g; s/</\&lt;/g; s/>/\&gt;/g; s/"/\&quot;/g; s/'"'"'/\&#39;/g' $1 > $1.escaped.txt
	echo "Escaped html stored in " $1.escaped.txt
else
	echo "USAGE: htmlEscape [HTML FILE PATH]"
fi
