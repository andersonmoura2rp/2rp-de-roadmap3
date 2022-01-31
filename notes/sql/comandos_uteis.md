CONVERTER TIPO DE ARQUIVO: 
SELECT CAST(duration AS FLOAT) result FROM processos_critico 

PEGAR HORA MINUTO E SEGUNDO DE UM TIMESTAMP:
EXTRACT( DAY FROM duration ) AS dias,
	EXTRACT( DAY FROM duration ) * 24 + EXTRACT ( HOUR FROM duration ) AS horas, 
	EXTRACT( DAY FROM duration ) * 24 * 60 + EXTRACT( HOUR FROM duration ) * 60 + EXTRACT(MINUTE FROM DURATION) AS minutos,
	EXTRACT( DAY FROM duration ) * 24 * 60 * 60 + EXTRACT( HOUR FROM duration ) * 60 * 60 + EXTRACT(MINUTE FROM DURATION) * 60 + EXTRACT(SECOND FROM DURATION) AS segundos    

	SELECT DATEDIFF(hour,        '2005-12-31 23:59:59.9999999', '2006-01-01 00:00:00.0000000');


CREATE VIEW AS SELECT id, dag_id, end_date, DATEDIFF(hour, start_date, end_date) AS 'Duration'  
    FROM public.dag_run;  

CREATE VIEW processos_criticos AS 
SELECT id, dag_id, start_date, end_date, (end_date - start_date) duration   
    FROM public.dag_run 
    WHERE 
    (dag_id = 'unificacao_pefisa') OR 
    (dag_id = 'unificacao_cliente') OR 
    (dag_id = 'bot_pfin') OR 
    (dag_id = 'bot_termometro_pfin') OR 
    (dag_id = 'conductor_uptodate') OR 
    (dag_id = 'etl_fat_term_pfin_cartao') OR 
    (dag_id = 'etl_fat_ped_venda_whatsapp') OR 
    (dag_id = 'facilita_revendedor') OR 
    (dag_id = 'indicador_figital') OR 
    (dag_id = 'relatorio_vendas_e_comm')
    ORDER BY dag_id;

select CAST(dag_id as decimal(10,2)) as DecimalValues FROM dag_run

CREATE VIEW processos_criticos_tempo AS SELECT 
	id, 
	dag_id, 
	start_date, 
	end_date, 
	duration,
	CAST(duration AS VARCHAR) AS duration_varchar,
	EXTRACT( DAY FROM duration ) AS dias,
	EXTRACT( DAY FROM duration ) * 24 + EXTRACT( HOUR FROM duration ) AS horas, 
	EXTRACT( DAY FROM duration ) * 24 * 60 + EXTRACT( HOUR FROM duration ) * 60 + EXTRACT(MINUTE FROM DURATION) AS minutos,
	EXTRACT( DAY FROM duration ) * 24 * 60 * 60 + EXTRACT( HOUR FROM duration ) * 60 * 60 + EXTRACT(MINUTE FROM DURATION) * 60 + EXTRACT(SECOND FROM DURATION) AS segundos     
FROM  processos_criticos;