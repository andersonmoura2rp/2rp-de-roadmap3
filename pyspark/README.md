SQL SPARK
- Forma de consulta e manipulação de dados no SPARK utilizando a linguagem SQL.

	CRIAR VIEW(EXEMPLO)
	empresas.createOrReplaceTempView("empresasView").show(n)

	SELECT (EXEMPLO)
	spark.sql("SELECT * FROM empresasView").show(n)

	WHERE
	spark.sql("""SELECT * FROM empresasView WHERE capital_social=50""").show(n)

	MEDIA
	spark.sql("""SELECT porte_empresa, MEAN(capital) AS Media FROM empresasView GROUP BY porte_empresa""").show(n)

	UNION
	spark.sql("""SELECT * FROM freqView UNION ALL SELECT 'Total' AS data_inicio, SUM(count) AS count FROM FreqView""").show()

FORMAS DE ARMAZENAMENTO
	ARQUIVOS CSV
	empresas.write.csv(path='<caminho>', mode='overwrite', sep=';', header=True)
		LEITURA
		empresas2 = spark.read.csv('<caminho>', sep=';', inferSchema=True, header=True)

	ARQUIVOS PARQUET
	formato de armazenamento colunar disponível para qualquer projeto no ecossistema Hadoop, independentemente da escolha da estrutura de processamento de dados, modelo de dados ou linguagem de programação.
	empresas.write.parquet(path='<caminho>', mode='overwrite')
		LEITURA
		empresas2 = spark.read.parquet(path='<caminho>')

	ARQUIVOS ORC
	formato de arquivo colunar. Ele é otimizado para grandes leituras de streaming, mas com suporte integrado para localizar as linhas necessárias rapidamente. O armazenamento de dados em formato colunar permite ler, descompactar e processar apenas os valores necessários para a consulta.
	empresas.write.orc(path='<caminho>', mode='overwrite')

PARTICIONAMENTO DE DADOS
empresas.coalesce(1).write.csv(path='<caminho>', mode='overwrite', sep=';', header=True)
empresas.write.parquet(path='<caminho>/parquet-partitionBy', mode='overwrite', partitionBy='porte_empresa')

