import os
import pdfplumber
import pandas as pd
from zipfile import ZipFile

def extrair_tabela(pdf_path):
    dados = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tabelas = page.extract_tables()
            for tabela in tabelas:
                for linha in tabela:
                    dados.append(linha)
    return dados

def salvar_csv(dados, csv_path):
    colunas = dados[0]  
    df = pd.DataFrame(dados[1:], columns=colunas)
    
   
    df.replace({
        "OD": "Procedimentos Odontológicos",
        "AMB": "Procedimentos Ambulatoriais"
    }, inplace=True)
    
    df.to_csv(csv_path, index=False, encoding='utf-8')

def compactar_csv(csv_path, zip_path):
    with ZipFile(zip_path, "w") as zipf:
        zipf.write(csv_path)
        os.remove(csv_path)  

def main():
    pdf_path = "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"  
    csv_path = "dados_extraidos.csv"
    zip_path = "Teste_Assis_p_n.zip"  
    
    print("Extraindo dados do PDF...")
    dados = extrair_tabela(pdf_path)
    
    if dados:
        print("Salvando em CSV...")
        salvar_csv(dados, csv_path)
        
        print("Compactando arquivo...")
        compactar_csv(csv_path, zip_path)
        print(f"Processo concluído! Arquivo salvo como {zip_path}")
    else:
        print("Nenhuma tabela encontrada no PDF.")

if __name__ == "__main__":
    main()
