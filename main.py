# Passo a passo do projeto
# Passo 1: Entrar no sistema da empresa 
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
# str > string (texto)
pyautogui.PAUSE = 0.4
# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(2)
pyautogui.click(x=603, y=366)

#digitar o  site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
#esperar a página carregar
time.sleep(3)

#PASSO 2: Fazer login no sistema
#clicar no campo de email   
pyautogui.click(x=390, y=375)
#digitar o email    
pyautogui.write("tangirodemonslayer@gmail.com")
#preencher senha
pyautogui.press("tab")
pyautogui.write("Tangiro@demonslayer")
time.sleep(5)
#botao de login
pyautogui.press("tab")
pyautogui.press("enter")
#esperar a página carregar
time.sleep(5)
#PASSO 3: importar  a base de dados
import pandas
tabela = pandas. read_csv("produtos.csv")
print(tabela)

#PASSO 4: casdastrar 1 produto
for linha in tabela.index: # para cada linha na tabela faça
    pyautogui.click(x=414, y=263)

    codigo = str(tabela.loc[linha, "codigo"]) # loc pega o valor da linha e coluna especifica
    pyautogui.write(codigo)

    pyautogui.press("tab")
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)

    pyautogui.press("tab")
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"]) 
    pyautogui.write(categoria)

    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab") # ir para o proximo  campo 
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")
    obs = str(tabela.loc[linha, "obs"]) 
    
    if obs != "nan":  # se obs for diferente de nan
       pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(10000) # scroll para cima (obs para baixo é -10000)

#PASSO 5: casdastrar todos os produtos da base de dados
# nan -> not a number (não é um número ou valor vazio)



