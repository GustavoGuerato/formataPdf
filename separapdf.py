import PyPDF2
import os

caminho_dos_pdf = r'pdf'

with open('pdf/novo_arquivo.pdf', 'rb') as arquivo_pdf:
    reader = PyPDF2.PdfReader(arquivo_pdf)
    num_paginas = len(reader.pages)

    for num_pagina in range(num_paginas):
        escritor = PyPDF2.PdfWriter()
        pagina_atual = reader.pages[num_pagina]
        escritor.add_page(pagina_atual)

        with open(f'novos_pdfs/{num_pagina}.pdf','wb') as novo_pdf:
            escritor.write(novo_pdf)