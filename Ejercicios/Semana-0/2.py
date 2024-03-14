import pyautogui
import time 
import keyboard

archivo = open("texto.csv", "r", encoding="utf-8")
texto = archivo.read()
archivo.close()

time.sleep(5)  # espera 5 segundos

while True:
    if keyboard.is_pressed('k'):  # si la tecla 'k' está presionada
        break  # salir del bucle
    pyautogui.click()  # hace clic en la posición actual del cursor
    pyautogui.write(texto)  # escribe el texto
    time.sleep(0.1)  # espera 2 segundos