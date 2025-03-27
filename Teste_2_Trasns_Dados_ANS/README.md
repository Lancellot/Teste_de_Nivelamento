## Transformação de Dados - ANS - Teste de Nivelamento

Este projeto foi desenvolvido como parte de um teste de nivelamento solicitado. O objetivo é extrair dados da tabela "Rol de Procedimentos e Eventos em Saúde" no Anexo I do PDF da ANS, salvar os dados em formato CSV, substituir as abreviações das colunas OD e AMB por suas descrições completas e compactá-los em um arquivo ZIP.

## 🛠️ Requisitos do Teste

O código solicitado para o teste deve realizar as seguintes tarefas:

  1. Extrair os dados da tabela "Rol de Procedimentos e Eventos em Saúde" presente no Anexo I do PDF.
  2. Salvar os dados extraídos em uma tabela estruturada no formato CSV.
  3. Compactar o CSV gerado em um arquivo ZIP nomeado como Teste_Assis_P_N.zip.
  4. Substituir as abreviações OD e AMB pelas descrições completas, conforme a legenda do rodapé do PDF.

## 📌 Tecnologias Utilizadas

   - **Python 3**

   - `pdfplumber` - Para extrair as tabelas do PDF

   -`pandas` - Para manipulação dos dados e criação do arquivo CSV

   -`zipfile`- Para compactar o arquivo CSV

   ## 🚀 Como Executar
1. Instale as dependências:
   ```sh
   pip install pdfplumber pandas
   ```
2. Coloque o arquivo Anexo_I.pdf na mesma pasta onde o script será executado.
3. Execute o script:
   ```sh
   python dados_ans.py
   ```
4. O arquivo gerado será um arquivo ZIP, com o nome Teste_ASSis_p_N.zip, contendo o arquivo CSV com os dados extraídos.

📂 Estrutura do Projeto
```
Transformacao_Dados_ANS/
│── transformacao_dados_ans.py  # Código principal
│── Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf                 # PDF de entrada
│── Teste_SeuNome.zip           # Arquivo ZIP gerado
│── README.md                   # Documentação do projeto
```
## 📝 Observações
- O arquivo PDF Anexo_I.pdf deve estar presente na mesma pasta que o script.

- O script substituirá OD por Procedimentos Odontológicos e AMB por Procedimentos Ambulatoriais.

---
Desenvolvido para Resolução de teste. 🚀
