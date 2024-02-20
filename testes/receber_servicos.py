import pyautogui
from tkinter import *
import customtkinter
import openpyxl
from tkinter import filedialog
from datetime import date, datetime

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def comecar():
    valor1 = diversos_valor.get()
    valor2 = pagarme_valor.get()
    valor3 = split_valor.get()
    print(valor1, valor2, valor3)

janela = customtkinter.CTk()
janela.title("Hyperlocal")
janela.iconbitmap("./img/icon.ico")
janela.geometry('1280x720')

titulo = customtkinter.CTkLabel(janela, text="Automações para inclusão de contas a receber na serviços", font=("", 25))
titulo.pack(padx=10, pady=20)
titulo2 = customtkinter.CTkLabel(janela, text="Caso não houve um a Receber apenas deixe em branco!", font=("", 20))
titulo2.pack(padx=10, pady=20)

diversos_label = customtkinter.CTkLabel(janela, text="Insira o valor para a Categoria 1.12 de DIVERSOS:\n Insira apenas o valor ex: 2500,00", font=("", 15))
diversos_label.pack(padx=15, pady=2)
diversos_valor = customtkinter.CTkEntry(janela)
diversos_valor.pack(padx=15, pady=10)  # Adiciona uma margem

pagarme_label = customtkinter.CTkLabel(janela, text="Insira o valor para a Categoria 1.48 de PAGARME:\n Insira apenas o valor ex: 2500,00", font=("", 15))
pagarme_label.pack(padx=15, pady=2)
pagarme_valor = customtkinter.CTkEntry(janela)
pagarme_valor.pack(padx=15, pady=10)  # Adiciona uma margem

spli_label = customtkinter.CTkLabel(janela, text="Insira o valor para a Categoria 1.12 de SPLIT:\n Insira apenas o valor ex: 2500,00", font=("", 15))
spli_label.pack(padx=15, pady=2)
spli_valor = customtkinter.CTkEntry(janela)
spli_valor.pack(padx=15, pady=10)  # Adiciona uma margem

botao = customtkinter.CTkButton(janela, text="Começar")#, command=abrir_arquivo)
botao.pack(padx=10, pady=10)

janela.mainloop()
