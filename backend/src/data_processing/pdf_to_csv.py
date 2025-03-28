import pdfplumber
import csv
import zipfile
import os

def pdf_to_csv():
    try:
        base_dir = os.path.dirname(os.path.abspath(__file__))
        pdf_path = os.path.join(base_dir, '../../data/pdfs/anexo1.pdf')
        csv_path = os.path.join(base_dir, '../../data/csv/dados.csv')
        zip_path = os.path.join(base_dir, '../../data/zip/Teste_Gabriel.zip')

        os.makedirs(os.path.dirname(csv_path), exist_ok=True)
        with pdfplumber.open(pdf_path) as pdf, open(csv_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
            writer = None
            header_written = False

            for page in pdf.pages:
                table = page.extract_table()
                if table:
                    if not header_written:
                        header = table[0]
                        header = [col.replace('OD', 'Seg. Odontológica').replace('AMB', 'Seg. Ambulatorial') for col in header]
                        writer = csv.writer(csvfile)
                        writer.writerow(header)
                        header_written = True
                    for row in table[1:]:
                        writer.writerow(row)

        os.makedirs(os.path.dirname(zip_path), exist_ok=True)
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            zipf.write(csv_path, arcname='dados.csv')

        print("CSV gerado e compactado!")
    
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    pdf_to_csv()
