#  já peço perdão pela organização do codigo


# passo 1 - entrar no sistema da empresa

import pyautogui
import time
 # # https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.PAUSE = 0.5 # pausa de 1 segundo a cada comando
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

time.sleep(1) #esperar tantos segundos em um local específico do código

# Passo 2 - fazer login
pyautogui.click(x=230, y=429) #clica no local do email
pyautogui.write("thaisestermedeirosgomes@gmail.com") #digita o email
pyautogui.press("tab")#aperta a tecla tab para descer para a próxima linha
pyautogui.write("teste123") #digita a senha
pyautogui.press("enter") #aperta enter para fazer o login
time.sleep(1) #espera o site carregar

# Passo 3 - important a vase de dados
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4 - Cadastrar um produto 

for linha in tabela.index:
    pyautogui.click(x=168, y=316)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    #marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    #tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    #categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    #preco
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    #custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    #obs
    obs = str(tabela.loc[linha, "obs"])
    if not pandas.isna(obs):
        pyautogui.write(obs)  

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(50000)

# Passo 5 - Repetir isso até acabar a base de dados