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

@app.route("/admin")
def admin():
    return send_file("admin.html")

@app.route("/webdev")
def webdev():
    return send_file("webdev.html")

@app.route("/seguranca")
def seguranca():
    return send_file("seguranca.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
