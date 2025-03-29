import pdfplumber
import csv
import zipfile
import os

def pdf_to_csv():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(base_dir, '../../data/pdfs/anexo1.pdf')
    csv_path = os.path.join(base_dir, '../../data/csv/dados.csv')
    zip_path = os.path.join(base_dir, '../../data/zip/Teste_Gabriel.zip')

    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    os.makedirs(os.path.dirname(zip_path), exist_ok=True)

    try:
        with pdfplumber.open(pdf_path) as pdf:
            tables = []
            for page in pdf.pages:
                tables.extend(page.extract_tables())
            with open(csv_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
                writer = csv.writer(csvfile)
                if tables:
                    header = [col.replace('OD', 'Seg. Odontológica').replace('AMB', 'Seg. Ambulatorial') for col in tables[0][0]]
                    writer.writerow(header)
                    writer.writerows([row for table in tables for row in table[1:]])

        with zipfile.ZipFile(zip_path, 'w') as zipf:
            zipf.write(csv_path, arcname='dados.csv')

        print("CSV gerado e compactado!")
    
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    pdf_to_csv()

