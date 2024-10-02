#Biblioteca SpaCy   
#Biblioteca para Processamento de linguagem natural
#download do modelo de lingaugem PT_BR

import spacy 
import spacy.displacy

#carregar o modelo de linguagem
spacyPT = spacy.load('pt_core_news_sm')

#processamento de texto

frase = spacyPT('Eu vi o menino com o telescópio')
frase1 = spacyPT('Eu vi o menino que carregava o telescópio')

print(frase)
print(' ')
#cada frase é uma sequência de tokens, token é cada classe da palavra e nós podemos itera sobre cada token
#TOKENIZAR
for token in frase:
    
    print(token)
    print(' ')
#Exibir as categorias morfossintáticas de cada token
    #pos_ -> Part of speech
for token in frase:
     print(f'{token.text}:{token.pos_}')

#Visualizar as dependências das categorias morfossintáticas
spacy.displacy.serve([frase, frase1], style='dep')

