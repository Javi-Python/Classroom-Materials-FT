from flask import Flask, request
import tools.getdata as get
import json
from flask import jsonify
import postdata as pos
import requests 

app = Flask(__name__)

@app.route("/")
def index():
    readme_file = open("Readme.md", "r")
    md_template = markdown.markdown(
        readme_file.read(), extendions=["fenced_code"]
    ) 
    return md_template



@app.route('/frases')
def frases():
    frases = get.frase()
    return jsonify(frases)


@app.route('/frases/<name>')
def frasespersonaje(name):
    frases = get.frase(name)
    return jsonify(frases)


@app.route('/nuevafrase', methods = ['POST'])
def insertamensaje():
    escena = request.form.get('scene')
    personaje = request.form.get('character_name')
    frase = request.form.get('dialogue')
    pos.insertamensaje(escena, personaje, frase)
    return 'Ya se han subido tus datos. '

app.run(debug=True)