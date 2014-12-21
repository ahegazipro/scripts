#!/bin/bash

# "THIS SCRIPT WILL INSTALL PHTOSHOP CS6 IN SPHINUX OS."
# "........ ANY ERRORS OR BUGS PLEASE SEND IT TO ..........."
# " >>>>> AHMAD HEGAZY 'hegazy@sphinux.org' <<<<<"
echo
echo

function EXIT(){
	err=$1
	ec=$2
	echo -e "ERROR : $err"
	echo "WILL EXIT NOW."
	exit $ec
}

function chk(){
	frspc=`df | grep "/home" | awk '{ print $4 }'`
	ned=1048576

	if [[ $ned -ge $frspc ]]
	then
		return 1
	else
		return 0
	fi
}

function main(){
      USER=`whoami`
      [[ "$USER" = "root" ]] && EXIT "PLEASE DON'T RUN SCRIPT AS ROOT USER." 1

      chk
      [[ $? != 0 ]] && EXIT  "NO ENGOUPH SPACE IN HOME PARTITION." 2

      cd /home/$USER
      mkdir .ps6 >> /dev/null 2>&1
      cd .ps6 

      echo -e "DOWNLOADING POHTOSHOP PLEASE WAIT \nIT MIGHT TAKE SEVERAL MINUTES"
      wget -c https://www.sphinux.org/misc/files/PS-CS6.zip >> /dev/null 2>&1
      [[ $? != 0 ]] && EXIT "PHOTOSHOP CAN'T BE DOWNLOADED .. \n PLEASE CHECK YOUR INTERNET CONNECTION." $?
      echo
      echo
      echo -e "DOWNLOADING WINE CONFIGURATION .. PLEASE WAIT \nIT MIGHT TAKE SEVERAL MINUTES"
      wget -c https://www.sphinux.org/misc/files/wine.7z >> /dev/null 2>&1
      [[ $? != 0 ]] && EXIT "WINE CONFIG. CAN'T BE DOWNLOADED .. \n PLEASE CHECK YOUR INTERNET CONNECTION." $?
      echo
      echo
      echo "INSTALLING WINE \n ITMIGHT TAKE SEVERAL MINUTES"
      echo "PLEASE PROVIDE YOUR PASSWORD FOR THE FOLLOWING COMMAND: "
      echo "sudo apt-get install wine"
      (sudo apt-get update && sudo apt-get -y install wine) >> /dev/null 2>&1
      [[ $? != 0 ]] && EXIT "WINE CONFIG. CAN'T BE INSTALLED .. \n PLEASE CHECK YOUR INTERNET CONNECTION \n AND YOUR REPOSITORY\apt-get log." $?
      echo
      echo
      echo "REMOVING OLD WINE CONFIGURATION FILES"
      rm -rf /home/$USER/.wine > /dev/null 2>&1
      echo
      echo
      echo "EXTRACTING PHOTOSHOP"
      unzip -u ./PS-CS6.zip -d ps >> /dev/null 2>&1
      [[ $? != 0 ]] && EXIT "PHOTOSHOP ZIP FILE EXTRACTING ERROR" $?
      echo
      echo
      echo "EXTRACTING WINE CONFIGURATION FILES"
      7z x ./wine.7z -o/home/$USER/ >> /dev/null 2>&1
      [[ $? != 0 ]] && EXIT "WINE CONFIGURATION FILE EXTRACTING ERROR" $?
      echo
      echo
      echo "INSTALLING PHOTOSHOP"
      echo "PLEASE PRESS NEXT>>NEXT>>FINISH"
      wine "/home/$USER/.ps6/ps/Adobe Photoshop CS6 Extended.exe"  > /dev/null 2>&1
      echo
      echo
      echo "INSTALLATION FINISHED .."
      echo "YOU'll Find PHOTOSHOP ON YOUR DESKTOP."
      echo "TRY IT ."

      echo
      echo
}

main