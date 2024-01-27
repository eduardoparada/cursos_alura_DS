from flask import Flask, request, jsonify #request faz um request JSON e o jsonify retorna um valor de arquivo JSON
from textblob import TextBlob

#Criando toda a estrutura de código para nova api COTACAO   
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('casas.csv',sep=',')
coluna =["tamanho", "ano","garagem"]
x= df.drop('preco', axis =1)
y = df['preco']
x_treino, x_teste, y_treino, y_teste = train_test_split(x,y,test_size=0.3, random_state = 42)
modelo = LinearRegression()
modelo.fit(x_treino,y_treino)


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

@app.route('/cotacao/', methods =['POST'])

def cotacao():
    dados = request.get_json()
    dados_input = [dados[col]for col in coluna]
    preco = modelo.predict([dados_input])
    return jsonify(preco=preco[0])#jsonify retorna valor em JSON


app.run(debug=True)#executável, o 'debug=True' serve pra que toda vez que esse código seja modificado, a própria API entenda
                   #e reinicie a execução
