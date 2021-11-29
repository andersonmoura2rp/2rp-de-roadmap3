#!/bin/bash
#curso shell script tarefa1 2rp

lista_arquivos(){
echo "Arquivos do repositório: "
	for entry in `ls -R * $search_dir`
do
  echo "$entry" 
done
}

echo 

DIR="$( cd "$( dirname "$0" )" && pwd  )"
echo
echo "Caminho: "
vetor=("$DIR")
echo ${vetor[*]}

lista_arquivos  

insere_texto(){

	echo -e "\n"$1 | tee -a $2 $3 $4 
	echo
	echo "Texto inserido!"
}
insere_texto $1 $2 $3 $4 

#Parâmetros: 
	#Diretório $1
	#Arquivos $2 $3 $4  


