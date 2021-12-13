
create table generation_anderson(
    generation int,
    date_introduced date
)
 stored as orc;


create table pokemon_anderson (
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