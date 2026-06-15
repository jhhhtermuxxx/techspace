from flask import Flask, send_file

app = Flask(__name__)
visitas = 0

@app.route("/")
def home():
    global visitas
    visitas += 1
    return send_file("index.html")

@app.route("/historia")
def historia():
    return send_file("historia.html")

@app.route("/linguagens")
def linguagens():
    return send_file("linguagens.html")

@app.route("/visitas")
def contar():
    return str(visitas)

app.run(debug=True, port=3000)
