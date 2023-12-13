from selenium import webdriver
from datetime import date, datetime
import time

driver = webdriver.Chrome()

driver.get("https://app.pipefy.com/")
data = date.today()
# converter para o novo formato
data = data.strftime('%d/%m/%Y')

time.sleep(3)
driver.find_element("xpath",
    '/html/body/div/div/div/div/div/form/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div/div[3]/div[1]/div/input').send_keys("caue.foyth@hyperlocal.com.br")

driver.find_element("xpath",
    '/html/body/div/div/div/div/div/form/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div/div[3]/div[2]/div[1]/div/input').send_keys("@Cauemfoyth1")

driver.find_element("xpath", '/html/body/div/div/div/div/div/form/div/div/div/button').click()

time.sleep(5)
driver.get("https://app.pipefy.com/pipes/301818652/reports_v2/new")

time.sleep(3)
driver.find_element("xpath", '/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/aside/div/div/div/div/button').click()
driver.find_element("xpath", '/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/aside/div/div/div/div[2]/div/div/div/div/ul/dl[1]/dd/dl/dd[2]/button').click()
driver.find_element("xpath", '/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/aside/div/div/div/div[2]/div/div/div/div/div/div/div[1]/div/label').click()
driver.find_element("xpath", '/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/aside/div/div/div/div[2]/div/div/div/div/div/div/div[1]/label/input').send_keys(f"{data}")
driver.find_element("xpath", '/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/aside/div/div/div/div[2]/div/div/div/div/footer/button[2]').click()
driver.find_element("xpath", '/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/aside/footer/button').click()
driver.find_element("xpath", '/html/body/div[10]/div/div[2]/footer/button[1]').click()
driver.find_element("xpath", '/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div/div/div/div/button').click()
driver.find_element("xpath", '/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/ul/li[1]/div[4]/label').click()
driver.find_element("xpath", '/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/ul/li[1]/div[7]/label').click()
driver.find_element("xpath", '/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/ul/li[1]/div[10]/label').click()
driver.find_element("xpath", '/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/ul/li[2]/div[7]/label').click()
driver.find_element("xpath", '/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/ul/li[2]/div[10]/label').click()
driver.find_element("xpath", '/html/body/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[2]/div/div/div/div[2]/div/div/div/div/ul/li[2]/div[11]/label').click()
time.sleep(10)