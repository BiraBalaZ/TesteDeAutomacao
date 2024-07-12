# pip install selenium
# pip install webdriver-manager

from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service

servico = Service(GeckoDriverManager().install())
navegador = webdriver.Firefox(service=servico)

page = 'https://pages.hashtagtreinamentos.com/arquivo-python-1jGh7kZSxQLoznA_GgwnWa8f7LEl3kKCZ?origemurl=hashtag_yt_org_planilhapyt_8AMNaVt0z_M'
navegador.get(page)

# Escrevendo E-Mail no formulário
navegador.find_element('xpath', '/html/body/div[2]/div[1]/section/div[2]/div/form/div[1]/div/div/div/input').send_keys('teste@gmail.com')

# Clicando no botão de enviar no formulário
navegador.find_element('xpath', '/html/body/div[2]/div[1]/section/div[2]/div/form/button').click()

# Fechando a aba
navegador.quit()
