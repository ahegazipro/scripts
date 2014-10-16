#!/bin/bash

#this script made By Ahmad Hegazy <ahegazipro@gmail.com> 
#you can Edit it and add new features but please don't remve copyright ,, thnaks 

function chkOSs(){
	#check installed systems
	OS=`os-prober`
	SPHNUM=`echo "$OS" | grep -ci "SphinUX"`
	SPHINUX=`echo "$OS" | grep -i "SphinUX"`
	#check if sphinux have more than one installations

	if [[ $SPHNUM > 1 ]]
	then
		chosGrub "$SPHINUX" "SPHNUM"
	elif [[ $SPHNUM == 1 ]]
	then
		SPHPART=`echo "$SPHINUX" | cut -d ":" -f1`
		restGrub "$SPHPART"
	else
		echo -e "Sorry SphinUX is not installed in your computer .. \nHorus installer will be opened ."
		sleep 5
		horus
	fi
}

#if sphinux installed more than one time ...
function chosGrub(){
	SPHINUX=`echo "$1" | sed 's/ //g'`
	SPHNUM=$2
	echo "SphinUX has been installed $SPHNUM times \n please choose which time to restore grub for .. ?"

	i=1
	chsLst=""
	for inst in $SPHINUX
	do
		chsLst+=`echo -e "\n$i) $inst \n"`
		i=$(($i+1))
	done

	while true
	do
		echo "$chsLst"
		read -p ">>> " num
		chkNum=`echo "$num" | grep [1-9]`
		if [[ -z $chkNum ]] || [[ $chkNum > $SPHNUM ]]
		then
			echo -e "please enter a vailed number form listed numbers !\n"
			continue
		else
			SPARTNAM=`echo "$chsLst" | grep "^$chkNum.*$"`
			PARTNAM=`echo "$SPARTNAM" | cut -d ' ' -f2 | cut -d ':' -f1`
			restGrub "$PARTNAM"
			break
		fi
	done
}
function restGrub(){
	SPHPART=$1
	echo "restoring SphinUX grub '$SPHPART' "
	partNam=`echo "$SPHPART" | sed -e 's/\/dev\///g'`
	mntPoint="/mnt/$partNam"
	mkdir $mntPoint
	mount $SPHPART $mntPoint

	/usr/share/horus/scripts/horus-grubconfig $mntPoint MBR
	echo "will reboot now"
	reboot
}

chkOSs
