# pip install OpenCV, pyautogui

import pyautogui
import time
from os import path

btn6_asset = path.dirname(path.realpath(__file__)) + 'img/apagar_click.png'

x, y = pyautogui.locateCenterOnScreen('img/protheus.png', confidence=0.6)
pyautogui.click(x, y)

x, y = pyautogui.locateCenterOnScreen('img/recentes.png', confidence=0.8)
pyautogui.click(x, y)

x, y = pyautogui.locateCenterOnScreen('img/contas_pagar.png', confidence=0.9) 
time.sleep(3)
pyautogui.click(x, y)

while True:
    btn_found = pyautogui.locateAllOnScreen(btn6_asset, confidence=0.9)
    if btn_found is not None:
        x, y, *extras = btn_found
        pyautogui.click(x,y)
        break
    else:
        print("Imagem não encontrada")
    time.sleep(0.5)

# for i in range(10):
#     time.sleep(0.5)
#     x, y = pyautogui.locateCenterOnScreen('img/apagar_click.png', confidence=0.7)
#     pyautogui.click(x, y)
    