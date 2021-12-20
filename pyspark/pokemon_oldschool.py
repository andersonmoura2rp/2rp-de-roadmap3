#ATIVIDADE SPARK TRILHA DE APRENDIZADO ENGENHARIA DE DADOS
#ANDERSON DAVID DE MOURA JUNIOR

#Importar bibliotecas Spark:
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
sc = SparkContext.getOrCreate()
spark = SparkSession(sc)

#Carregar dados da tabela pokemon_anderson
df_pokemon_anderson = spark.table("work_dataeng.pokemon_anderson");
df_pokemon_anderson.show();

#Carregar dados da tabela generation_anderson
df_generation_anderson = spark.table("work_dataeng.generation_anderson");
df_generation_anderson.show();

#Criar filtro para pegar somente as gerações inferiores a 2002-11-21 e fazer um cache do dataframe:
df_generation_anderson = df_generation_anderson.filter("date_introduced < '2002-11-21'");
df_generation_anderson.show();
df_generation_anderson = df_generation_anderson.cache()

#Renomear colunas "generation" para evitar nomes duplicados
df_pokemon_anderson = df_pokemon_anderson.withColumnRenamed('generation', 'p_generation');
df_generation_anderson = df_generation_anderson.withColumnRenamed('generation', 'g_generation');
pokemons_oldschools_anderson = pokemons_oldschools_anderson.withColumnRenamed('generation', 'o_generation');

#Inner join entre generation_anderson e pokemon_anderson
df_innerjoin = df_pokemon_anderson.join(df_generation_anderson, on=[df_p_anderson.pokemon_generation == df_generation_anderson.g_generation], how = 'inner');

#Criar view a partir do df_innerjoin para popular tabela
df_innerjoin.createOrReplaceTempView("df_innerjoin_anderson");

#Criar tabela a partir dos dados da view:
spark.sql("create table work_dataeng.pokemons_oldschool_anderson as select * from df_innerjoin_anderson");