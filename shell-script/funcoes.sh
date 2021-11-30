#!/bin/bash
#curso shell script tarefa1 2rp

lista_arquivos(){

echo "Arquivos do repositório: "
files=(`find $1 -type f`)
echo ${files[*]} 

}

echo 

insere_texto(){

	echo -e "\n"$1 | tee -a $2 $3 $4 
	echo
	echo "Texto inserido!"
}
#Parâmetros: 
	#Diretório $1
	#Arquivos $2 $3 $4  


