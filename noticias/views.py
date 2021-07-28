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


def ofertas(link):
    lista_produtos = []
    response = requests.get(link)

    content = response.content

    site = BeautifulSoup(content, 'html.parser')

    produtos = site.findAll('div', attrs={'class': 'a-row Grid-module__gridSection_1SEJTeTsU88s6aVeuuekAp'})

    for produto in produtos:

        nome = produto.find('div', attrs={'class': 'DealCard-module__truncate_3E_98PYsAQzbYk0BLscdkC'})
        print(nome.text)

        preco = produto.find('span', attrs={'class': 'a-price-whole'})
        print(preco.text)

        lista_produtos.append([nome.text, preco.text])
        print(lista_produtos)

    return lista_produtos


def exibe_ofertas(request):
    return render(request, 'ofertas.html', {'conteudo': ofertas('https://www.amazon.com.br/gp/goldbox/')})
