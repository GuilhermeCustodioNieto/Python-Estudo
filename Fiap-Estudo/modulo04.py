#MÓDULO 04 DO CURSO FIAP PYTHON

#--------manipulação de arquivos--------------

#PROBLEMA 01

with open("teste.txt", "r") as arquivo:
  conteudo = arquivo.read()
  
with open("teste.txt", "w") as arquivo:
    arquivo.write("Nunca foi tão fácil criar um arquivo.")

with open("teste.txt", "w") as arquivo:
    arquivo.write("
Continuação do texto.")

#PROBLEMA 02

with open("pagina.html", "w") as pagina:
    pagina.write("<body> <h1> Esta é um teste para página WEB </h1>")
    pagina.write("<br><h2> Abaixo seguem alguns nomes importantes para o projeto:  </h2>")
    pagina.write("<h3>")
    nome=""
    while nome!="SAIR":
        nome = input("Digite um nome ou SAIR: ").upper()
        if nome!="SAIR":
            pagina.write("<br>"+nome)
    pagina.write("</h3></body>")
    
with open("teste.txt", "r") as arquivo:
    conteudo=arquivo.read()
print("Tipo de dado da variável",type(conteudo))
print("
Conteúdo do arquivo:
",conteudo)


#PROBLEMA 03

def chamarMenu():
    escolha = int(input("Digite: "
                      "
<1> para registrar ativo"
                      "
<2> para persistir em arquivo"
                      "
<3> para exibir ativos armazenados: "))
    return escolha

def registrar(dicionario):
    resp="S"
    while resp=="S":
        dicionario[input("Digite o número patrimonial: ")]=[
        input("Digite a data da última atualização: "),
        input("Digite a descrição: "),
        input("Digite o departamento: ")]
        resp=input("Digite <S> para continuar.").upper()

def persistir(dicionario):
    with open("inventario.csv", "a") as inv:
        for chave, valor in dicionario.items():
            inv.write(chave + ";" + valor[0] + ";" + 
					valor[1] + ";" +valor[2]+"
")
    return "Persistido com sucesso"

def exibir():
    with open("inventario.csv", "r") as inv:
        linhas=inv.readlines()
    return linhas
    
inventario={}
opcao=chamarMenu()
while opcao>0 and opcao<4:
    if opcao==1:
        registrar(inventario)
    elif opcao==2:
        persistir(inventario)
    elif opcao==3:
        print(exibir())
    opcao = chamarMenu()
    

#PROBLEMA 04

with open("economic-indicators.csv","r") as boston:
    total_voos=0
    maior=0
    total_passageiros=0
    maior_media_diaria=0
    ano_usuario = input("Qual ano deseja pesquisar? ")
    for linha in boston.readlines()[1:-1]:
        lista=linha.split(",")
        total_voos=total_voos+float(lista[3])
        if float(lista[2])>float(maior):
            maior=lista[2]
            ano=lista[0]
            mes=lista[1]
        if ano_usuario==lista[0]:
            total_passageiros=total_passageiros+float(lista[2])
            if float(lista[5])>float(maior_media_diaria):
                maior_media_diaria=lista[5]
                mes_maior_diaria=lista[1]
    print("O total de voos é: ", total_voos)
    print("O mês/ano de maior movimento no aeroporto foi: ", 
						str(mes),"/",str(ano))
    print("O total de passageiros do ano ", ano_usuario, 
						"foi de ", total_passageiros)
    print("O mês do ano ", ano_usuario, 
	"com maior média para diária de hotel foi ", mes_maior_diaria)
	
#PROBLEMA 05
import json
inventario={}
opcao=int(input("Digite: "
                      "
<1> para registrar ativo"
                      "
<2> para exibir ativos armazenados: "))
while opcao>0 and opcao<3:
    if opcao==1:
        resp = "S"
        while resp == "S":
            inventario[input("Digite o número patrimonial: ")] = [
                input("Digite a data da última atualização: "),
                input("Digite a descrição: "),
                input("Digite o departamento: ")]
            resp = input("Digite <S> para continuar.").upper()
        with open("inventario_json.json", "w") as arq_json:
            json.dump(inventario, arq_json)
        print("JSON gerado!!!!")
    elif opcao==2:
            with open("inventario_json.json", "r") as arq_json:
    		 resultado = json.load(arq_json)
    		 for chave, dado in resultado.items():
                	print("Data.........: ", dado[0])
                	print("Descrição....: ", dado[1])
                	print("Departamento.: ", dado[2])
    opcao = int(input("Digite: "
                      "
<1> para registrar ativo"
                      "
<2> para exibir ativos armazenados: "))

#PROBLEMA 06
import json
import os
def chamarMenu():
    escolha = int(input("Digite: "
                      "
<1> para registrar ativo"
                      "
<2> para exibir ativos armazenados: "))
    return escolha

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

def registrar(dicionario, arquivo):
    resp = "S"
    while resp == "S":
        dicionario[input("Digite o número patrimonial: ")] = [
            input("Digite a data da última atualização: "),
            input("Digite a descrição: "), input("Digite o departamento: ")]
        resp = input("Digite <S> para continuar.").upper()
        gravar_arquivo(dicionario,arquivo)
    return "JSON gerado!!!!"

def exibir(arquivo):
    dicionario = ler_arquivo(arquivo)
    for chave, dado in dicionario.items():
        print("Data.........: ", dado[0])
        print("Descrição....: ", dado[1])
        print("Departamento.: ", dado[2])

inventario = ler_arquivo("inventario_json.json")
opcao=chamarMenu()
while opcao>0 and opcao<3:
    if opcao==1:
        print(registrar(inventario, "inventario_json.json"))
    elif opcao==2:
        exibir("inventario_json.json")
    opcao = chamarMenu()