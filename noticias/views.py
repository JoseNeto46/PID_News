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
        print('Titulo da noticia : \n', (titulo.text))
        print(titulo['href'])  # Consigo pegar o link da noticia

        subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})
        print('Subtitulo :')
        if subtitulo:
            print(subtitulo.text)
            lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
        else:
            lista_noticias.append([titulo.text, '', titulo['href']])

    news = pd.DataFrame(lista_noticias, columns=['Título:', 'Subtítulo:', 'Link:'])
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
        print(titulo['href'])
        titulo['href'] = 'https://www.bbc.com' + titulo['href']

        # subtitulo
        subtitulo = noticia.find('p', attrs={'class': 'bbc-166eyoy e1tfxkuo1'})

        if subtitulo:
            print(subtitulo.text)
            lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
        else:
            lista_noticias.append([titulo.text, '', titulo['href']])

    news = pd.DataFrame(lista_noticias, columns=['Titulo', 'Subtitulo', 'Link'])

    return lista_noticias


def exibe_noticia_bbc(request):
    return render(request, 'noticias_bbc.html', {'conteudo': noticias_bbc('https://www.bbc.com/portuguese')})
