# Este é o arquivo para o discurso do presidente Collor:

from PyPDF2 import PdfReader

# Nome do arquivo PDF
pdf_file = 'collor_onu.pdf'

# Criar um objeto PdfReader
pdf_reader = PdfReader(pdf_file)

# Inicializar uma string vazia para armazenar o texto
discurso_collor = ""

# Loop através de todas as páginas do PDF
for page in pdf_reader.pages:
    # Extrair o texto da página atual
    page_text = page.extract_text()
    
    # Adicionar o texto da página atual ao texto completo
    discurso_collor += page_text

# Imprimir o texto completo
print(discurso_collor)


# Escrever o texto completo em um arquivo TXT
with open('discurso_collor.txt', 'w', encoding='utf-8') as txt_file:
    txt_file.write(discurso_collor)

print("Texto extraído e exportado com sucesso para 'discurso_collor.txt'.")