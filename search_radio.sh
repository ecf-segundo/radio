#!/bin/bash
# Search Radio Stations
# Busca no site www.radios.com.br pelas estações
RADIOS=`curl https://www.radios.com.br/ | grep "https://www.radios.com.br/aovivo/" | grep btn | sed 's/ /_/g' | sed 's/"_/" /g' | sed 's/data-toggle="tooltip" //g' |cut -d " " -f2- | sed 's/href="https/https/g' | sed 's/"//g' | sed 's/>/ /g' | sed 's/</ /g' | awk '{print $1,$3}' | sed 's/ /,/g'`

# Para a lista gerada de radios cria o arquivo com radio_list.txt
# A URL eh aquela que permite a execução do stream via mplayer
for aux in $RADIOS; do
	station=`echo $aux | cut -d "," -f2 | sed 's/_/ /g'`
	temp_url=`echo $aux | cut -d "," -f1`
	url=`curl $temp_url | grep "'url':'" | cut -d ":" -f2- | cut -d "'" -f2`
	echo $station,$url >> radio_list.txt
done

# Verifica os duplicados
### Implementar

# Verifica se os links ainda estão inteiros
### Implementar
