# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 0.5

# Passo 1: Entrar no sistema da empresa
# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(3)
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
# Fazer uma pausa maior para garantir que o site carregue
time.sleep(3)

# Passo 2: Fazer Login
# clicar no campo email
pyautogui.click(x=1294, y=392)
time.sleep(1)
pyautogui.write("email@email.com")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=1554, y=377)
pyautogui.press("enter")


# Passo 3: Abrir a base de dados (importar o arquivo)
# pip install pandas openpyxl
import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela.to_string())

for linha in tabela.index:
    # Passo 4: Cadastrar 1º produto
    pyautogui.click(x=1196, y=288)
    # Fazer uma pausa maior para garantir que o site carregue
    time.sleep(2)
    pyautogui.press("enter")
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs =(str(tabela.loc[linha, "obs"]))
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")

    # Voltar para o inicio para cadastrar o proximo
    pyautogui.scroll(200)

   
# Passo 5: Repetir os passos 4 até acabar a lista de produtos






