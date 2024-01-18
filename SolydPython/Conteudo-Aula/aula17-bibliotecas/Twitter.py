import oauth2
import urllib.parse
import json

class Twitter:
    """
    Essa ´e uma biblioteca que pode fazer posts e pegar tweets do Twitter, ela usa a APi do twitter
    
    Uma observaç˜ao ´e que a api do twitter ´e da vers˜˜ao 2, ent˜ao n˜ao ´e a mais atual e talvez o programa n˜ao funcione da forma certa.
    """
    def __init__(self, consumer_key, consumer_secret, token_key, token_secret):
        self.conexao(consumer_key, consumer_secret, token_key, token_secret)

    def conexao(self, consumer_key, consumer_secret, token_key, token_secret):
        """
        Essa funç˜ao cria uma conex˜ao entre o nosso programa e a API do twitter
        No final dela, o que importa ´e a variavel cliente, que guarda o user da conta
        """
        
        self.consumer = oauth2.Consumer(consumer_key, consumer_secret)
        self.token = oauth2.Token(token_key, token_secret)
        self.cliente = oauth2.Client(self.consumer, self.token)

    def tweet(self, novo_tweet):
        """
        Essa funç˜ao faz um tweet novo, ela recebe o texto do ovo tweet e no final retorna as informaç˜oes sobre o tweet feito.
        """
        query_codificada = urllib.parse.quote(novo_tweet, safe='')
        requisicao = self.cliente.request('https://api.twitter.com/1.1/statuses/update.json?status=' + query_codificada,
                                     method='POST')
        decodificar = requisicao[1].decode()
        objeto = json.loads(decodificar)
        return objeto

    def search(self, query, lang):
        """
        Essa funç˜ao faz a pesquisa de tweets recentes com base em um texto para query
        
        ela recebe o texto para a query e a linguagem que vai ser feita a busca, e por fim retorna um dicion´ario de tweets encontrados.
        """
        
        query_codificada = urllib.parse.quote(query, safe='')
        requisicao = self.cliente.request(
            'https://api.twitter.com/1.1/search/tweets.json?q=' + query_codificada + '&lang=' + lang)
        decodificar = requisicao[1].decode()
        objeto = json.loads(decodificar)
        twittes = objeto['statuses']
        return twittes
