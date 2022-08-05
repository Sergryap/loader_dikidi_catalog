from selenium import webdriver
from fake_headers import Headers
import time


url = 'https://dikidi.net/'
# url = 'https://www.whatismybrowser.com/detect/what-is-my-user-agent/'
headers = Headers(os="lin", headers=True).generate()
print(headers)

options = webdriver.FirefoxOptions()

# options.add_argument(f"User-Agent={headers['User-Agent']}")
options.set_preference('general.useragent.override', f"User-Agent={headers['User-Agent']}")

driver = webdriver.Firefox(options=options)

try:
	driver.get(url=url)
	time.sleep(10)
except Exception as ex:
	print(ex)
finally:
	driver.close()
	driver.quit()
