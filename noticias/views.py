from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import pandas as pd


def noticias_g1():
    lista_noticias = []

    response = requests.get('https://g1.globo.com/')

    content = response.content

    site = BeautifulSoup(content, 'html.parser')

    noticias = site.findAll('div', attrs={'class':'feed-post-body'})

    for noticia in noticias:

        titulo = noticia.find('a', attrs={'class': 'feed-post-link'})
        print('Titulo da noticia : \n', (titulo.text))
        print(titulo['href'])  # Consigo pegar o link da noticia

        subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})
        print('Subtitulo :')
        if (subtitulo):
            print(subtitulo.text)
            lista_noticias.append([titulo.text, subtitulo.text, titulo['href']])
        else:
            lista_noticias.append([titulo.text, '', titulo['href']])

    news = pd.DataFrame(lista_noticias, columns=['Título:', 'Subtítulo:', 'Link:'])

    print(news)


def noticias_r7():
