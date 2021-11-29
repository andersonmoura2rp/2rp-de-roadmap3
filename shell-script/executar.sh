#!/bin/bash
#curso shell script tarefa 2rp
source funcoes.sh

echo

files=(`find $1 -type f`)
echo "Vetor Arquivos: "
echo ${files[*]}

for i in $(seq 1 ${#files[@]})
    do
        insere_texto "$2" ${files[i-1]} 
    done

#Parâmetros: 
	#Diretório $1
	#Texto $2 
