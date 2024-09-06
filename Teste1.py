import keyboard
import pyautogui

text = input("Digite o texto: ")

pyautogui.moveTo(x=1098, y=552, duration=1)
pyautogui.click()
keyboard.write(text)

