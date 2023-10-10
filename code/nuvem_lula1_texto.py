import numpy as np
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image  # Importe o módulo Image do PIL

# Função para remover preposições, artigos e advérbios
def remove_stopwords(texto):
    stopwords = ["a", "o", "as", "os", 
                "um", "uma", "uns", "umas", 
                "de", "da", "do", "das", "dos", 
                "no", "na", "nos", "nas", "em", 
                "por", "para", "com", "sem", "sob", 
                "sobre", "ante", "até", "após", "com", 
                "contra", "entre", "desde", "perante", 
                "mas", "porque", "pois", "assim", 
                "também", "então", "agora", "aqui", 
                "ali", "bem", "mal", "não", "sim",
                "e", "mais", "se", "todos", "todas",
                "que", "é", "como", "à", "está", "nossa",
                "nosso", "há", "pela", "pelo", "já", "que", "às", "são",
                "sua", "seu", "ao", "onde", "quando", "ao", 'hoje', 'precisam',
                'aquelas', 'tenho', 'nossos', 'se', 'ou', 'ser', 'aos', 'só', 
                'desta', 'se', 'que', 'todo', 'tudo', 'toda', 'todos', 'todas', 
                'foi', 'foram', 'era', 'é', 'pode', 'se', 'meu', 'essa',
                'forma', 'seus', 'esse', 'ano', 'estamos', 'nos', 'tem', 
                'nós']
    palavras = texto.split()
    palavras_sem_stopwords = [palavra for palavra in palavras if palavra.lower() not in stopwords]
    return " ".join(palavras_sem_stopwords)

# Ler o arquivo de texto
with open('discurso_lula1.txt', 'r', encoding='utf-8') as txt_file:
    discurso = txt_file.read()

# Remover preposições, artigos e advérbios
discurso_sem_stopwords = remove_stopwords(discurso)

# Abrir a imagem/máscara e inserir na nuvem:
imagem_mascara = np.array(Image.open('cloud_copia.png'))
imagem_mascara

# Criar a nuvem de palavras
wordcloud = WordCloud(width=1223, height=689,
                    background_color='#000000',
                    mask=imagem_mascara,
                    colormap='Set1',
                    max_font_size=100,
                    max_words=50,
                    prefer_horizontal=1,
                    relative_scaling=0.5,
                    scale=3,
                    random_state=42).generate(discurso_sem_stopwords)

# Exibir a nuvem de palavras
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()