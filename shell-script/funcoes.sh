#!/bin/bash
#curso shell script tarefa1 2rp

lista_arquivos(){
echo "Arquivos do repositório: "
files=(`find $1 -type f`)

echo ${files[*]} 
}

echo 

DIR="$( cd "$( dirname "$0" )" && pwd  )"
echo
echo "Caminho: "
vetor=("$DIR")
echo ${vetor[*]}
echo

lista_arquivos $1 $2 

insere_texto(){

	echo -e "\n"$1 | tee -a $2 $3 $4 
	echo
	echo "Texto inserido!"
}
insere_texto $1 $2 $3 $4 

#Parâmetros: 
	#Diretório $1
	#Arquivos $2 $3 $4  


