#!/bin/bash
# Search Radio Stations
RADIOS=`curl https://www.radios.com.br/ | grep "https://www.radios.com.br/aovivo/" | sed 's/>/=/g' | cut -d '=' -f3-4 | sed 's/title=//g' | sed 's/Ouvir //g' | sed 's/" "/","/g' | sed 's/ /_/g' | sed 's/https/http/g' | sed 's/"//g'`
for aux in $RADIOS; do
	station=`echo $aux | cut -d "," -f2`
	url=`echo $aux | cut -d "," -f1`
	echo $station,$url
done
