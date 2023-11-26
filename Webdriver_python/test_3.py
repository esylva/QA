from selenium import webdriver
from selenium.webdriver.common.by import By

"""Функции тестирования выполнены в соответствии с предоставленной сигнатурой"""

def main():
	"""Выполнение тестов"""
	test_check_sensor_ram_v40()
	test_check_sensor_ram_v30()
	test_check_sensor_ram_v40_rus()


def test_check_sensor_ram_v40():

	driver = webdriver.Chrome()
	driver.implicitly_wait(10)

	"""Открыть https://support.kaspersky.com/help/"""
	driver.get("https://support.kaspersky.com/help/")

	"""Найти на странице Industrial CyberSecurity for Networks"""
	element1 = driver.find_element(By.XPATH, 
			'//span[text() = "Industrial CyberSecurity for Networks"]//../..//span[@class="product__version js_dropdown_btn"]'
		)
	element1.click()
	""" Открыть версию 4.0"""
	element2 = driver.find_element(By.XPATH, 
			'//span[text() = "Industrial CyberSecurity for Networks"]/../..//a[text()="4.0"]'					
			)
	element2.click()
	"""В справке открыть \"About Kaspersky Industrial CyberSecurity for Networks\" 
		Открыть \"Hardware and software requirements\""""
	element3 = driver.find_element(By.XPATH,
			'//li/a[contains(text(), "Hardware and software requirements")]'
			)
	element3.click()
	"""Найти текст \"RAM: 8 GB, and an additional 2 GB for each monitoring point on this computer\""""
	element4 = driver.find_element(By.XPATH,
			'//li[contains(text(), "RAM: 8 GB, and an additional 2 GB for each monitoring point on this computer")]'
			)
	"""Assert текст соответствует тексту \"RAM: 8 GB, and an additional 2 GB for each monitoring point on this computer\""""
	assert(element4.text == "RAM: 8 GB, and an additional 2 GB for each monitoring point on this computer")

	driver.quit()


def test_check_sensor_ram_v30():
	
	driver = webdriver.Chrome()
	driver.implicitly_wait(10)
	"""Открыть https://support.kaspersky.com/help/"""
	driver.get("https://support.kaspersky.com/help/")

	"""Найти на странице Industrial CyberSecurity for Networks"""
	element1 = driver.find_element(By.XPATH, 
			'//span[text() = "Industrial CyberSecurity for Networks"]//../..//span[@class="product__version js_dropdown_btn"]'
		    )
	element1.click()
	"""Открыть версию 3.0"""
	element2 = driver.find_element(By.XPATH, 
			'//span[text() = "Industrial CyberSecurity for Networks"]/../..//a[text()="3.0"]'					
			)
	element2.click()
	"""В справке открыть \"About Kaspersky Industrial CyberSecurity for Networks\"
    	Открыть Hardware and software requirements"""
	element3 = driver.find_element(By.XPATH,
			'//li/a[contains(text(), "Hardware and software requirements")]'
			)
	element3.click()
	"""Найти текст \"RAM: 4 GB, and an additional 2 GB for each monitoring point on this computer.\""""
	element4 = driver.find_element(By.XPATH,
			'//li[contains(text(), "RAM: 4 GB, and an additional 2 GB for each monitoring point on this computer.")]'
			)
	"""Assert текст соответствует тексту \"RAM: 4 GB, and an additional 2 GB for each monitoring point on this computer.\""""
	assert(element4.text == "RAM: 4 GB, and an additional 2 GB for each monitoring point on this computer.")
	driver.quit()

def test_check_sensor_ram_v40_rus():

	driver = webdriver.Chrome()
	driver.implicitly_wait(10)

	"""Открыть https://support.kaspersky.com/help/ """
	driver.get("https://support.kaspersky.com/help/")

	"""Найти на странице Industrial CyberSecurity for Networks"""
	element1 = driver.find_element(By.XPATH, 
			'//span[text() = "Industrial CyberSecurity for Networks"]//../..//span[@class="product__version js_dropdown_btn"]'
		)
	element1.click()

	"""Открыть версию 4.0"""
	element2 = driver.find_element(By.XPATH, 
			'//span[text() = "Industrial CyberSecurity for Networks"]/../..//a[text()="4.0"]'					
			)
	element2.click()

	"""В справке открыть "О Kaspersky Industrial CyberSecurity for Networks"""
	element3 = driver.find_element(By.XPATH,
			'//*[@class="dropdown__btn js_dropdown_btn" and contains(text(),"English")]'
			)
	element3.click()

	"""Найти текст \"объем оперативной памяти: 8 ГБ и по 2 ГБ для каждой точки мониторинга на этом компьютере;\""""
	element4 = driver.find_element(By.XPATH,
			'//*[@class="dropdown__btn js_dropdown_btn" and contains(text(),"English")]/..//*[contains(text(),"Русский")]'
			)
	element4.click()

	"""Открыть \"Аппаратные и программные требования\""""
	element5 = driver.find_element(By.XPATH,
			'//li/a[contains(text(), "Аппаратные и программные требования")]'
			)
	element5.click()

	"""Найти текст \"объем оперативной памяти: 8 ГБ и по 2 ГБ для каждой точки мониторинга на этом компьютере;\""""
	element6 = driver.find_element(By.XPATH,
			'//li[contains(text(), "объем оперативной памяти: 8 ГБ и по 2 ГБ для каждой точки мониторинга на этом компьютере;")]'
			)
	
	"""Assert текст соответствует тексту \"объем оперативной памяти: 8 ГБ и по 2 ГБ для каждой точки мониторинга на этом компьютере;\""""
	assert(element6.text == "объем оперативной памяти: 8 ГБ и по 2 ГБ для каждой точки мониторинга на этом компьютере;")
	
	driver.quit()

if __name__ == "__main__":
	main()