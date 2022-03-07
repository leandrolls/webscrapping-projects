from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("https://www.coronatracker.com/pt-br/")
sleep(3)

print(browser.title)
item = 1
try:
    main = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                                            "#__layout > div > main > div > div.w-full.md\:w-2\/3.px-2 > div.bg-white.rounded.border.border-gray-400.p-4")))
    print("Achei a sessão")
    for i in range(3):
        titulo = browser.find_element_by_xpath(f'//*[@id="__layout"]/div/main/div/div[1]/div[1]/div[1]/div[2]/div[{item}]/div[2]/span')
        numero = browser.find_element_by_xpath(f'// *[ @ id = "__layout"] / div / main / div / div[1] / div[1] / div[1] / div[2] / div[{item}] / div[1]')

        print(titulo.text)
        print(numero.text)
        item = item + 1

except:
    print("Não deu certo")
    browser.quit()