#!/bin/bash

# Variaveis
DIR=`pwd`

# Parametro $1 = Radio
if [ -z $1 ];then
	echo "Entre com uma das Rádios abaixo:"
	cat $DIR/radio.txt | awk '{print $1}'
	exit
fi

# Teste de a Radio exite
STATION=`cat $DIR/radio.txt | awk '{print $1}' | grep -i $1`
if [ -z $STATION ];then
	echo "Radio não existe"
	echo "Entre com uma das Rádios abaixo:"
	cat $DIR/radio.txt | awk '{print $1}'
	exit
fi

STATION=`cat $DIR/radio.txt | grep -i $1 | cut -d " " -f2-`

# Check if is Spotfy
if [ "$STATION" == "spotify" ]; then
	/snap/bin/spotify
else
	mplayer $STATION
fi
