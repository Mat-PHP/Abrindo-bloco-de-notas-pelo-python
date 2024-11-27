import pyautogui
import time

# Abrir o bloco de notas
pyautogui.press('winleft')
time.sleep(3)
pyautogui.write('bloco de notas')
time.sleep(3)
pyautogui.press('enter')

# Digitar este é um exemplo de automação
time.sleep(1)
pyautogui.write('Este é um exemplo de automação')