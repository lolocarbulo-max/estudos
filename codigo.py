import pyautogui
import time
import random

# Desativa a trava de segurança do pyautogui
pyautogui.FAILSAFE = False

print("Bot AFK iniciado. Pressione Ctrl+C no terminal para parar.")

while True:
    # Gera coordenadas aleatórias dentro de uma tela comum (ex: 1920x1080)
    x = random.randint(100, 700)
    y = random.randint(100, 700)
    
    # Move o mouse para a posição gerada
    pyautogui.moveTo(x, y, duration=0.5)
    
    # Aguarda um tempo aleatório entre 1 e 5 segundos
    tempo_espera = random.randint(1, 5)
    time.sleep(tempo_espera)

