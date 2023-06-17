from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_driver = webdriver.Chrome()

chrome_driver.get("https://www.wikipedia.org/")
print(chrome_driver.title)

search_box = chrome_driver.find_element(By.ID, "searchInput")
search_box.send_keys("gonzalez suarez")
search_button = chrome_driver.find_element(By.CSS_SELECTOR, '#search-form > fieldset > button > i')
search_button.click()


elem = chrome_driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
chrome_driver.close()


