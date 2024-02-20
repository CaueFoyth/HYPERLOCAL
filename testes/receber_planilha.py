import tkinter as tk
from tkinter import filedialog
import openpyxl

def abrir_arquivo():
    arquivo = filedialog.askopenfilename(filetypes=[("Arquivos Excel", "*.xlsx")])
    if arquivo:
        try:
            workbook = openpyxl.load_workbook(arquivo)
            sheet = workbook.active
            for row in sheet.iter_rows(values_only=True):
                print(row)
        except Exception as e:
            print(f"Erro ao ler o arquivo: {e}")

root = tk.Tk()
root.title("Leitor de Arquivo Excel")

botao = tk.Button(root, text="Selecionar Arquivo", command=abrir_arquivo)
botao.pack()

root.mainloop()