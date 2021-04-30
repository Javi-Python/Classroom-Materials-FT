from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def index():
    return 'Hola mundo'



@app.route('/ejemplo_01')
def prueba():
    return 'prueba_01'


@app.route('/ejemplo_02')
def prueba_02():
    return 'Esto no me lo esperaba'





app.run("0.0.0.0", 5000, debug = True)