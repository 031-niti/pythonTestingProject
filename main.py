import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


s = Service('D:\\644259031\\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://sc.npru.ac.th/sc_npru/public/")
time.sleep(2)
driver.close()