from tkinter import Tk
import pyautogui
import time

root = Tk()
root.withdraw()

coords = []

with open('escolas.txt') as f:
  escolas = f.readlines()
  for escola in escolas:
    spl = escola.strip().split(';')
    tipo = spl[0]
    nome = spl[1]
    logr = spl[2]
    cep = spl[3]
    query = f'{tipo} {nome} {logr} Campo Grande RJ {cep}'

    pyautogui.moveTo(100, 116)
    pyautogui.click()
    pyautogui.hotkey('ctrl','a')
    pyautogui.press('delete')
    pyautogui.write(query)
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.moveTo(683, 557)
    pyautogui.rightClick()
    pyautogui.moveTo(701, 579)
    pyautogui.click()
    lat, long = root.clipboard_get().split(', ')
    coords.append( (float(lat), float(long), tipo, nome) )
    with open('coordenadas.txt','a') as f2:
        f2.write(f'{lat};{long};{tipo};{nome}')