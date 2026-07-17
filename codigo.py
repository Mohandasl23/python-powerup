# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 0.3

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
pyautogui.click(x=1212, y=424)
time.sleep(1)
pyautogui.write("email@email.com")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(3)
pyautogui.click(x=1554, y=377)
pyautogui.press("enter")
pyautogui.click(x=1115, y=293)
pyautogui.press("enter")
pyautogui.write("999999999999")




# time.sleep(3)
# pyautogui.click(x=1671, y=370)
# time.sleep(3)
# pyautogui.click(x=1161, y=294)




# # entrar no link 
# pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
# pyautogui.press("enter")
# time.sleep(3)