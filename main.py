import time

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver = webdriver.Chrome()

# bot = TelegramBot()
# db = Mongo()


chrome_driver.get("https://www.wikipedia.org/")
print(chrome_driver.title)

topics = [
    "Alhambra",
    "Generalife",
    "gonzalez suarez"
]

for t in topics:
    search_box = chrome_driver.find_element(By.ID, "searchInput")
    search_box.send_keys(t)
    search_button = chrome_driver.find_element(By.CSS_SELECTOR, '#search-form > fieldset > button > i')
    search_button.click()

    content = chrome_driver.find_element(By.ID, "mw-content-text")
    print(content.text)

    # enviar por telegram
    # bot.send(content.text, chat_id)
    # db.insert_wikipedia_text({
    #   "topic": content.text
    # }

    time.sleep(2)
    chrome_driver.get("https://www.wikipedia.org/")


print("fin")
chrome_driver.close()


