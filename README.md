# Manipulação Avançada de PDFs com PyPDF2

Este repositório oferece scripts em Python para simplificar operações avançadas em arquivos PDF, utilizando a poderosa biblioteca PyPDF2. Agilize tarefas como mesclagem de múltiplos PDFs em um único documento ou extração de páginas para arquivos separados.

## Funcionalidades

### Mesclagem de PDFs

```python
import PyPDF2
import os
```
# Caminho do diretório contendo os PDFs a serem mesclados
caminho_dos_pdfs = r'pdf'

# Criação do arquivo resultante da mesclagem
with open('pdf/novo_arquivo.pdf', 'rb') as arquivo_pdf:
    reader = PyPDF2.PdfReader(arquivo_pdf)
    num_paginas = len(reader.pages)

    escritor = PyPDF2.PdfWriter()
    for num_pagina in range(num_paginas):
        pagina_atual = reader.pages[num_pagina]
        escritor.add_page(pagina_atual)

        # Criação de arquivos individuais para cada página mesclada
        with open(f'novos_pdfs/{num_pagina}.pdf', 'wb') as novo_pdf:
            escritor.write(novo_pdf)
