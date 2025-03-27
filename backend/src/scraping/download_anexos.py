import requests
from bs4 import BeautifulSoup
import zipfile
import os

def download_anexos():
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }

        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')

        pdf_links = [
            link['href'] for link in soup.select('a.internal-link[href*="Anexo_I"], a.internal-link[href*="Anexo_II"]')
            if link.get('href') and ('Anexo_I' in link['href'] or 'Anexo_II' in link['href']) and link['href'].endswith('.pdf')
        ]

        if len(pdf_links) < 2:
            raise ValueError("Não foram encontrados os dois anexos necessários")

        base_dir = os.path.dirname(os.path.abspath(__file__))
        pdf_dir = os.path.join(base_dir, '../../data/pdfs')
        zip_dir = os.path.join(base_dir, '../../data/zip')
        
        os.makedirs(pdf_dir, exist_ok=True)
        os.makedirs(zip_dir, exist_ok=True)

        for index, link in enumerate(pdf_links[:2], 1):
            try:
                file_name = f"anexo{index}.pdf"
                file_path = os.path.join(pdf_dir, file_name)
                
                print(f"Baixando {link}...")
                response = requests.get(link, headers=headers, stream=True, timeout=20)
                response.raise_for_status()

                with open(file_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)

            except Exception as download_error:
                print(f"Falha no download de {link}: {str(download_error)}")
                raise

        zip_path = os.path.join(zip_dir, 'anexos.zip')
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for i in range(1, 3):
                pdf_file = os.path.join(pdf_dir, f'anexo{i}.pdf')
                if os.path.exists(pdf_file):
                    zipf.write(pdf_file, arcname=f'anexo{i}.pdf')
                else:
                    print(f"Aviso: {pdf_file} não encontrado para compactação")

        print("Processo concluído com sucesso!")

    except Exception as e:
        print(f"Erro crítico: {str(e)}")
        exit(1)

if __name__ == "__main__":
    download_anexos()
