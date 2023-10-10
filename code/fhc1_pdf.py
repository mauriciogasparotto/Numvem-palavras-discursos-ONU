# Este é o arquivo para o discurso do presidente FHC no primeiro mandato:

from PyPDF2 import PdfReader

# Nome do arquivo PDF
pdf_file = 'fhc1_onu.pdf'

# Criar um objeto PdfReader
pdf_reader = PdfReader(pdf_file)

# Inicializar uma string vazia para armazenar o texto
discurso_fhc1 = ""

# Loop através de todas as páginas do PDF
for page in pdf_reader.pages:
    # Extrair o texto da página atual
    page_text = page.extract_text()
    
    # Adicionar o texto da página atual ao texto completo
    discurso_fhc1 += page_text

# Imprimir o texto completo
print(discurso_fhc1)


# Escrever o texto completo em um arquivo TXT
with open('discurso_fhc1.txt', 'w', encoding='utf-8') as txt_file:
    txt_file.write(discurso_fhc1)

print("Texto extraído e exportado com sucesso para 'discurso_fhc1.txt'.")