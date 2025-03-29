import requests
import os
import zipfile
import io
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

def download_file(url, path):
    response = requests.get(url)
    with open(path, "wb") as f:
        f.write(response.content)

def download_and_extract_zip(url, csv_dir):
    response = requests.get(url)
    with zipfile.ZipFile(io.BytesIO(response.content), "r") as zipf:
        for file in zipf.namelist():
            if file.endswith(".csv"):
                with zipf.open(file) as csvfile:
                    df = pd.read_csv(csvfile, sep=";")
                    df["VL_SALDO_INICIAL"] = df["VL_SALDO_INICIAL"].str.replace(",", ".")
                    df["VL_SALDO_FINAL"] = df["VL_SALDO_FINAL"].str.replace(",", ".")
                    df.to_csv(os.path.join(csv_dir, file), index=False, sep=";")

def download_ans_data():
    base_url = "https://dadosabertos.ans.gov.br/FTP/PDA/"
    base_dir = os.path.dirname(os.path.abspath(__file__))
    csv_dir = os.path.join(base_dir, '../../data/csv/')
    os.makedirs(csv_dir, exist_ok=True)

    operadoras_url = base_url + "operadoras_de_plano_de_saude_ativas/Relatorio_cadop.csv"
    download_file(operadoras_url, os.path.join(csv_dir, "operadoras.csv"))

    with ThreadPoolExecutor() as executor:
        tasks = []
        for year in range(2023, 2025):
            for quarter in range(1, 5):
                zip_filename = f"{quarter}T{year}.zip"
                demonstracoes_url = base_url + f"demonstracoes_contabeis/{year}/{zip_filename}"
                tasks.append(executor.submit(download_and_extract_zip, demonstracoes_url, csv_dir))
        for task in tasks:
            task.result()

    print("Arquivos baixados e extraídos com sucesso!")

if __name__ == "__main__":
    download_ans_data()

