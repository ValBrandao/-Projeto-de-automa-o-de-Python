import pyautogui
import time

time.sleep(10)
print(pyautogui.position()) # Pega a posição do mouse


#PASSO 4: casdastrar 1 produto
pyautogui.click(x=414, y=263)

codigo = "MOLO000251"
pyautogui.write(codigo)

pyautogui.press("tab")
marca = "Logitech"
pyautogui.write(marca)

pyautogui.press("tab")
tipo = "Mouse"
pyautogui.write(tipo)

pyautogui.press("tab")
categoria = "1"
pyautogui.write(categoria)

pyautogui.press("tab")
preco_unitario = "25.95"
pyautogui.write(preco_unitario)

pyautogui.press("tab") # ir para o proximo  campo 
custo = "6.50"
pyautogui.write(custo)

pyautogui.press("tab")
obs = ""
pyautogui.write(obs)

pyautogui.press("tab")
pyautogui.press("enter")

pyautogui.scroll(10000) # scroll para cima (obs para baixo é -10000)

#PASSO 5: casdastrar todos os produtos da base de dados


