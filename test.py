from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# Opciók beállítása
options = Options()
options.add_experimental_option("detach", True)
prefs = {'download.default_directory': 'downloads'}
options.add_experimental_option('prefs', prefs)

# Szolgáltatás létrehozása
service = Service(ChromeDriverManager().install())

# Böngésző inicializálása
driver = webdriver.Chrome(service=service, options=options)

# Weboldal megnyitása
driver.get("https://akk.hu/statisztika/hozamok-indexek-forgalmi-adatok/zero-kupon-hozamok")

time.sleep(3)
input_text_fname = driver.find_element(By.CSS_SELECTOR, 'div.v-slot-scroll-main-container div:nth-of-type(1) > input')
input_text_fname.clear()
input_text_fname.send_keys("2024. 06. 01")

# driver.close()