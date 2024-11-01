import time

import requests
from bs4 import BeautifulSoup

# FONTE: https://www.hashtagtreinamentos.com/introducao-ao-beautifulsoup-python?gad_source=1&gclid=Cj0KCQjw1Yy5BhD-ARIsAI0RbXYFSs5ubPMRvl22T_SCeztzhEbHM99BI6YW1PFjUkm8T3lSdVAq7K8aAgF0EALw_wcB

while(True):
    link = "https://www.google.com/search?q=cota%C3%A7%C3%A3o+do+bitcoin&client=ubuntu-sn&hs=uWm&sca_esv=604b5f8f73d33d4a&channel=fs&ei=qEQkZ4yNDrT15OUP0p-QwAw&ved=0ahUKEwiMgYDFkrqJAxW0OrkGHdIPBMgQ4dUDCA8&uact=5&oq=cota%C3%A7%C3%A3o+do+bitcoin&gs_lp=Egxnd3Mtd2l6LXNlcnAiFGNvdGHDp8OjbyBkbyBiaXRjb2luMhAQABiABBixAxiDARhGGIICMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMgUQABiABDIFEAAYgAQyBRAAGIAEMhwQABiABBixAxiDARhGGIICGJcFGIwFGN0E2AECSLgjUOgLWJshcAF4AZABAJgBnQGgAeILqgEEMC4xMrgBA8gBAPgBAZgCDaACzg3CAgoQABiwAxjWBBhHwgINEAAYgAQYsAMYQxiKBcICGRAuGIAEGLADGNEDGEMYxwEYyAMYigXYAQHCAhMQLhiABBiwAxhDGMgDGIoF2AEBwgIQEAAYgAQYsQMYQxiDARiKBcICCxAAGIAEGLEDGIMBwgIIEAAYgAQYsQPCAhUQABiABBixAxhDGIMBGIoFGEYYggLCAiEQABiABBixAxhDGIMBGIoFGEYYggIYlwUYjAUY3QTYAQKYAwCIBgGQBgu6BgQIARgIugYGCAIQARgTkgcEMS4xMqAHiVE&sclient=gws-wiz-serp"

    cabecalho = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0"}

    requisicao = requests.get(link, headers=cabecalho)

    texto = requisicao.text

    site = BeautifulSoup(texto, "html.parser")

    pesquisa = site.find("span", class_="pclqee")

    print(pesquisa.get_text())
    time.sleep(180)
