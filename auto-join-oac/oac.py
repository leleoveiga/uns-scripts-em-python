from selenium import webdriver
from time import sleep
import schedule
from selenium.webdriver.chrome.options import Options

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
driver = webdriver.Chrome(chrome_options=opt, executable_path='./chromedriver.exe')
# driver.maximize_window()
driver.get("https://accounts.google.com/signin/v2/identifier?hl=pt-BR&passive=true")

def entrarNaAula():
  driver.get("https://meet.google.com/ywk-jura-uia?pli=1&authuser=1") #oac
  # driver.get("https://meet.google.com/fib-fnnf-gun") #teste
  sleep(3.3)
  # elem = driver.find_element_by_xpath('//span[@class="CwaK9"]//span[@class="RveJvd snByac"]')
  elem = driver.find_element_by_xpath("//*[@id='yDmH0d']/div[3]/div/div[2]/div[3]/div/span/span")
  # elem = driver.find_element_by_class_name("RveJvd.snByac")
  elem = driver.switch_to.active_element
  sleep(0.5)
  elem.click()

  sleep(0.5)
  elem = driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]/span/span")
  # elem = driver.find_element_by_class_name("NPEfkd.RveJvd.snByac")
  # elem = driver.switch_to.active_element
  elem.click()

sleep(8)
entrarNaAula()
# hora = input("fale aí a hora pra entrar na aula. Ex.: 04:20\n")
# schedule.every().day.at(hora).do(entrarNaAula)

# print("agr faz o login. vc vai entrar no classroom às " + hora)

# while True:
#   schedule.run_pending()
#   sleep(1)