#MÓDULO 03 DO CURSO FIAP PYTHON

#--------dicionarios--------------

#PROBLEMA 01

usuarios={}
opcao=input("O que deseja realizar?
" +
            "<I> - Para Inserir um usuário
"+
            "<P> - Para Pesquisar um usuário
"+
            "<E> - Para Excluir um usuário
"+
            "<L> - Para Listar um usuário: ").upper()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        chave=input("Digite o login: ").upper()
        nome=input("Digite o nome: ").upper()
        data=input("Digite a última data de acesso: ")
        estacao=input("Qual a última estação acessada: ").upper()
        usuarios[chave]=[nome, data, estacao]
    opcao = input("O que deseja realizar?
" +
                  "<I> - Para Inserir um usuário
" +
                  "<P> - Para Pesquisar um usuário
" +
                  "<E> - Para Excluir um usuário
" +
                  "<L> - Para Listar um usuário: ").upper()
                  
 
usuarios[input("Digite o login: ").upper()]=[input("Digite o nome: ").upper(),
                 input("Digite a última data de acesso: "),
                 input("Qual a última estação acessada: ").upper()]
                 
                 
#PROBLEMA 02

def perguntar():
    resposta = input("O que deseja realizar?
" +
                  "<I> - Para Inserir um usuário
" +
                  "<P> - Para Pesquisar um usuário
" +
                  "<E> - Para Excluir um usuário
" +
                  "<L> - Para Listar um usuário: ").upper()
    return resposta

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                          input("Digite a última data de acesso: "),
                                          input("Qual a última estação acessada: ").upper()]
                                          
def pesquisar(dicionario, chave):
    lista=dicionario.get(chave)
    if lista!=None:
        print("Nome...........: " + lista[0])
        print("Último acesso..: " + lista[1])
        print("Última estação.: " + lista[2])

def excluir(dicionario, chave):
    if dicionario.get(chave)!=None:
        del dicionario[chave]
    print("Objeto Eliminado")

def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto......")
        print("Login: ", chave)
        print("Dados: ", valor)
                                          
usuarios={}

opcao=perguntar()
while opcao=="I" or opcao=="P" or opcao=="E" or opcao=="L":
    if opcao=="I":
        inserir(usuarios)
    if opcao=="P":
        pesquisar(usuarios,input("Qual login deseja pesquisar? "))
    if opcao == "E":
        excluir(usuarios,input("Qual login deseja excluir? "))
    if opcao == "L":
        listar(usuarios)
    opcao = perguntar()
    
    
#--------tuplas--------------

#PROBLEMA 01
ips={}
resp="S"
while resp=="S":
    ips[(input("Digite os dois primeiros octetos: "),
       input("Digite os dois últimos octetos: "))]=input("Nome da máquina: ")
    resp=input("Digite <S> para continuar: ").upper()
    
print("Exibindo ip´s: ")
for ip in ips.keys():
    print(ip[0]+"."+ip[1])
    
print("Exibindo as máquinas que compõem uma mesma rede: ")
rede=input("Digite os dois primeiros octetos: ")
for ip,nome in ips.items():
    if(ip[0]==rede):
        print(nome)
        
#PROBLEMA 02

usuarios={}
resp="S"
emails=[]
while resp=="S":
    emails.append(input("Digite um e-mail: ").lower())
    resp=input("Digite <S> para continuar: ").upper()
    
tupla = list(enumerate(emails))
for chave in range(0,len(tupla)):
    print("Email: ", tupla[chave][1])
    usuarios[tupla[chave]]=[input("Digite o nome"), input("Digite o nível")]
    
for chave,dado in usuarios.items():
    print("Usuario.:", chave[0])
    print("Email...: ",chave[1])
    print("Nome....: ", dado[0])
    print("Nível...: ", dado[1])