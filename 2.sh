cd /home/pi

str1=`echo "$1" | sed -e 's/シェル//g' | sed -e 's/@Chromium_Linux//g' | tr -d '\n' | sed -e 's/  //g'`

str2=`$str1`

echo "$str2" | sed 's/ //g' | tr -d '\n'