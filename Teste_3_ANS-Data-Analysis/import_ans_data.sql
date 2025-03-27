-- Criando tabelas
CREATE TABLE operadoras (
    id SERIAL PRIMARY KEY,
    registro_ans VARCHAR(20) UNIQUE NOT NULL,
    cnpj VARCHAR(20) NOT NULL,
    razao_social VARCHAR(255) NOT NULL,
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(100),
    uf VARCHAR(2),
    data_registro DATE
);

CREATE TABLE demonstracoes_contabeis (
    id SERIAL PRIMARY KEY,
    registro_ans VARCHAR(20) NOT NULL,
    ano INT NOT NULL,
    trimestre INT NOT NULL,
    receita DECIMAL(15,2),
    despesas_eventos DECIMAL(15,2),
    FOREIGN KEY (registro_ans) REFERENCES operadoras(registro_ans)
);

-- Importand os arquivos 
LOAD DATA INFILE '/csv/*.csv'
INTO TABLE operadoras
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(registro_ans, cnpj, razao_social, nome_fantasia, modalidade, uf, data_registro);

LOAD DATA INFILE '/csv/*.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(registro_ans, ano, trimestre, receita, despesas_eventos);


SELECT o.nome_fantasia, d.registro_ans, SUM(d.despesas_eventos) AS total_despesas
FROM demonstracoes_contabeis d
JOIN operadoras o ON d.registro_ans = o.registro_ans
WHERE d.ano = (SELECT MAX(ano) FROM demonstracoes_contabeis)
  AND d.trimestre = (SELECT MAX(trimestre) FROM demonstracoes_contabeis WHERE ano = (SELECT MAX(ano) FROM demonstracoes_contabeis))
GROUP BY o.nome_fantasia, d.registro_ans
ORDER BY total_despesas DESC
LIMIT 10;


SELECT o.nome_fantasia, d.registro_ans, SUM(d.despesas_eventos) AS total_despesas
FROM demonstracoes_contabeis d
JOIN operadoras o ON d.registro_ans = o.registro_ans
WHERE d.ano = (SELECT MAX(ano) FROM demonstracoes_contabeis)
GROUP BY o.nome_fantasia, d.registro_ans
ORDER BY total_despesas DESC
LIMIT 10;
