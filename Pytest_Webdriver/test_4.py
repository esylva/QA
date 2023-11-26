from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.implicitly_wait(10)

site = "https://www.mobile.de/ru"
mark = "BMW"
model = "серии 1"
modelDescription = "коняшка"
espect_values = ["5000", "10000", "20000", "30000", "40000", "50000", "60000", "70000", "80000", "90000", "100000", "125000", "150000", "200000"]


"""	1. Перейти на страницу https://www.mobile.de/ru 
	2. Принять куки
	3. Выбрать марку BMW в выпадающем списке, используя Select
	4. Выбрать модель 1 серии в выпадающем списке, используя Select
    5. Проверить, что выпадающем списке 'Пробег до' содержит все необходимые данные, создать словарь со всеми значениями из выпадающего списка и сравнить их, перебрав через цикл. Проверять значение "Не важно" не нужно. 
 	6. Перейти на страницу поиска мотоциклов
    7. Ввести в поле 'Описание модели' текст 'коняшка', для ввода данных написать функцию ввода текста в поле и использовать ее."""

def main():
	"""Выполнение тестов"""
	test_login()
	test_select_mark()
	test_select_model()
	test_check_mileage()
	test_select_moto()
	driver.quit()


def test_login():
	"""Вход на сайт, принятие куки"""
	driver.get(site)
	accept_cookies = driver.find_element(By.XPATH, '//button[contains(text(), "Согласен")]')
	accept_cookies.click()
	
def test_select_mark():
	"""Выбор марки автомобиля"""
	selected_mark = Select(driver.find_element(By.XPATH, '//select[@name="makeModelVariant1.make"]'))
	selected_mark.select_by_visible_text(mark)

def test_select_model():
	"""Выбор модели автомобиля"""
	selected_model = Select(driver.find_element(By.XPATH, '//select[@name="makeModelVariant1.model"]'))
	selected_model.select_by_visible_text(model)

def test_check_mileage():
	"""Создание словаря и проверка необходимых данных по пробегу"""
	selected_milage = Select(driver.find_element(By.XPATH, '//select[@name="maxMileage"]'))
	opt_selected_milage = selected_milage.options
	fact_values = []
	for option in opt_selected_milage:
		fact_values.append(option.get_attribute("value"))
	fact_values.pop(0) # Удаление элемента не подлежащего сравнению
	qa = dict(zip(espect_values, fact_values))
	for key, value in qa.items():
		assert key == value
	
def test_select_moto():
	"""Переход на страницу мотоциклов и поиск по описанию"""
	moto = driver.find_element(By.XPATH, '//*[@class="gicon-searchbike-xxl icon--xxl icon--grey-60"]')
	moto.click()
	model_description = driver.find_element(By.ID, 'modelDescription')
	model_description.send_keys(modelDescription)
	sub_button = driver.find_element(By.XPATH, '// *[@type="submit"]')
	sub_button.click()

if __name__ == "__main__":
	main()