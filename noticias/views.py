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


def ofertas_ml(busca=None):
    lista_produtos = []

    url_base = 'https://lista.mercadolivre.com.br/'
    response = requests.get(url_base + busca)
    site = BeautifulSoup(response.text, 'html.parser')

    produtos = site.findAll('div', attrs={
        'class': 'andes-card andes-card--flat andes-card--default ui-search-result ui-search-result--core andes-card--padding-default'})
    for produto in produtos:
        titulo = produto.find('h2', attrs={'class': 'ui-search-item__title'})

        link = produto.find('a', attrs={'class': 'ui-search-link'})

        real = produto.find('span', attrs={'class': 'price-tag-fraction'})
        lista_produtos.append([titulo.text, real.text, link['href']])

    return lista_produtos


def ofertas_amazon(busca=None):
    lista_produtos = []

    url_base = 'https://www.amazon.com.br/s?k='
    response = requests.get(url_base + busca + '&__mk_pt_BR=ÅMÅŽÕÑ&ref=nb_sb_noss_2')
    site = BeautifulSoup(response.text, 'html.parser')

    produtos = site.findAll('div', attrs={
        'class': 's-main-slot s-result-list s-search-results sg-row'})
    for produto in produtos:
        titulo = produto.find('span', attrs={'class': 'a-size-base-plus a-color-base a-text-normal'})

        link = produto.find('a', attrs={'class': 'a-link-normal a-text-normal'})

        real = produto.find('span', attrs={'class': 'a-offscreen'})
        link['href'] = 'https://www.amazon.com.br' + link['href']
        lista_produtos.append([titulo.text, real.text, link['href']])

    return lista_produtos


def ofertas_cc(busca=None):
    lista_produtos = []

    url_base = 'https://www.cec.com.br/busca?q='
    response = requests.get(url_base + busca)
    site = BeautifulSoup(response.text, 'html.parser')

    produtos = site.findAll('div', attrs={
        'class': 'itemListElement'})
    for produto in produtos:
        titulo = produto.find('a', attrs={'class': 'name-and-brand'})

        link = produto.find('a', attrs={'class': 'name-and-brand'})

        real = produto.find('span', attrs={'class': 'value-full'})
        link['href'] = 'https://www.cec.com.br' + link['href']
        lista_produtos.append([titulo.text, real.text, link['href']])

    return lista_produtos


def exibe_ofertas(request):
    busca = None
    conteudo = None
    site = ''
    if request.POST.get('sites') == 'mercado_livre':
        if request.POST.get('busca'):
            busca = request.POST.get('busca')
            conteudo = ofertas_ml(busca)
            site = 'Mercado Livre'
    elif request.POST.get('sites') == 'amazon':
        if request.POST.get('busca'):
            busca = request.POST.get('busca')
            conteudo = ofertas_amazon(busca)
            site = 'Amazon'
    elif request.POST.get('sites') == 'cc':
        if request.POST.get('busca'):
            busca = request.POST.get('busca')
            conteudo = ofertas_cc(busca)
            site = 'C&C'

    return render(request, 'ofertas.html', {'produtos': conteudo, 'busca': busca, 'site': site})
