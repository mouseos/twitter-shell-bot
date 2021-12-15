#!/bin/sh

#[twitterID]にTwitterアカウントのIDを入れてください(例:sed -e 's/@Chromium_Linux//g')

str1=`echo "$1" | sed -e 's/シェル//g' | sed -e 's/@twitterID//g' | tr -d '\n' | sed -e 's/  //g'`

str2=`timeout 4 $str1 2>&1`

echo "$str2" | sed 's/ //g' | perl -pe 's/\n//g' | cut -c 1-139
