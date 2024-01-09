# Passo a passo do projeto

# passo 1 - entrar no sistema da empresa

import pyautogui
import time
 # # https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.PAUSE = 1 # pausa de 1 segundo a cada comando
#clicar : pyautogui.click(x,y)
#digitar: pyautogui.write('texto')
#pressionar uma tela: pyautogui.press('enter')
#apertar: pyautogui.hotkey

#apertar a tecla do windows
pyautogui.press("win")

#digitar o nome do programa
pyautogui.write("chrome")



#apertar enter
pyautogui.press("enter")

#escrever link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
#dar enter

pyautogui.press("enter")

time.sleep(2) #esperar tantos segundos em um local específico do código

# Passo 2 - fazer login
pyautogui.click(x=230, y=429)
pyautogui.write("thaisestermedeirosgomes@gmail.com")
pyautogui.press("tab")
pyautogui.write("teste123") 
# Passo 3 - important a vase de dados

# Passo 4 - Cadastrar um produto 

# Passo 5 - Repetir isso até acabar a base de dados