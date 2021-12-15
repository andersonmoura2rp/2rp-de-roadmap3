--CRIAÇÃO DAS TABELAS--
	TABELA GENERATION:
	create table work_dataeng.generation_anderson(
	    generation int,
	    date_introduced date
	) 
	stored as orc;

	TABELA POKEMON
	create table work_dataeng.pokemon_anderson (
		idnum   int, 
		name string, 
		hp  int,
		speed   int,
		attack  int,
		special_attack  int, 
		defense int, 
		special_defense int, 
		generation  int
	) 
	stored as orc;

POPULAR TABELAS
	TABELA GENERATION: 
	insert into work_dataeng.generation_anderson
	(generation,date_introduced) 
	values
	(1,'1996-02-27'),
	(2,'1999-11-21'),
	(3,'2002-11-21'),
	(4,'2006-09-28'),
	(5,'2010-09-18'),
	(6,'2010-12-13'),
	(7,'2016-11-18');

	TABELA POKEMON:
	1) Abrir o hive através do hue
	2) Acessar HDFS > USER > UPLOAD FILE > pokemon.csv
	3) Criar tabela temporária:
		create external table work_dataeng.pokemon_anderson_temp (
		idnum   int, 
		name string, 
		hp  int,
		speed   int,
		attack  int,
		special_attack  int, 
		defense int, 
		special_defense int, 
		generation  int
		) row format delimited fields terminated by ',' 
		stored as textfile tblproperties ("skip.header.line.count"="1");

	4)load data inpath 'hdfs://bigdataclu-ns/user/2rp-anderson/pokemon.csv' into table work_dataeng.pokemon_anderson_temp;
	5)insert into work_dataeng.pokemon_anderson select * from work_dataeng.pokemon_anderson_temp;
JOIN
	HIVE: 1min48seg
		select * from work_dataeng.pokemon_anderson p  
		join work_dataeng.generation_anderson g  
		on p.generation = g.generation;

	IMPALA:1.38 SEGUNDOS (*No impala a coluna data_introduced não deve ser selecionada pois o tipo DATE não é suportado)
		select G.generation, P.* from work_dataeng.generation_anderson G
		join work_dataeng.pokemon_anderson P  
		on G.generation = P.generation;

