import os
import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile

def baixar_pdf(url, nome_arquivo):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(nome_arquivo, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(f"Download concluído: {nome_arquivo}")
    else:
        print(f"Falha ao baixar {nome_arquivo}")

def main():
    url_base = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    response = requests.get(url_base)
    
    if response.status_code != 200:
        print("Falha ao acessar a página")
        return
    
    soup = BeautifulSoup(response.text, "html.parser")
    links = soup.find_all("a", href=True)
    
    pdf_links = [link["href"] for link in links if link["href"].endswith(".pdf")]
    pdf_files = []
    
    for pdf_link in pdf_links:
        pdf_url = pdf_link if pdf_link.startswith("http") else f"https://www.gov.br{pdf_link}"
        nome_arquivo = pdf_url.split("/")[-1]
        baixar_pdf(pdf_url, nome_arquivo)
        pdf_files.append(nome_arquivo)
    
    if pdf_files:
        with ZipFile("anexos.zip", "w") as zipf:
            for pdf in pdf_files:
                zipf.write(pdf)
                os.remove(pdf)  # Remove os PDFs após a compactação
        print("Todos os anexos foram compactados em anexos.zip")
    else:
        print("Nenhum anexo encontrado.")

if __name__ == "__main__":
    main()
