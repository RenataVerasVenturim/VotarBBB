from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import pyautogui


# Inicialização do driver do Selenium (no exemplo, o ChromeDriver)
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

# Acessar a URL fornecida
navegador.get("https://gshow.globo.com/realities/bbb/bbb-24/voto-da-torcida/votacao/voto-da-torcida-quem-voce-quer-eliminar-do-bbb-24-cDpydBRSJ3.ghtml")

# clicar no DAVI
search_button = navegador.find_element(By.XPATH, '//*[@id="roulette-root"]/div/main/div[1]/div/ul/li[2]/button/div')
search_button.click()

time.sleep(7)

# clicar em continuar com Facebook
search_button2 = navegador.find_element(By.XPATH, '//*[@id="root"]/div[1]/main/div/div/div/div/div[1]/div/button[2]/div')
search_button2.click()

# preencher e-mail e senha
search_button3 = navegador.find_element(By.XPATH, '//*[@id="email"]')
search_button3.send_keys('renata_venturim@hotmail.com')
search_button3 = navegador.find_element(By.XPATH, '//*[@id="pass"]')
search_button3.send_keys('Xena123')

# clicar em entrar
search_entrar = navegador.find_element(By.XPATH, '//*[@id="loginbutton"]')
search_entrar.click()

time.sleep(15)

# Aguardar até que o carregamento da página seja concluído
wait = WebDriverWait(navegador, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

# Encontrar a posição da imagem no captcha na tela
x, y = pyautogui.locateCenterOnScreen('sou_humano.jpg', confidence=0.8)

# Se a imagem for encontrada na tela
if x is not None and y is not None:
    # Clicar na posição encontrada
    pyautogui.click(x, y)
else:
    print('Imagem do captcha não encontrada na tela.')

while True:
    time.sleep(10) 