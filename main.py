import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from telegram_bot import TelegramBot
from mongodb import MongoDB
chrome_driver = webdriver.Chrome()

bot = TelegramBot()
db = MongoDB()


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
    text = content.text
    text = text[:4000]
    bot.send_tg_message(text)
    db.insert_wikipedia_text(title=t, text=text)
    time.sleep(2)
    chrome_driver.get("https://www.wikipedia.org/")


print("fin")
chrome_driver.close()


