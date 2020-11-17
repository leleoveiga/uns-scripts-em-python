from pyautogui import press, typewrite, hotkey
import clipboard
from time import sleep

text = clipboard.paste()  # text will have the content of clipboard
sleep(1)
typewrite(text)