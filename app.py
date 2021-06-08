from selenium import webdriver
from time import sleep
import requests


class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir-Perfil')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )
        self.url_pdf = r'http://www.ans.gov.br/images/stories/Plano_de_saude_e_Operadoras/tiss/Padrao_tiss/tiss3/Padr%C3%A3o_TISS_Componente_Organizacional_202103.pdf'

    def click_link(self):
        try:
            btn_link = self.chrome.find_element_by_xpath('/html/body/div[9]/div/div[2]/div[2]/div[2]/a')
            btn_link.click()
            print('Acessando padrão mais recente de TISS...')
        except Exception as e:
            print('Erro ao acessar o site', e)

    def click_pdf(self):
        try:
            btn_link = self.chrome.find_element_by_xpath('/html/body/div[9]/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[3]/a')
            btn_link.click()
            print('clicando no pdf...')
        except Exception as e:
            print('Erro ao clicar em Compente Organizacional.pdf', e)

    def download_pdf(self):
        try:
            r = requests.get(self.url_pdf)
            with open('Compente Organizacional.pdf', 'wb') as code:
                code.write(r.content)
        except Exception as e:
            print('Erro ao realizar o download do pdf', e)

    def access(self, website):
        self.chrome.get(website)
        print('Acessando Site...')

    def exit_nav(self):
        self.chrome.quit()


if __name__ == '__main__':
    chrome = ChromeAuto()
    chrome.access('http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar')
    sleep(5)
    chrome.click_link()
    sleep(5)
    chrome.click_pdf()
    sleep(5)
    chrome.download_pdf()
    chrome.exit_nav()
