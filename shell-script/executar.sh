#!/bin/bash
#curso shell script tarefa 2rp
source funcoes.sh

echo

lista_arquivos Subdir1

for i in $(seq 1 ${#files[@]})
    do
        insere_texto "Alterações 3" ${files[i-1]} 
    done

#Parâmetros: 
	#Diretório $1
	#Texto $2 
