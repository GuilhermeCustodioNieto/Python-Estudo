import oauth2
import json
import urllib.parse

"""
Problema: Manipular a api do twitter a fins de estudo

Soluç˜ao: Fazer a autenticaç˜ao do usu´ario via oauth2, postertiomente fazemos m´etodos get para realizar queryes em tweets e m´etodos posts para realizar tweets novos.

Observaç˜oes:
    1: O token n˜ao ´e meu, e sim do professor, infelizmente meu twitter n˜ao est´a funcionando direito e n˜ao consigo configurar minhas chaves de API
    2: A vers˜ao desse c´odigo ´e a 1.1, mas o twitter t´a na 2.0, ent˜ao o c´odigo n˜ao funcionar´a totalmente direito hoje em dia, sendo necess´ario alguns ajustes.
"""

consumer_key = 'WRXnyJds71yDayQaXFxPpI2jv'
consumer_secret = 'AjpaogRVFUyuZTfvaNgwj08J0pD3n6f1k08BjUUlapnUFca2w4'

token_key = '799122088594460672-vzJloX2qozKzEuJhNuyB1oew8rJSEzF'
token_secret = 'COd1bb65SodeBgD7zPTseuZ9lUBpkeeapROr0MXFprlqz'

consumer = oauth2.Consumer(consumer_key, consumer_secret)
token = oauth2.Token(token_key, token_secret)
cliente = oauth2.Client(consumer, token)

def get_tweets(query_text):
    """
    Aqui, vamos pegar os tweets mais recentes baseado em uma query
    pegamos o texto que queremos pesquisar, fazemos a pesquisa com um get e posteriormente imprmimos os resultados encontrados
    """
    
    
    query_codificada = urllib.parse.quote(query_text, safe='')
    requisicao = cliente.request('https://api.twitter.com/1.1/search/tweets.json?q=' + query_codificada + '&lang=pt')

    decodificar = requisicao[1].decode()

    objeto = json.loads(decodificar)
    twittes = objeto['statuses']

for twit in twittes:
    print(twit['user']['screen_name'])
    print(twit['text'])
    print()
    

def new_tweet(post_text):
    """
    Aqui, vamos fazer novs posts no twitter
    Pegamos o texto que vai ser postado, vamos decotificar ele e posteriomente realizar um m´etodo post na Api do twitter e pronto!
    """
    
    query_codificada = urllib.parse.quote(post_text, safe='')
    requisicao = cliente.request('https://api.twitter.com/1.1/statuses/update.json?status=' + query_codificada, method='POST')

    decodificar = requisicao[1].decode()

    objeto = json.loads(decodificar)
    
    print(objeto)