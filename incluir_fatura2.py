# pip install OpenCV, pyautogui

import pyautogui
import time

x = 0
while True:
    x, y = pyautogui.locateCenterOnScreen('img/protheus.png', confidence=0.6)
    if x != 0:
        pyautogui.click(x, y)
        x = 0
        break

while True:
    x, y = pyautogui.locateCenterOnScreen('img/recentes.png', confidence=0.8)
    if x != 0:
        pyautogui.click(x, y)
        x = 0
        break

while True:
    x, y = pyautogui.locateCenterOnScreen('img/contas_pagar.png', confidence=0.9) 
    if x != 0:
        time.sleep(3)
        pyautogui.click(x, y)
        x = 0
        break

while True:
    x, y = pyautogui.locateCenterOnScreen('img/apagar_click.png', confidence=0.7)
    if x != 0:
        pyautogui.click(x, y)
        x = 0
        break

