import requests
import json
import time

"""
Problema: consultar filmes e gerar relatórios de forma automatica e simplificada.

Solução: O uso de uma API gratuita que permite as consultas dos filmss através do titulo, posteriormente adicionamos os principais dados do filme em um arquivo

http://www.omdbapi.com/?i=tt3896198&apikey=f7bf428d
"""

def get_movie(movie_name):
  try:
      req = requests.get("http://www.omdbapi.com/?t="+movie_name+"&apikey=f7bf428d&type=movie")
      movie = json.loads(req.text)
      return movie
  except:
      print("Erro de conexão")
      return None


def output_movie_infos(movie):
    movie_infos = "Reports \n"
    movie_infos += "Title: " + movie["Title"] +"\n"
    movie_infos += "Year: " +movie["Year"] + "\n"
    movie_infos += "Genre: " + movie["Genre"]+ "\n"
    movie_infos += "Actors: " + movie["Actors"] + "\n"
    movie_infos += "Plot: " + movie["Plot"] + "\n"
    print("-"*50)
    
    return movie_infos
 
def generate_reports(path_name, movie_infos):
    with open(path_name, "w+") as movies_reports:
        original_txt = movies_reports.read()
        movies_reports.write(movie_infos)
        
        movies_reports.close()
        
while True:
    try:
        print("-"*50)
        movie_name = input("Write the movie name: ")
        
        if movie_name == "EXIT":
            print("Saindo...")
            time.sleep(1)
            print("Fim do programa")
            break
        movie = get_movie(movie_name)
        if movie["Response"] == "False":
            print("Filme não encontrado, tente novamente")
        else:
            movie_infos = output_movie_infos(movie)
            
            print("*"*50)
            print(movie_infos)
            print("*"*50)
            
            if (input("Want to save the movie info in a file? [Y/N] ")).lower() == "y":
                path_name = input("Write the path to save: ")
                generate_reports(path_name, movie_infos)
                print("Finished!")
                
    except Exception as ex:
        print("Critical Error")
        print(ex)
        break