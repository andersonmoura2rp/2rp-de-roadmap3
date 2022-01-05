#ATIVIDADE PYSPARK
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
sc = SparkContext.getOrCreate()
spark = SparkSession(sc)

df_pokemon_anderson = spark.table("work_dataeng.pokemon_anderson");
df_generation_anderson = spark.table("work_dataeng.generation_anderson");


df_generation_anderson = df_generation_anderson.filter("date_introduced < '2002-11-21'");
df_generation_anderson = df_generation_anderson.cache();

df_pokemon_anderson = df_pokemon_anderson.withColumnRenamed('generation', 'p_generation');
df_generation_anderson = df_generation_anderson.withColumnRenamed('generation', 'g_generation');

df_innerjoin = df_pokemon_anderson.join(df_generation_anderson, on=[df_pokemon_anderson.p_generation == df_generation_anderson.g_generation], how = 'inner');

df_innerjoin.write.mode('overwrite').format('orc').saveAsTable('work_dataeng.pokemons_oldschool_anderson');

#ATIVIDADE KAFKA
from pyspark.sql.functions import struct, to_json

pokemons_oldschool_anderson = spark.sql("""SELECT * FROM work_dataeng.pokemons_oldschool_anderson limit 10""")
database = 'work_dataeng'
topic_name = "nifi.send.trilha.conhecimento"
kafka_bootstrap_servers = "192.168.80.8:19093,192.168.80.7:19093,192.168.80.14:19093"
options = {
    "kafka.sasl.jaas.config": "com.sun.security.auth.module.Krb5LoginModule required useKeyTab=true keyTab=\"/home/{user}/{user}.keytab\" principal=\"{user}@BDACLOUDSERVICE.ORACLE.COM\";".format(
        user=z.getInterpreterContext().getAuthenticationInfo().getUser()),
    "kafka.security.protocol": "SASL_SSL",
    "kafka.sasl.kerberos.service.name": "kafka",
    "kafka.ssl.truststore.location": "/opt/cloudera/security/pki/bds.truststore",
    "kafka.ssl.truststore.password": "dqmQtyVB6zzjcJbZAi7DIa8LRkM7zVX3",
    "kafka.bootstrap.servers": kafka_bootstrap_servers,
    "topic": topic_name

}

pokemons_oldschool_anderson.select(to_json(struct("name")).alias("value")).selectExpr("CAST(value AS STRING)").write.format("kafka").options(**options).save()
