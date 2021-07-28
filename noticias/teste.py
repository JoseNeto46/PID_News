import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_produtos = []
response = requests.get('https://www.amazon.com.br/gp/goldbox/')
print('1')
content = response.content
print('2')
site = BeautifulSoup(content, 'html.parser')

produtos = site.findAll('div', attrs={'class': 'Grid-module__grid_1-xkdMK87Hfx0wjqVxAGcI'})
print('3')
for produto in produtos:
    nome = produto.find('div', attrs={'class': 'DealCard-module__truncate_3E_98PYsAQzbYk0BLscdkC'})
    print('teste2')
    print(nome.text)

    preco = produto.find('span', attrs={'class': 'a-price-whole'})
    print(preco.text)

    lista_produtos.append([nome.text, preco.text])
print(lista_produtos)
