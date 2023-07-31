import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.click(x=28, y=1067)
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("tab")
pyautogui.press("enter")

pyautogui.click(x=69, y=193)
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(5)
with open('incluir_fatura.csv', 'r') as arquivo:
        for linha in arquivo:
                

                # Prefixo
                codigo = linha.split(';')[1]
                if codigo == "":
                        pyautogui.press("tab")
                else:
                        pyautogui.write(codigo)

                # Número do título
                codigo = linha.split(';')[2]
                num_codigo = len(codigo)
                if num_codigo == 9:
                        pyautogui.write(codigo)
                else:
                        pyautogui.write(codigo)
                        pyautogui.press("tab")

                # Parcela
                codigo = linha.split(';')[3]
                num_codigo = len(codigo)
                if codigo == "":
                        pyautogui.press("tab")
                elif num_codigo == 1:
                        codigo = codigo + " "
                        pyautogui.write(codigo)
                else:
                        pyautogui.write(codigo)

                # Tipo
                codigo = linha.split(';')[4]
                num_codigo = len(codigo)
                if num_codigo == 2:
                        codigo = codigo + " "
                        pyautogui.write(codigo)
                else:
                        pyautogui.write(codigo)  

                # Natureza
                codigo = linha.split(';')[5]
                pyautogui.write(codigo)
                pyautogui.press("tab")

                # Fornecedor
                codigo = linha.split(';')[6]
                pyautogui.write(codigo)

                # Loja
                codigo = linha.split(';')[7]
                pyautogui.write(codigo)
                pyautogui.press("tab")

                # Vencimento
                codigo = linha.split(';')[8]
                pyautogui.write(codigo) 
                pyautogui.press("tab")

                # Valor
                codigo = linha.split(';')[9]
                pyautogui.write(codigo)    

                # Historico
                # codigo = linha.split(';')[10]
                # if codigo == "":
                #         pyautogui.press("tab")
                # else:
                #         pyautogui.write(codigo)

                pyautogui.click(x=1850, y=153)

                time.sleep(5) 