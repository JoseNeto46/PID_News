import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_produtos = []
response = requests.get('https://www.amazon.com.br/gp/goldbox/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

produtos = site.findAll('div', attrs={'aria-label': 'Grade de ofertas'})
print('teste')
for produto in produtos:
    nome = produto.find('div', attrs={'class': 'DealCard-module__truncate_3E_98PYsAQzbYk0BLscdkC'})
    print('teste2')
    print(nome.text)

    preco = produto.find('span', attrs={'class': 'a-price-whole'})
    print(preco.text)

    lista_produtos.append([nome.text, preco.text])
print(lista_produtos)
