#!/bin/bash
### Search Radio Stations
# Arquivo com a lista de radios
RadioList="all_radio_list.txt"
# Busca no site www.radios.com.br pelas estações
RADIOS=`curl -s https://www.radios.com.br/ | grep "https://www.radios.com.br/aovivo/" | grep btn | sed 's/ /_/g' | sed 's/"_/" /g' | sed 's/data-toggle="tooltip" //g' |cut -d " " -f2- | sed 's/href="https/https/g' | sed 's/"//g' | sed 's/>/ /g' | sed 's/</ /g' | awk '{print $1,$3}' | sed 's/ /,/g'`

# Para a lista gerada de radios cria o arquivo com radio_list.txt
# A URL eh aquela que permite a execução do stream via mplayer
for aux in $RADIOS; do
	station=`echo $aux | cut -d "," -f2 | sed 's/_/ /g'`
	temp_url=`echo $aux | cut -d "," -f1`
	url=`curl -s $temp_url | grep "'url':'" | cut -d ":" -f2- | cut -d "'" -f2 | sed 's/;//g'`
	echo $station,$url | sed 's/;//g' >> $RadioList
done

### Verifica os duplicados / Estações sem url válida
# Arquivo temporario - Elimina estações sem url e duplicados
TMP="tmp.txt"
# Elimina duplicados e vazios
duplicados=`cat $RadioList | cut -d "," -f2 | sort | uniq | awk '{print $1}'`
for item in $duplicados; do
	cat $RadioList | grep $item | head -1 >> $TMP
done

# Substitui o arquivo original por esse alterado
cat $TMP > $RadioList

# Exclui arquivo temporário
rm -Rf $TMP

# Verifica se os links ainda estão inteiros
### Implementar
