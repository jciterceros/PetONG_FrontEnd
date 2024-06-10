from flask import Flask, render_template
# , request, redirect, url_for
# from flask import Flask, request, jsonify
# import requests
import json
from urllib import request
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

n_point_api = "https://api.npoint.io/e6b1dd077c2a1f6b50eb"
my_email = os.environ.get('MY_EMAIL')
my_password = os.environ.get('MY_PASSWORD')

# Rota principal
@app.route('/')
def index():
    response =  request.urlopen("https://petongbackend-production.up.railway.app/posts")
    posts = json.loads(response.read())
    return render_template('indexnew.html', posts=posts)

# Rota para a página adotar
@app.route('/adotar.html')
def adotar():
    response =  request.urlopen("https://petongbackend-production.up.railway.app/posts")
    posts = json.loads(response.read())
    return render_template('adotar.html', posts=posts)

# Rota para a página sobre
@app.route('/sobre.html')
def sobre():
    return render_template('sobre.html')

# Rota para a página eventos
@app.route('/eventos.html')
def eventos():
    response =  request.urlopen("https://petongbackend-production.up.railway.app/posts")
    posts = json.loads(response.read())
    return render_template('eventos.html', posts=posts)

# Rota para a página contato
@app.route('/contato.html')
def contato():
    return render_template('contato.html')

# Rota para a página login
@app.route('/login.html')
def login():
    return render_template('login.html')


# Fazendo a requisição da API usando a biblioteca urllib
# response = request.urlopen(n_point_api)
# data  = json.loads(response.read())

# Renderizando o template index.html e passando os dados da API
# return render_template('index.html', input_data=data)


# @app.route('/index.html')
# def home():
#     responses = requests.get(n_point_api).json()
#     return render_template("index.html", input_data=responses)


# @app.route('/eventos.html')
# def hom():
#     responses = requests.get(n_point_api).json()
#     return render_template("eventos.html", input_data=responses)

# @app.route('/adotar.html')
# def adot():
#     responses = requests.get(n_point_api).json()
#     return render_template("adotar.html", input_data=responses)

# @app.route('/sobre.html')
# def sob():
#     return render_template("sobre.html")

# @app.route('/login.html')
# def logi():
#     return render_template("login.html")


# @app.route('/contato.html')
# def contato():
#     return render_template("contato.html", message_sent=True)


# @app.route("/<int:blog_id>")
# def blog_post(blog_id):
#     responses = requests.get("https://api.npoint.io/1158833654ad0cd9f17f").json()
#     for response in responses:
#         if response["id"] == blog_id:
#             post_title = response["title"]
#             post_subtitle = response["subtitle"]
#             post_body = response["body"]
#         else:
#             pass
#     return render_template("post.html", post1_t=post_title, post1_st=post_subtitle, post1_b=post_body)


# @app.route('/form-entry', methods=["POST"])
# def receive_data():
#     user_name = request.form["nome"]
#     user_email = request.form["email"]
#     user_phone = request.form["Numero"]
#     user_message = request.form["mensagem"]
#     send_email(user_name, user_email, user_phone, user_message)
#     return render_template("contato.html", message_sent=False)



# @app.route('/cadastro', methods=['POST'])
# def cadastrar_animal():
#     nome = request.form['nome']
#     especie = request.form['especie']
#     # Salvando os dados do animal de estimação no banco de dados
#     return 'Animal cadastrado com sucesso!'

# @app.route('/buscar', methods=['GET'])
# def buscar_animal():
#     nome = request.args.get('nome')
#     # Buscando o animal de estimação no banco de dados
#     return f'O animal de estimação {nome} foi encontrado.'



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)
