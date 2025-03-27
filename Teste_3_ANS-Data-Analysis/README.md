# Teste de Nivelamento - Banco de Dados (MySQL 8 / PostgreSQL >10.0)

Este repositório contém scripts SQL para estruturar tabelas, importar dados e realizar consultas analíticas com base em informações da Agência Nacional de Saúde Suplementar (ANS). Este teste foi solicitado como parte de um processo de nivelamento técnico.


## Aviso sobre Arquivos Grandes

Alguns arquivos grandes não estão incluídos neste repositório devido às limitações de tamanho de arquivo do GitHub (máximo de 25MB por arquivo). Se precisar desses arquivos, entre em contato para que possamos fornecer uma alternativa para compartilhamento.

Agradecemos pela compreensão!


## Objetivo

Criar e executar scripts SQL para processar e analisar dados das operadoras de plano de saúde, incluindo:
- Download e processamento de arquivos CSV da ANS
- Estruturação das tabelas no banco de dados
- Importação de dados
- Consultas analíticas para identificar operadoras com maiores despesas

## Requisitos

1. **Baixar arquivos dos últimos 2 anos** do repositório público:
   - [Demonstrações Contábeis](https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/)
   - [Dados cadastrais das operadoras ativas](https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/)

2. **Criar queries SQL** para:
   - Estruturar as tabelas necessárias para armazenar os dados do CSV.
   - Importar os dados corretamente no banco de dados (MySQL 8 ou PostgreSQL >10.0).
   - Garantir o encoding correto durante a importação.

3. **Elaborar consultas analíticas** para responder:
   - Quais as 10 operadoras com maiores despesas em "EVENTOS/SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA À SAÚDE MÉDICO HOSPITALAR" no último trimestre?
   - Quais as 10 operadoras com maiores despesas nessa categoria no último ano?

## Estrutura do Repositório

- `import_ans_data.sql`: Script SQL para criação de tabelas, importação de dados e consultas analíticas.
- `README.md`: Instruções e requisitos do teste.

## Observação

Este projeto faz parte de um teste de nivelamento técnico e não deve ser utilizado para outros fins sem autorização. Todos os dados utilizados são públicos e fornecidos pela ANS.

