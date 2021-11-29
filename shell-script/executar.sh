#!/bin/bash
#curso shell script tarefa 2rp
echo "Digite o diretório desejado: Subdir1 ou Subdir2? "
read entry

echo

  
lista_arquivos(){

echo "Vetor: "
vetor=(`ls $entry`)
echo ${vetor[*]}
entra=`cd $entry`
echo $entra  


}
lista_arquivos

insere_texto(){
echo 
DIR="$( cd "$( dirname "$0" )" && pwd  )"
vetor2=("$DIR")

echo
echo "Digite um texto qualquer: "
read p
echo
echo "Em qual arquivo deseja inserir? 0, 1 ou 2? "
read n

	echo $p >> ${vetor2[*]}/$entry/${vetor[$n]}    
	echo 
	echo
	echo "Texto inserido"


}

insere_texto 