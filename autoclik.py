import pyautogui
import time

def autoclicker(intervalo=0.5):
    """Clica no local onde o mouse está, repetidamente, a cada `intervalo` segundos."""
    print("Autoclicker rodando... pressione Ctrl+C para parar.")
    try:
        while True:
            pyautogui.click()
            time.sleep(intervalo)
    except KeyboardInterrupt:
        print("\nAutoclicker parado.")

if __name__ == "__main__":
    autoclicker(intervalo=0.5)  # clica a cada 0.5 segundo

