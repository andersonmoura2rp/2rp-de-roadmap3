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

lista_arquivos

echo
echo "Caminho: "
vetor=("$DIR")
echo ${vetor[*]}

insere_texto(){
	echo
	echo "Digite o que deseja inserir no arquivo: "
	read p
	echo $p >> arquivo.txt 
	echo
	echo "Texto inserido em arquivo.txt"
	echo
	cat arquivo.txt
}
insere_texto 