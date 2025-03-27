import pdfplumber
import pandas as pd
import zipfile
import os

def pdf_to_csv():
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        pdf_path = os.path.join(base_dir, '../../data/pdfs/anexo1.pdf')
        csv_path = os.path.join(base_dir, '../../data/csv/dados.csv')
        zip_path = os.path.join(base_dir, '../../data/zip/Teste_Gabriel.zip')

        all_data = []
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                table = page.extract_table()
                if table:
                    all_data.extend(table[1:])

        df = pd.DataFrame(all_data, columns=table[0])
        df.columns = [col.replace('OD', 'Seg. Odontológica').replace('AMB', 'Seg. Ambulatorial') 
                     for col in df.columns]

        os.makedirs(os.path.dirname(csv_path), exist_ok=True)
        df.to_csv(csv_path, index=False, encoding='utf-8-sig')

        os.makedirs(os.path.dirname(zip_path), exist_ok=True)
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            zipf.write(csv_path, arcname='dados.csv')

        print("CSV gerado e compactado!")
    
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    pdf_to_csv()
