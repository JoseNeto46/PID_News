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


def noticias_r7(link):
    lista_noticias = []
    response = requests.get(link)

    content = response.content

    site = BeautifulSoup(content, 'html.parser')

    noticias = site.findAll('div', attrs={'class': 'widget-8x1-e'})

    for noticia in noticias:

        # titulo
        titulo = noticia.find('a', attrs={'class': 'r7-flex-hat__description'})
        print(titulo['href'])

        # subtitulo
        subtitulo = noticia.find('h3', attrs={'class': 'r7-flex-title-h5'})

        if subtitulo:
            print(subtitulo.text)
            lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
        else:
            lista_noticias.append([titulo.text, '', titulo['href']])

    news = pd.DataFrame(lista_noticias, columns=['Titulo', 'Subtitulo', 'Link'])

    return lista_noticias


def exibe_noticia_r7(request):
    return render(request, 'noticias_r7.html', {'conteudo': noticias_r7('https://www.r7.com/')})
