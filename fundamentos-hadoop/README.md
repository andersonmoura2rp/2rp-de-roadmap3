FUNDAMENTOS - HADOOP - 2RP
ANOTAÇÕES ANDERSON

1)HADOOP ECOSYSTEM
HDFS - HADOOP DISTRIBUTED FILE SYSTEM
- Armazenamento de diferentes tipos de grandes conjuntos de dados.
- Estruturados/Não-Estruturados/Semi-Estruturados
- Cria um nível de abstração Sobre os recursos 
- Componente principal do ecossistema Hadoop
	COMPONENTES HDFS
		NAMENODE
		- Nó principal 
		- Contem metadados
		- Requer menos armazenamento e mais recursos computacionais.
		DATANODE
		- Armazena dados do namenode
		- Requer mais armazenamento
		- Hardware
YARN - YET ANOTHER RESOURCE NEGOTIATOR
- Cérebro do ecossistema Hadoop
- Atividades de processamento
- Aloca recursos e agenda tarefas
	COMPONENTES YARN
		RESOURCE MANAGER
		- Nó principal da área de processamento
		- Recebe solicitações de processamento e passa para os NodeManager correspondentes
		NODE MANAGER
		- Onde o processamento ocorre
		- Instalados em cada DataNode
		- Responsável pela execução de tarefas
		SCHEDULERS
		- Se baseia nos requisitos de recursos
		- Executa algoritmos de agendamento e aloca recursos
		APLICATION MANAGERS 
		- Aceita o envio de trabalho
		- Negocia os containers
		- Execução de tarefas
MAPREDUCE 
- Principal componente de processamento
- Fornece a lógica de processamento
- Estrutura de software que ajuda a escrever aplicativos que processam grandes conjuntos de dados
- Utiliza algoritmos distribuídos e paralelos
	FUNÇÕES
		MAP(): Executa ações como filtragem, agrupamento e classificação
		REDUCE(): Agrege e resume o resultado produzido pela função MAP
APACHE PIG
- Pig Latin: Linguagem
- Pig Runtime: Ambiente de execução
- Estrutura de comando semelhante a SQL
	1 linha pig latin = 100 linhas map-reduce
- O compilador converte pig latin em map reduce
- Fornece uma plataforma para construção de fluxo de dados para ETL, processamento e análise.
APACHE HIVE
- Criado pelo facebook para fluentes em SQL
- Componente de armazenamento de dados que faz: leitura, gravação e gerenciamento de grandes conjuntos de dados
- Semelhantes a SQL
	HQL: HIVE + SQL
	- Linguagem de consulta do HIVE 
	- Altamente escalonével
		- Processamento de consulta
		- Processamento em tempo real
	- Suporta todos os tipos de dados primitivos SQL
		COMPONENTES
		- Linha de comando: execução
		- JDBC(JAVA)/ODBC(OBJECT): Conexão do armazenamento
MAHOUT
- Ambiente para criação de aplicativos de machine learning escalonáveis
	O QUE FAZ
		FILTRAGEM COLABORATIVA
		- Análise comportamentos de usuários
		- Previsão
		- Faz recomendações ex: site de comércio
		CLUSTERING
		- Organiza e agrupa dados semelhantes
		CLASSIFICAÇÃO
		- Classifica e categoriza os dados em subdepartamentos
		CONJUNTO DE ITENS FREQUENTES AUSENTES
		- Verifica quais objetos aparecem juntos
		- Faz sugestões, se tiverem ausentes
APACHE SPARK	
- Estrutura para a análise de dados em tempo real
- Ambiente de computação distribuído
- Executa cálculos na memória para aumentar a velocidade de processamento do Map-Reduce
- Suporta R, SQL, PYTHON, SCALA, JAVA, ETC.
APACHE HBASE
- Banco de dados distribuído
- Não relacional
- Código aberto
- Suporte a todos os tipos de dados
- Tolerante a falhas
- JAVA
- Recuperar pequena quantidade de dados de grandes conjuntos de dados
APACHE DRILL 
- Análise de grandes conjuntos de dados 
- Réplica d Google Dremel
- Fornece escalabilidade para processar petabytes e exabytes de dados de forma eficiente
	FUNCIONALIDADES
	- Combinação de uma variedade de armazenamento de dados usando apenas uma única consulta
APACHE ZOOKEEPER
- Coordenador de qualquer trabalho do Hadoop
- Vários serviços em um sistema distribuído
APACHE OOZIE
- Serviço de relógio e alarme
- Planejador
	FLUXO DE TRABALHO
	- Conjunto sequencial de ações a serem executadas
	- Como uma corridad de revezamento
	COORDENADOR
	- Trabalhos que são acionados quando os dados são disponibilizados
APACHE FLUME
- Ingestão de dados não-estruturados/semi-estruturados HDFS
- Solução confiável e distribuída
- Ajuda na coleta e movimentação de grandes conjuntos de dados de diversas fontes
	COMPONENTES
		FONT: Aceita os dados da linha de entrada e armazena no channel
		CHANNEL: Armazenamento temporário entre a fonte de dados e os dados do HDFS
		SINK: Coleta os dados
APACHE SQOOP
-Ingestão de dados não-estruturados, semi-estruturados/estruturados
	MAPTASK
	- Subtarefa que importa parte dos dados para Hadoop
APACHE SOLR & LUCENE 
- Pesquisa e indexação
	LUCENE
	- JAVA
	- Núcleo
	SOLR
	-Aplicativo desenvolvido em torno do lucene 
	Utiliza a biblioteca de pesquisa lucene para pesquisa e indexação
APACHE AMBARI
- Torna o Hadoop mais gerenciável
	PROVISIONAMENTO DE CLUSTER
	- Fornece passo a passo para instalar serviços Hadoop
	- Faz a configuração de serviços em um cluster
	GERENCIAMENTO DE CLUSTER
	- Fornece serviço de gerenciamento central para iniciar, interromper e reconfigurar serviços Hadoop
	MONITORAMENTO DE CLUSTER
	- Monitorar a saúde e status
	- Fornece um painel
		FRAMEWORK AMBER ALERT
		- Serviço de alerta de acordo com a necessidade

