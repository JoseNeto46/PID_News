import requests
from bs4 import BeautifulSoup

list_produtos = []

url_base = 'https://lista.mercadolivre.com.br/'

produto_nome = input('Qual produto você deseja? ')

response = requests.get(url_base + produto_nome)

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class': 'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default'})

for produto in produtos:
    titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})

    link = produto.find('a', attrs={'class': 'ui-search-link'})

    real = produto.find('span', attrs={'class': 'price-tag-fraction'})
    list_produtos.append([titulo.text, link['href'], real.text])

    print(titulo.text)
    print(link['href'])
    print('R$', real.text)
    print('\n\n')
print(list_produtos)
print(response.text)