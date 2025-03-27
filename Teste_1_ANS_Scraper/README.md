# ANS Scraper - Teste de Nivelamento

Este projeto é um **teste de nivelamento** que solicita a criação de um script para realizar **web scraping** na página da Agência Nacional de Saúde Suplementar (ANS). O script deve baixar os anexos disponíveis e compactá-los em um arquivo ZIP.

## 🛠️ Requisitos do Teste

O código deve:
1. **Acessar o site** da ANS no seguinte endereço:
   - [ANS - Atualização do Rol de Procedimentos](https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos)
2. **Identificar e baixar os arquivos PDF** listados na página (Anexo I e Anexo II).
3. **Compactar todos os PDFs** baixados em um único arquivo ZIP.
4. **Ser implementado em Python**.

## 📌 Tecnologias Utilizadas
- **Python 3**
- `requests` - Para acessar a página e baixar arquivos
- `BeautifulSoup` - Para analisar e extrair links da página
- `zipfile` - Para compactar os arquivos baixados

## 🚀 Como Executar
1. Instale as dependências:
   ```sh
   pip install requests beautifulsoup4
   ```
2. Execute o script:
   ```sh
   python ans_scraper.py
   ```
3. O arquivo **`anexos.zip`** será gerado na pasta do projeto.

## 📂 Estrutura do Projeto
```
ANS_Scraper/
│── ans_scraper.py  # Código principal
│── anexos.zip      # Arquivo ZIP gerado (depois da execução)
│── README.md       # Documentação do projeto
```

## 📝 Observações
- O script buscará **todos os arquivos PDF** disponíveis na página.
- Caso a estrutura da página da ANS mude, pode ser necessário ajustar o código.

---
Desenvolvido para Resolução de teste. 🚀

