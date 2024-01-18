#MÓDULO 05 DO CURSO FIAP PYTHON

#--------GeoPy--------------

#PROBLEMA 01
from geopy.geocoders import Nominatim

def ler_arquivo(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r") as arq_json:
            dicionario=json.load(arq_json)
    else:
        dicionario = {}
    return dicionario

def gravar_arquivo(dicionario,arquivo):
    with open(arquivo, "w") as arq_json:
        json.dump(dicionario, arq_json)

geolocator = Nominatim(user_agent="wazeyes")
dicionario=ler_arquivo("entrada.json")
lista=dicionario["endereco"]
endereco=lista[0] + "," + lista[1] + " " + lista[2] + " " + lista[3]
location = geolocator.geocode(endereco)
saida={"coordenadas": (location.latitude, location.longitude)}
gravar_arquivo(saida,"saida.json")

#PROBLEMA 02

geolocator = Nominatim(user_agent="wazeyes")

endereco=input("Digite um endereco com número e cidade. "
               "
Exemplo: avenida paulista, 100 São Paulo:
")
resultado = str(geolocator.geocode(endereco)).split(",")

if resultado[0]!='None':
    print("Endereço completo.: ", resultado)
    print("Bairro............: ", resultado[1])
    print("Cidade............: ", resultado[2])
    print("Regiao............: ", resultado[3])
    
#PROBLEMA 03

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="wazeyes")

latitude=float(input("Digite a latitude...: "))
longitude=float(input("Digite a longitude.: "))

resultado = str(geolocator.reverse(f"{latitude}, {longitude}")).split(",")
if resultado[0]!='None':
    print("Endereço completo.: ", resultado)
    print("Dado 1............: ", resultado[0])
    print("Dado 2............: ", resultado[1])
    print("Dado 3............: ", resultado[2])
    
#--------Systema Operacional-Platform--------------

#PROBLEMA 01

import platform

print("Distribuição do Sistema Operacional.: ", platform.platform())
print("Nome do Sistema Operacional.........: ", platform.system())
print("Versão do Sistema Operacional.......: ", platform.release())
print("Arquitetura.........................: ", platform.architecture())
print("Nome do Computador..................: ", platform.node())
print("Tipo de Máquina.....................: ", platform.machine())
print("Processador.........................: ", platform.processor())
print("Versão do Python....................: ", platform.python_version())

#--------Systema Operacional-Getpass--------------

#PROBLEMA 01

import getpass
from datetime import datetime

print("Usuário.......: ", getpass.getuser())
print("Data Completa.: ", datetime.now())
print("Dia...........: ", datetime.now().day)
print("Mês...........: ", datetime.now().month)
print("Ano...........: ", datetime.now().year)
print("Hora..........: ", datetime.now().hour)
print("Minuto........: ", datetime.now().minute)
print("Segundo.......: ", datetime.now().second)

#PROBLEMA 02
import getpass

usuario = input("
Digite o usuário: ").upper()
senha = getpass.getpass("Digite a senha: ")

if usuario == "BITMED" and senha == "FiAp1222":
    print("Usuário logado")
else:
    print("Login Negado")