from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import pandas as pd


def index(request):
    return render(request, 'index.html')


def noticias_g1(link):
    lista_noticias = []

    response = requests.get(link)

    content = response.content

    site = BeautifulSoup(content, 'html.parser')

    noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

    for noticia in noticias:

        titulo = noticia.find('a', attrs={'class': 'feed-post-link'})
        subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})

        if subtitulo:
            lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
        else:
            lista_noticias.append([titulo.text, '', titulo['href']])

    return lista_noticias


def exibe_noticia_g1(request):
    return render(request, 'noticias_g1.html', {'conteudo': noticias_g1('https://g1.globo.com/')})


def noticias_bbc(link):
    lista_noticias = []
    response = requests.get(link)

    content = response.content

    site = BeautifulSoup(content, 'html.parser')

    noticias = site.findAll('ul', attrs={'class': 'e57qer20 bbc-10m7ymo eom0ln50'})

    for noticia in noticias:

        # titulo
        titulo = noticia.find('a', attrs={'class': 'bbc-1fxtbkn evnt13t0'})
        titulo['href'] = 'https://www.bbc.com' + titulo['href']
        # subtitulo
        subtitulo = noticia.find('p', attrs={'class': 'bbc-166eyoy e1tfxkuo1'})

        if subtitulo:
            lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
        else:
            lista_noticias.append([titulo.text, '', titulo['href']])

    return lista_noticias


def exibe_noticia_bbc(request):
    return render(request, 'noticias_bbc.html', {'conteudo': noticias_bbc('https://www.bbc.com/portuguese')})


# def ofertas_ml(link):
# 
# 
#     lista_produtos = []
# 
#     url_base = link
# 
#     produto_nome = input('Qual produto você deseja? ')
# 
#     response = requests.get(url_base + produto_nome)
# 
#     site = BeautifulSoup(response.text, 'html.parser')
# 
#     produtos = site.findAll('div', attrs={
#         'class': 'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default'})
# 
#     for produto in produtos:
#         titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})
# 
#         link = produto.find('a', attrs={'class': 'ui-search-link'})
# 
#         real = produto.find('span', attrs={'class': 'price-tag-fraction'})
#         lista_produtos.append([titulo.text, real.text, link['href']])
# 
#     return lista_produtos


def exibe_ofertas_ml(request):
    busca = None
    lista_produtos = []
    url_base = ''
    if request.POST.get('busca'):
        url_base = 'https://lista.mercadolivre.com.br/'
        busca = request.POST.get('busca')
        response = requests.get(url_base + busca)
        site = BeautifulSoup(response.text, 'html.parser')
    
        produtos = site.findAll('div', attrs={
            'class': 'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default'})
        for produto in produtos:

            titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})
    
            link = produto.find('a', attrs={'class': 'ui-search-link'})
    
            real = produto.find('span', attrs={'class': 'price-tag-fraction'})
            lista_produtos.append([titulo.text, real.text, link['href']])
    return render(request, 'ofertas.html', {'produtos': lista_produtos, 'busca': busca})
