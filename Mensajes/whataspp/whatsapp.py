import pyautogui, webbrowser
from time import sleep


webbrowser.open('https://web.whatsapp.com/send?phone=9381430129')

sleep(10)

for i in range(3):
    pyautogui.typewrite('hola')
    pyautogui.press('enter')