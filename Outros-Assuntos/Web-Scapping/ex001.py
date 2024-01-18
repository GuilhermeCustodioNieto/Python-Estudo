import requests
import bs4
import requests

request = requests.get("https://lista.mercadolivre.com.br/pc-gamer#D[A:pc%20gamer]")

pagina = bs4.BeautifulSoup(request.text, "html.parser")
print(pagina.select("Pc gamer"))