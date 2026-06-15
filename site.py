from flask import Flask, send_file
import os

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

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
