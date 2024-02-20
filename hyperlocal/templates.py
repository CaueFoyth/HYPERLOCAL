from tkinter import *
import customtkinter
import openpyxl
from tkinter import filedialog

class TelaPrincipal():
    # Customização do layout
    def janela():
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")

        janela = customtkinter.CTk()
        janela.title("Hyperlocal")
        janela.iconbitmap("./hyperlocal/img/icon.ico")
        screen_width = janela.winfo_screenwidth()
        screen_height = janela.winfo_screenheight()
        janela.geometry(f"{screen_width}x{screen_height}")

        titulo = customtkinter.CTkLabel(janela, text="Automações Hyperlocal", font=("", 25))
        titulo.pack(padx=10, pady=20)

        botao = customtkinter.CTkButton(janela, text="Selecionar Arquivo")#, command=abrir_arquivo)
        botao.pack(padx=10, pady=10)

        janela.mainloop()