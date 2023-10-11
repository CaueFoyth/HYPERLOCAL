# pip install OpenCV, pyautogui, CustomTkinter

import pyautogui
import time
from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def incuir_fatura():

    pyautogui.useImageNotFoundException()

    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen('img/protheus.png', confidence=0.9)
            pyautogui.click(x, y)
            break
        except pyautogui.ImageNotFoundException:
            pass

    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen('img/recentes.png', confidence=0.8)
            pyautogui.click(x, y)
            break
        except pyautogui.ImageNotFoundException:
            pass

    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen('img/contas_pagar.png', confidence=0.9) 
            break
        except pyautogui.ImageNotFoundException:
            pass

    while True:
        try:
            veri = pyautogui.locateCenterOnScreen('img/forn.png', confidence=0.7)
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

janela = customtkinter.CTk()
janela.title("Hyperlocal")
janela.iconbitmap("./img/icon.ico")
janela.geometry('1280x720')

titulo = customtkinter.CTkLabel(janela, text="Automações Hyperlocal", font=("", 25))
titulo.pack(padx=10, pady=20)

botao = customtkinter.CTkButton(janela, text="Inclusão de faturas", command=incuir_fatura)
botao.pack(padx=10, pady=10)

janela.mainloop()

