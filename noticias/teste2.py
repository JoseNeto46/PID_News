import requests
from bs4 import BeautifulSoup

list_produtos = []

url_base = 'https://www.amazon.com.br/s?k='

produto_nome = input('Qual produto você deseja? ')

response = requests.get(url_base + produto_nome + '&__mk_pt_BR=ÅMÅŽÕÑ&ref=nb_sb_noss')

site = BeautifulSoup(response.text, 'html.parser')

produtos = site.findAll('div', attrs={'class': 's-main-slot s-result-list s-search-results sg-row'})

for produto in produtos:
    titulo = produto.find('span', attrs={'class': 'a-size-base-plus a-color-base a-text-normal'})

    link = produto.find('a', attrs={'class': 'a-link-normal a-text-normal'})

    real = produto.find('span', attrs={'class': 'a-offscreen'})
    list_produtos.append([titulo.text, link['href'], real.text])

    print(titulo.text)
    print(link['href'])
    print('R$', real.text)
    print('\n\n')
print(list_produtos)

