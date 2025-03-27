import requests
import os
import zipfile
import io

def download_ans_data():
    base_url = "https://dadosabertos.ans.gov.br/FTP/PDA/"
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    csv_dir = os.path.join(base_dir, '../../data/csv/')
    
    os.makedirs(csv_dir, exist_ok=True)
    
    operadoras_url = base_url + "operadoras_de_plano_de_saude_ativas/Relatorio_cadop.csv"
    response = requests.get(operadoras_url)
    with open(os.path.join(csv_dir, "operadoras.csv"), "wb") as f:
        f.write(response.content)
    
    for year in range(2023, 2025):
        for quarter in range(1, 5):
            zip_filename = f"{quarter}T{year}.zip"
            demonstracoes_url = base_url + f"demonstracoes_contabeis/{year}/{zip_filename}"
            response = requests.get(demonstracoes_url)
            
            with zipfile.ZipFile(io.BytesIO(response.content), "r") as zipf:
                for file in zipf.namelist():
                    if file.endswith(".csv"):
                        with zipf.open(file) as csvfile:
                            with open(os.path.join(csv_dir, file), "wb") as f:
                                f.write(csvfile.read())
    
    print("Arquivos baixados e extraídos com sucesso!")

if __name__ == "__main__":
    download_ans_data()
