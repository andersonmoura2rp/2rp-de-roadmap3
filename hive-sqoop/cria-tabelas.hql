--ATIVIDADE HIVE/SQOOP -- ANDERSON -- TRILHA DE APRENDIZADO ENGENHARIA DE DADOS 2RP --

create table work_dataeng.generation_anderson(
    generation int,
    date_introduced date
)
 stored as orc;


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