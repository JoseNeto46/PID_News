import requests
from bs4 import BeautifulSoup

list_produtos = []

url_base = 'https://www.dafiti.com.br/catalog/?q='

produto_nome = input('Qual produto você deseja? ')

response = requests.get(url_base + produto_nome + '&wtqs=1')

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'data-product-class': 'model-picture'})
print(produtos)
for produto in produtos:
    titulo = produto.find('p', attrs={'class': 'product-box-title'})

    link = produto.find('a', attrs={'class': 'product-box-link is-lazyloaded image product-image-rotate'})
    antes = produto.find('span', attrs={'class': 'product-box-price-to'})
    real = produto.find('span', attrs={'class': 'product-box-price-from'})
    # if antes:
    #     list_produtos.append([titulo.text, real.text, link['href']])
    # else:
    list_produtos.append([titulo.text, real.text, link['href'], antes.text])

    print(titulo.text)
    print(link['href'])
    print('Antes: R$', real.text)
    print('Agora: R$', antes.text)
    print('\n\n')
print(list_produtos)

