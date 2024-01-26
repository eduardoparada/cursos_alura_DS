from flask import Flask
from textblob import TextBlob

app = Flask (__name__) #criando a variável app, chamando o flask pra criar a API, __name__ é uma variável especial

@app.route('/') #definindo a rota que o usuário da API vai fazer para acessa-la
#Criando a função que vai rodar, ou seja, o response para o usuário
def home():
    return "Minha primeira API"

@app.route('/sentimento/<frase>')
def sentimento (frase):
    tb = TextBlob(frase)
    tb_en=tb.translate(from_lang='pt',to='en')
    polaridade = tb_en.sentiment.polarity
    return 'polaridade: {}'.format(polaridade)

app.run(debug=True)#executável, o 'debug=True' serve pra que toda vez que esse código seja modificado, a própria API entenda
                   #e reinicie a execução
