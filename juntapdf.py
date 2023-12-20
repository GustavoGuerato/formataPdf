import PyPDF2
import os

caminho_dos_pdf = r'pdf'

pdf_novo = PyPDF2.PdfMerger()
for root, dirs, files in os.walk(caminho_dos_pdf):
    for file in files:
        complete_path = os.path.join(root, file)

        arquivo_pdf = open(complete_path, 'rb')
        pdf_novo.append(arquivo_pdf)

with open(f'{caminho_dos_pdf}/novo_arquivo.pdf', 'wb') as meu_novo_pdf:
    pdf_novo.write(meu_novo_pdf)
