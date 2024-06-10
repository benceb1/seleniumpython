from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime, timedelta
import time
import os


# Opciók beállítása
options = Options()
options.add_experimental_option("detach", True)
prefs = {"download.default_directory" : os.getcwd() + "\downloads"}
options.add_experimental_option("prefs",prefs);

# Szolgáltatás létrehozása
service = Service(ChromeDriverManager().install())

# Böngésző inicializálása
driver = webdriver.Chrome(service=service, options=options)

# Weboldal megnyitása
driver.get("https://akk.hu/statisztika/hozamok-indexek-forgalmi-adatok/zero-kupon-hozamok")

time.sleep(3)

session = True

str_from = '2024-05-01'
str_to = '2024-05-20'
date_from = datetime.strptime(str_from, '%Y-%m-%d').date()
date_to = datetime.strptime(str_to, '%Y-%m-%d').date()

temp_date = date_to - timedelta(days=7)

# többi kör
while session:
    if date_from > temp_date:
        temp_date = date_from
        session = False

    from_input = driver.find_element(By.XPATH, '//*[@id="scroll-main-container"]/div[1]/div/div/div/div[2]/div/div[1]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/input')
    from_input.clear()
    from_input.send_keys(temp_date.strftime("%Y. %m. %d"))
    from_input.send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.XPATH, "//*[@id='zero-kupon-hozamok']/div/div/div/div[2]/div/div/div/span[1]").click()

    temp_date = temp_date - timedelta(days=8)

    time.sleep(2)

time.sleep(5)

# merge
driver.close()