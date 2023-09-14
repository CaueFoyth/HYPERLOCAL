# pip install OpenCV, pyautogui

import pyautogui
import time

pyautogui.useImageNotFoundException()

while True:
    try:
        x, y = pyautogui.locateCenterOnScreen('img/protheus.png', confidence=0.9)
        pyautogui.click(x, y)
        break
    except pyautogui.ImageNotFoundException:
        pass


# x, y = pyautogui.locateCenterOnScreen('img/protheus.png', confidence=0.9)
# pyautogui.click(x, y)

while True:
    try:
        x, y = pyautogui.locateCenterOnScreen('img/recentes.png', confidence=0.8)
        pyautogui.click(x, y)
        break
    except pyautogui.ImageNotFoundException:
        pass

# x, y = pyautogui.locateCenterOnScreen('img/recentes.png', confidence=0.8)
# pyautogui.click(x, y)
# time.sleep(1)

while True:
    try:
        x, y = pyautogui.locateCenterOnScreen('img/contas_pagar.png', confidence=0.9) 
        time.sleep(2)
        pyautogui.click(x, y)
        break
    except pyautogui.ImageNotFoundException:
        pass

while True:
    try:
        x, y = pyautogui.locateCenterOnScreen('img/apagar_click.png', confidence=0.7) 
        pyautogui.click(x, y)
        break
    except pyautogui.ImageNotFoundException:
        pass

pyautogui.press("tab")
pyautogui.press("enter")     