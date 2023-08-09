# pip install OpenCV, pyautogui

import pyautogui
import time

x, y = pyautogui.locateCenterOnScreen('img/protheus.png', confidence=0.6)
pyautogui.click(x, y)

x, y = pyautogui.locateCenterOnScreen('img/recentes.png', confidence=0.8)
pyautogui.click(x, y)

x, y = pyautogui.locateCenterOnScreen('img/contas_pagar.png', confidence=0.9) 
time.sleep(3)
pyautogui.click(x, y)

for i in range(10):
    time.sleep(0.5)
    x, y = pyautogui.locateCenterOnScreen('img/apagar_click.png', confidence=0.7)
    pyautogui.click(x, y)
    