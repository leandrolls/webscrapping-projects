from selenium import webdriver
from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from funcions import*

chrome_options = Options()
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_options.add_argument('--lang=pr-BR')
chrome_options.add_argument('--disable-notifications')
driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')


driver.get("https://www.americanas.com.br/lojista/tecla-certa-31167676000106?ordenacao=higherPrice")

print(driver.title)
sleep(3)
item = 1
nomes = []
precos = []

main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content-middle"]/div[4]/div/div/div/div[1]')))
print("Achei a grade")
for x in range(5):
    item = 1
    sleep(5)
    for i in range(24):
        try:
            nome = driver.find_element_by_xpath(f'//*[@id="content-middle"]/div[4]/div/div/div/div[1]/div[{item}]/div/div[2]/a/section/div[2]/div[1]/h2')
            preco = driver.find_element_by_xpath(f'// *[@id="content-middle"]/div[4]/div/div/div/div[1]/div[{item}]/div/div[2]/a/section/div[2]/div[2]/div[3]/span')

            nomes.append(nome.text)
            precos.append(preco.text)

            print(nome.text,": ", preco.text)
            item = item + 1
            sleep(1)

        except NoSuchElementException:

            print(f'\u001b[33m{"Produto recém sem estoque"}\u001b[0m')

    try:
        botao_proximo = driver.find_element_by_xpath('//*[@id="content-middle"]/div[4]/div/div/div/div[2]/div/ul/li[6]/a')
        botao_proximo.click()
        print("*********PROXIMA PAGINA************")


    except NoSuchElementException:

        print(f'\u001b[33m{"Não há mais paginas!"}\u001b[0m')
        print(f'\u001b[32m{"Escaneamento Concluido"}\u001b[0m')

        criarPlanilha(nomes, precos)
        enviar_email()
        sleep(1)
        driver.quit()





