"""
Site de controle remoto do carrinho - backend em Flask.
 
Camadas do projeto:
 
    Navegador (HTML/JS)  --HTTP-->  Flask (este arquivo)  --Serial-->  Arduino (C++)
 
A biblioteca Python usada para "conversar" com o Arduino e a pyserial
(modulo `serial`). Ela escreve bytes na porta USB exatamente como o
Monitor Serial da IDE do Arduino faz - so que agora quem envia esses
bytes e o nosso proprio codigo, disparado pelos cliques no site.
 
Modo simulacao: se o Arduino nao for encontrado na porta configurada
(por exemplo, se ele ainda nao estiver plugado), o site continua
funcionando normalmente - os comandos so aparecem no terminal em vez
de serem enviados de verdade. Isso deixa testar o site inteiro sem
precisar do hardware por perto.
"""
 
from flask import Flask, render_template, jsonify
import serial
import time
import os
 
app = Flask(__name__)
 
# ---- Configuracao da porta serial ----
# Windows costuma ser algo como "COM3"; Linux/Mac, "/dev/ttyUSB0" ou "/dev/ttyACM0".
# Pode trocar sem mexer no codigo: defina a variavel de ambiente PORTA_SERIAL.
PORTA_SERIAL = os.environ.get("PORTA_SERIAL", "COM3")
BAUD_RATE = 9600
CAMINHO_INO = os.path.join(os.path.dirname(__file__), "arduino", "carrinho_controle.ino")
 
arduino = None
modo_simulacao = False
 
 
def conectar_arduino():
    global arduino, modo_simulacao
    try:
        arduino = serial.Serial(PORTA_SERIAL, BAUD_RATE, timeout=1)
        time.sleep(2)  # o Arduino reinicia ao abrir a porta serial - precisa desse tempo
        modo_simulacao = False
        print(f"Conectado ao Arduino em {PORTA_SERIAL}")
    except Exception as erro:
        print(f"Nao consegui conectar em {PORTA_SERIAL} ({erro}). Rodando em modo simulacao.")
        arduino = None
        modo_simulacao = True
 
 
conectar_arduino()
 
 
@app.route("/")
def index():
    return render_template("index.html")
 
 
@app.route("/api/status")
def status():
    return jsonify({"simulacao": modo_simulacao, "porta": PORTA_SERIAL})
 
 
@app.route("/api/codigo")
def codigo():
    """Devolve o .ino de verdade, para o site sempre mostrar o codigo atual."""
    try:
        with open(CAMINHO_INO, "r", encoding="utf-8") as f:
            conteudo = f.read()
        return jsonify({"codigo": conteudo})
    except FileNotFoundError:
        return jsonify({"codigo": "// arduino/carrinho_controle.ino nao encontrado"}), 404
 
 
@app.route("/api/comando/<cmd>")
def comando(cmd):
    cmd = cmd.upper()
    if cmd not in ("F", "B", "L", "R", "S"):
        return jsonify({"erro": "comando invalido"}), 400
 
    if arduino and not modo_simulacao:
        arduino.write(cmd.encode())
    else:
        print(f"[SIMULACAO] comando enviado: {cmd}")
 
    return jsonify({"comando": cmd, "simulacao": modo_simulacao})
 
 
if __name__ == "__main__":
    app.run(debug=True, port=5000)

