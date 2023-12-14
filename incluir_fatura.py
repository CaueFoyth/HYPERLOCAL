# pip install OpenCV, pyautogui, CustomTkinter, openpyxl
import pyautogui
import time
from tkinter import *
import customtkinter
import openpyxl
from tkinter import filedialog
from datetime import date, datetime

# Customização do layout
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

#Chegar a página de contas a pagar
def chegar_inclusao():
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

#Inclusão de fatura
def incluir_cp():
    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen('img/prefixo.png', confidence=0.7) 
            pyautogui.press("tab")
            pyautogui.write(no_tit)
            break
        except pyautogui.ImageNotFoundException:
            pass

    pyautogui.press("tab")

    num_codigo = len(tipo)
    if num_codigo == 2:
            pyautogui.write(tipo)
            pyautogui.press("tab")
    else:
            pyautogui.write(tipo)

    pyautogui.write(natureza)
    pyautogui.press("tab")
    
    global fornecedor_codigo
    print(fornecedor_codigo)
    num_codigo = len(str(fornecedor_codigo))
    if num_codigo >= 14:
        fornecedor_codigo = fornecedor_codigo[:8]
        pyautogui.write(fornecedor_codigo)
    else:
        fornecedor_codigo = fornecedor_codigo[:7]
        pyautogui.write(f"0{fornecedor_codigo}")
    
    pyautogui.press("tab")
    pyautogui.press("tab")

    print(data_vencimento)
    pyautogui.write(f"{data_vencimento}")
    pyautogui.press("tab")
    pyautogui.write(f"{valor}")

    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen('img/salvar.png', confidence=0.9)
            time.sleep(1) 
            pyautogui.click(x, y)
            break
        except pyautogui.ImageNotFoundException:
            pass
            time.sleep(1) 

#Abrir o protheus
def abrir_protheus():
    while True:
        try:
            x, y = pyautogui.locateCenterOnScreen('img/protheus.png', confidence=0.9)
            pyautogui.click(x, y)
            break
        except pyautogui.ImageNotFoundException:
            pass

#Troca de banco
def banco_troca(cod_banco):
    global banco_antigo
    if banco_antigo != banco:
        while True:
            try:
                x, y = pyautogui.locateCenterOnScreen('img/totvs.png', confidence=0.7)
                pyautogui.click(x, y)
                break
            except pyautogui.ImageNotFoundException:
                pass
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.write(cod_banco)
        time.sleep(1)
        pyautogui.press("enter")
        pyautogui.press("enter")
        banco_antigo = banco

#Verificar o banco
def verifica_banco():
    if banco == "Solutions Itaú":
        cod_banco = "0201"
    if banco == "Serviços Itaú":
        cod_banco = "0101"
    if banco == "Franqueadora Itaú":
        cod_banco = "0301"
    print(cod_banco)
    banco_troca(cod_banco)

# Função para iniciar o a inclusão de faturas
def abrir_arquivo():
    global numero
    global banco_antigo
    banco_antigo = ""
    data = date.today()
    data_str = data.strftime('%Y-%m-%d')
    data_format = data_str.replace("-", "")
    numero = 0
    arquivo = filedialog.askopenfilename(filetypes=[("Arquivos Excel", "*.xlsx")])
    pyautogui.useImageNotFoundException()

    abrir_protheus()

    if arquivo:
        try:
            workbook = openpyxl.load_workbook(arquivo)
            sheet = workbook.active
            first_row_skipped = False
            for row in sheet.iter_rows(values_only=True):
                if not first_row_skipped:
                    first_row_skipped = True
                    continue
                
                global banco, fornecedor, valor, data_vencimento, natureza_noformat, inserir, tipo, fornecedor_codigo, no_tit, natureza
                banco = row[0]
                fornecedor = row[1]
                valor = row[2]
                data_vencimento = row[3]
                natureza_noformat = row[8]
                inserir = row[9]
                tipo = row[10]
                fornecedor_codigo = row[11]

                numero = int(numero) + 1
                print(numero)
                no_tit = f"{data_format}{numero}"

                partes = natureza_noformat.split(" ", 1)  # Divide a string em duas partes no primeiro espaço encontrado

                data_vencimento = data_vencimento.strftime('%Y-%m-%d')
                data_vencimento = data_vencimento.replace("-", "")
                data_vencimento = data_vencimento.split(" ", 1)[0] 
                data_vencimento = datetime.strptime(data_vencimento, '%Y%m%d').strftime('%d%m%Y')
                if len(partes) > 1:
                    natureza = partes[0]  # Pega a primeira parte (antes do espaço)
                else:
                    natureza = natureza_noformat  # Se não houver espaço na string, resultado é a própria string original

                if inserir.lower() == "não":
                    print(inserir)
                    continue
                else:
                    #verifica_banco()
                    #chegar_inclusao()
                    #incluir_cp()

        except Exception as e:
            print(f"Erro ao ler o arquivo: {e}")

# Setando propriedades do aplicativo              
janela = customtkinter.CTk()
janela.title("Hyperlocal")
janela.iconbitmap("./img/icon.ico")
janela.geometry('1280x720')

titulo = customtkinter.CTkLabel(janela, text="Automações Hyperlocal", font=("", 25))
titulo.pack(padx=10, pady=20)

botao = customtkinter.CTkButton(janela, text="Selecionar Arquivo", command=abrir_arquivo)
botao.pack(padx=10, pady=10)

janela.mainloop()

