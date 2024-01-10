#  código simples de uma automação de cadastro de produtos
# simple code of a product registration automation

# passo 1 - entrar no sistema da empresa
# step 1 - enter the company system

import pyautogui
import time
import pandas


pyautogui.PAUSE = 0.5 # pausa de 1 segundo a cada comando \\ pause of 1 second after each command

#explicações de códigos do auto gui // explanations of auto gui codes
#clicar : pyautogui.click(x,y)
#digitar: pyautogui.write('texto')
#pressionar uma tela: pyautogui.press('enter')
#apertar: pyautogui.hotkey

#apertar a tecla do windows // press the windows key
pyautogui.press("win")
#digitar o nome do programa // type the program name
pyautogui.write("chrome")
#apertar enter // press enter
pyautogui.press("enter")
#escrever link do site // write the site link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
#dar enter // press enter
pyautogui.press("enter")
time.sleep(1) #esperar tantos segundos em um local específico do código
                # wait some seconds in a specific location of the code

# Passo 2 - fazer login
pyautogui.click(x=230, y=429) #clica no local do email // click on the email location
pyautogui.write("thaisestermedeirosgomes@gmail.com") #digita o email // type the email
pyautogui.press("tab")#aperta a tecla tab para descer para a próxima linha // press the tab key to go down to the next line
pyautogui.write("teste123") #digita a senha // type the password
pyautogui.press("enter") #aperta enter para fazer o login // press enter to login
time.sleep(1) #espera o site carregar // wait the site fully load

# Passo 3 - importa a base de dados // import the database

tabela = pandas.read_csv("produtos.csv") #associa o csv a uma variável usando a biblioteca pandas // associate the csv to a variable using the pandas library
#print(tabela) #imprime a tabela para verificação // print the table for verification

# Passo 4 - Cadastrar os produtos // register the products

#para cada linha da tabela, ele associa ao indice e preenche os campos 
#// for each line of the table, it associates with the index and fills in the fields
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
