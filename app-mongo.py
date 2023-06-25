from flask import Flask, jsonify, render_template, request, redirect
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__, template_folder = 'templates')
client = MongoClient()
client = pymongo.MongoClient("localhost", 27017)
db = client["agenda"]
contatos = db["contatos"]


#apagar = contatos.delete_many({})

@app.route('/')
def index():
    lista_contatos = []
    for contato in contatos.find():
        lista_contatos.append(contato)
    return render_template('index.html', contatos=lista_contatos)

@app.route('/criarContato')
def criarContato():
    return render_template('criarContato.html')

@app.route('/criarContato', methods=['POST'])
def submit_form():
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    telefone = request.form['telefone']
    email = request.form['email']
    contato = {"nome": nome, "sobrenome": sobrenome, "telefone": telefone, "email":email}
    contatos.insert_one(contato)
    return redirect('/')

@app.route('/editarContato/<id>', methods=['GET'])
def editarContato(id):
    contato = contatos.find_one({"_id": ObjectId(id)})
    return render_template('editarContato.html', contato=contato)

@app.route('/editarContato/<id>', methods=['POST'])
def atualizarContato(id):
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    telefone = request.form['telefone']
    email = request.form['email']
    contatos.update_one({"_id": ObjectId(id)}, {"$set": {"nome": nome, "sobrenome": sobrenome, "telefone": telefone, "email": email}})
    return redirect('/')

@app.route('/excluirContato/<id>')
def excluirContato(id):
    contatos.delete_one({"_id":ObjectId(id)})
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)