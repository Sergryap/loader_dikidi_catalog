import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from fake_headers import Headers
import time
import csv
import random
from authorization import password, tel, url_company, url_service
from pprint import pprint


def get_click_loader(driver, url=url_service):
	driver.get(url=url)
	driver.find_element(by="link text", value="Вход / Регистрация").click()
	time.sleep(random.uniform(0.5, 1))
	driver.find_element(by="link text", value="Мобильный номер").click()
	time.sleep(random.uniform(0.5, 1))
	xpath = '//*[@id="number"]'
	tel_input = driver.find_elements(by="xpath", value=xpath)
	for n in tel:
		tel_input[1].send_keys(n)
		time.sleep(.1)
	# tel_input = driver.find_elements(by="name", value="number")
	# tel_input[1].send_keys(tel)
	time.sleep(random.uniform(0.5, 1))
	password_input = driver.find_element(by="name", value="password")
	for n in password:
		password_input.send_keys(n)
		time.sleep(.1)
	time.sleep(random.uniform(0.5, 1))
	password_input.send_keys(Keys.ENTER)
	time.sleep(random.uniform(0.5, 1))
	driver.get(url=url_company)
	time.sleep(random.uniform(0.5, 1))
	xpath = "/html/body/div[1]/div[2]/div[2]/div[2]/form/div[1]/div[2]/div/button"
	driver.find_element(by="xpath", value=xpath).click()
	time.sleep(random.uniform(0.5, 1))
	xpath = "/html/body/div[1]/div[2]/div[2]/div[2]/form/div[1]/div[2]/div/ul/li[1]/a"
	driver.find_element(by="xpath", value=xpath).click()
	time.sleep(10)


def get_driver():
	headers = Headers(os="win", headers=True).generate()
	options = webdriver.ChromeOptions()
	prefs = {"download.default_directory": f"{os.getcwd()}"}
	options.add_experimental_option("prefs", prefs)
	options.add_argument(f"User-Agent={headers['User-Agent']}")
	return webdriver.Chrome(options=options)


def load_data():
	driver = get_driver()
	try:
		get_click_loader(driver=driver)
	except Exception as ex:
		print(ex)
	finally:
		driver.close()
		driver.quit()


def get_data_client():
	with open("clients_2022.08.05.csv", "r", newline='', encoding='utf-8') as csvfile:
		clients = csv.reader(csvfile, delimiter=';')
		return [
			{
				'name': client[0],
				'tel': client[1],
				'amount_vizit': client[9],
				'last_visit': client[10],
				'black_list': client[13]
			} for client in clients][1:]


if __name__ == '__main__':
	# load_data()
	pprint(get_data_client())
