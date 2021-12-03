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

2) HADOOP ARCHITETURE 
ARQUITETURA HDFS
- Sistema de arquivos estruturados em blocos 
- Cada arquivo é dividido em blocos de tamanho pré-determinado
- Os blocos são armazenados em um cluster de uma ou várias máquinas
- Segue uma arquitetura "mestre-escravo" em que um cluster é composto por um único NameNode e todos os outros nós são DataNodes
NAMENODE
- Nó mestre
- Mantém e gerencia os blocos presentes nos DataNodes (nós-escravos)
- Controla o acesso dos clientes aos arquivos
- Os dados residem apenas no DataNodes
	FUNÇÕES
	I) Mantém e gerencia DataNodes
	II) Registra os metadados de todos os arquivos armazenados no cluster
		ARQUIVOS ASSOCIADOS AOS METADADOS
		- FSIMAGE: Contém o estado completo do namespace do sistema de arquivos
		- EDITLOGS: Contém todas as modificações recentes feitas no sistema de arquivos em relação ao FSIMAGE mais recente
	III) Registra cada mudança que ocorre nos metadados
	IV) Recebe regularmente um heartbeat e um relatório de bloco de todos os DataNodes
	V) Cuidar do fator de replicação
	VI) No caso de falha do DataNode, o NameNode escolhe novos DataNodes para novas réplicas, equilibra o uso do disco e gerencia o trafego de comunicação para os DataNodes
DATANODE
- Nó escravo
- Hardware
- Servidor de bloco que armazena os dados no arquivo local ext3 ou ext4
	FUNÇÕES
	I) Armazenamento dos dados reais
	II) Executam as solicitações de leitura e gravação de baixo nível dos clientes do sistema de arquivos
	III) Enviam pulsações ao NameNode periodicamente(3s) para relatar a integridade geral do HDFS
NAMENODE SECUNDÁRIO
- Funciona simultaneamente com o NameNode 
- Auxiliar
	FUNÇÕES
	I) Lê sistemas de arquivo e metadados da RAM do NameNode e os grava no disco rígido ou no sistema de arquivos
	II) Combinar EditLogs com FSIMAGE do NameNode
	III) Baixa os EditLogs do NameNode em intervalos regulares e se aplica ao FsImage é copiado de volta para o NameNode, que é usado sempre que o NameNOde é iniciado
BLOCOS
- Menor local contínuo em disco rígido onde os dados são armazenados
- Tamanho padrão: 128MB
* Não é necessário ser múltiplos exatos
	GERENCIAMENTO DE REPLICAÇÃO
	- Tolerância a falhas
	- Fator de replicação padrão: 3
	- Cada bloco é replicado 3x e armazenado em diferentes DataNodes
	CONSCIENTIZAÇÃO DE RACK
	- O NameNode garante que todas as réplicas não sejam armazenadas no mesmo rack
	- Redução de latência e tolerância a falhas
	- A primeira réplica será armazenada em um rack local e as outras 2 em um rack remoto
		VANTAGENS
		- Melhor desempenho da rede
		- Evitar perda de dados
ARQUITETURA DE LEITURA E GRAVAÇÃO
- Filosofia Write Once-Read Many
- Não se pode editar arquivos já armazenados mas pode acrescentar novos dados abrindo novamente o arquivo
	GRAVAÇÃO
	- NameNode concederá ao cliente a permissão de gravação e fornecerá os IPs dos DataNodes
	- Etapas:
	1. Configuração do pipeline
	2. Streaming e replicação de dados
	3. Desligamento do pipeline
		CONFIGURAÇÃO DO PIPELINE
		- Antes de gravar os blocos, o cliente confirma se os DataNodes, presentes nas listas estão prontos para receber os dados
		- É criadpo um pipeline para cada bloco, conectando os DataNodes individuais na lista desse bloco
			ETAPAS CRIAÇÃO
			1. O cliente escolhe o primeiro DataNode da lista
			2. O cliente informa o DataNode1 para estar pronto para receber o bloco
			3. O DataNode1 se conecta ao DataNode4. O DN1 informa o DN4 para estar pronto e da o IP do 6, então dirá ao 6, etc.
			4. O reconhecimento segue sequência inversa 6 -> 4 -> 1 -> cliente
			5. Por fim, informa o cliente
			6. Inicia o processo de streaming
		STREAMING DE DADOS
		- Envio de dados para o pipeline
		- Replicação de dados com base no fator 3
			ETAPAS REPLICADO
			1. Depois que o bloco foi gravado no DN1 pelo cliente, o DN1 se conectará ao DN4
			2. DN1 enviará o bloco no pipeline e os dados serão copiados para o DN4
			3. DN4 se conectará ao DN6 e copiará a ultima replica do bloco 
		ENCERRAMENTO DO PIPELINE/RECONHECIMENTO
		- Uma série de reconhecimento ocorrerá para garantir ao cliente e NameNode que os dados foram gravados com sucesso
		- A configuração ocorre na sequencia inversa
			1. O DN enviará 3 confirmações para o pipeline e as enviará ao cliente
			2. O cliente informará NameNode que os dados foram gravados
			3. O NameNode atualização seus metadados
			4. Cliente desligará o pipeline
	LEITURA
	- Etapas
		1. O cliente solicita os metadados do bloco
		2. O NameNode retorna a lista de DataNodes
		3. O Namenode se conecta ao DataNode
		4. Cliente lê os dados e forma o arquivo

3) UDEMY - REAL WORLD HADOOP - HANDS ON ENTERPRISE DISTRIBUTED STORAGE
CRIANDO UM ESPAÇO DE USUÁRIO PARA LER/GRAVAR
	COMANDO LS EM CLUSTER
	- hdfs dfs -help ls (ajuda)
	- hdfs dfs ls (lista conteúdo)
	- hdfs dfs -mkdir (cria diretorio)
	- sudo -u hdfs -mkdir/user/<nome> (muda user)
CARREGANDO UM ARQUIVO NO HDFS (UPLOAD)
- hdfs dfs -help put (ajuda)
- hdfs dfs -put <localsrc> <caminho> (upload)
- hdfs dfs -cat (ler arquivo)
- hdfs dfs -tail (ler parte do arquivo)
- hdfs fsck <caminho> (detalha o arquivo)
- hdfs fsck <caminho> -files -blocks (detalha os blocos)
	LS, RM E EXPUNGE
	- - hdfs dfs -rm -skiptrash <arquivo> <caminho> (remove tudo permanentemente)
* trash = lixeira(opcional)
FAZER MERGE DE VÁRIOS ARQUIVOS SIMULTANEAMENTE
1) Criar n arquivos
2) Add todos em uma única pasta
3) hdfs dfs -help appendToFile
4) hdfs dfs -appendToFile toyin* <localsrc><dst> /arquivo.txt
appendToFile: unir vários arquivos em um único
BUSCA DE ARQUIVOS -find
- find .-name "<nomearquivo>" (local)
- hdfs dfs -find <caminho> -name "<nome>" 
- hdfs dfs -find <caminho> -name "<nome*>" (arquivo que começam com nome)
GET E GETMERGE
- hdfs dfs help -get
- hdfs dfs -get <caminho><destinolocal>
- hdfs dfs help -getmerge
- hdfs dfs -getmerge <caminho><destino>
CONTAGEM DE ARQUIVOS/PASTAS
- hdfs dfs help -count
- hdfs dfs -count -h -v <caminho>
TODOS OS COMANDOS
- hdfs dfs
COPIAR E MOVER ARQUIVOS
-cp <nome><destino>(dentro de uma pasta)
-mv <nome><destino>
-cp <origem><destino>(dentro de outro arquivo)
-mv <origem><destino>
COMBINAR TOUCH E APPENDTOFILE
- hdfs dfs touchz <caminho>.<nomearquivo>