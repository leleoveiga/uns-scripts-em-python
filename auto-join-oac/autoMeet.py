from selenium import webdriver
from time import sleep
import schedule
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pyautogui

# leonardo.porfirio@ccc.ufcg.edu.br

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2, 
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.geolocation": 2, 
    "profile.default_content_setting_values.notifications": 2
  })
opt.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=opt, executable_path='./chromedriver.exe')
# driver.maximize_window()
driver.get("https://accounts.google.com/signin/v2/identifier?hl=pt-BR&passive=true")

def gravar():
    pyautogui.keyDown('ctrl')
    pyautogui.keyDown('shift')
    pyautogui.keyDown(']')
    sleep(0.5)
    pyautogui.keyUp('ctrl')
    pyautogui.keyUp('shift')
    pyautogui.keyUp(']')

def clickBotaoPedirPraEntrar():
    elem = driver.find_element(By.XPATH, "//*[@id='yDmH0d']/c-wiz/div/div/div[9]/div[3]/div/div/div[3]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span")
  # elem = driver.switch_to.active_element
    elem.click()

def clickBotaoMic():
    elem = driver.find_element(By.XPATH, "//*[@id='yDmH0d']/div[3]/div/div[2]/div[3]/div/span/span")

    elem = driver.switch_to.active_element
    sleep(0.5)
    elem.click()

meetLink = "https://meet.google.com/mod-mtig-ikn"

def entrarNaAula():
  driver.get(meetLink) #poe o link do meet q tu quer entrar
  sleep(3.3)
  clickBotaoMic()

  sleep(0.5)
  clickBotaoPedirPraEntrar()
  gravar()

# sleep(8)
# entrarNaAula()

hora = input("fale aí a hora pra entrar na aula. Ex.: 04:20\n")
schedule.every().day.at(hora).do(entrarNaAula)

print("agr faz o login. vc vai entrar no classroom às " + hora)

while True:
  schedule.run_pending()
  sleep(1)