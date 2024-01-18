#MÓDULO 06 DO CURSO FIAP PYTHON

#--------Sockets--------------

#PROBLEMA 01

import socket
resp="S"
while(resp=="S"):
    url=input("Digite uma url: ")
    ip=socket.gethostbyname(url)
    print("O IP referente à url informada é: ", ip)
    resp=input("Digite <s> para continuar: ").upper()
   
#PROBLEMA 02

print(socket.getservbyname("domain"))
print(socket.getservbyname("http"))
print(socket.getservbyname("ftp"))

#PROBLEMA 03

#parte do servidor

servidor="127.0.0.1"
porta=43210
obj_socket = socket(AF_INET, SOCK_STREAM)
obj_socket.bind((servidor,porta))
obj_socket.listen(2)
print("Aguardando cliente....")
while True:
    con, cliente = obj_socket.accept()
    print("Conectado com: ", cliente)
    while True:
        msg_recebida = str(con.recv(1024))
        print("Recebemos: ", str(msg_recebida)[2:-1])
        msg_enviada = bytes(input("Sua resposta: "), 'utf-8')
        con.send(msg_enviada)
        break
    con.close()

#parte do cliente

servidor="127.0.0.1"
porta=43210

while True:
    obj_socket = socket(AF_INET, SOCK_STREAM)
    obj_socket.connect((servidor, porta))
    msg = bytes(input("Sua mensagem: "), 'utf-8')
    obj_socket.send(msg)
    resposta=obj_socket.recv(1024)
    print("Resposta do Servidor: ", str(resposta)[2:-1])
    if str(msg)[2:-1].upper()=="FIM":
        break
obj_socket.close()


#--------Sockets - UPD--------------

#SERVIDOR

from socket import *
servidor="127.0.0.1"
porta=43210
obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.bind((servidor,porta))
print("Servidor pronto....")
while True:
    dados, origem = obj_socket.recvfrom(65535)
    print("Origem..........: ", origem)
    print("Dados recebidos.: ", dados.decode())
    resposta=input("Digite a resposta: ")
    obj_socket.sendto(resposta.encode(), origem)
obj_socket.close()

#CLIENTE

from socket import *

servidor="127.0.0.1"
porta=43210
obj_socket = socket(AF_INET, SOCK_DGRAM)
obj_socket.connect((servidor, porta))
saida=""
while saida!="X":
    msg = input("Sua mensagem: ")
    obj_socket.sendto(msg.encode(), (servidor,porta))
    dados, origem = obj_socket.recvfrom(65535)
    print("Resposta do Servidor: ", dados.decode())
    saida=input("Digite <X> para sair: ").upper()
obj_socket.close()

#--------Protocolo FPD--------------

#PROBLEMA 01

from ftplib import *
ftp_ativo=False
ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())
usuario=input("Digite o usuario: ")
senha=input("Digite a senha: ")
ftp.login(usuario, senha)
print("Diretório atual de trabalho: ", ftp.pwd())
ftp.cwd('pub')
print("Diretório corrente: ", ftp.pwd())
print(ftp.retrlines('LIST'))
ftp.quit()

#PROBLEMA 02

import os
def escreverLinha(data):
    arq.write(data)
    arq.write(os.linesep)
ftp_ativo=False
ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())
ftp.login()
arquivo='LEIAME'
ftp.set_pasv(ftp_ativo)
with open (arquivo, 'w') as arq:
    ftp.retrlines('RETR README', escreverLinha)
ftp.quit()

#PROBLEMA 03

ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())
ftp.login()
ftp.cwd('/pub/linux/logos/pictures')
with open ('pai_do_linux.jpg', 'wb') as arq:
    ftp.retrbinary('RETR linus-father-of-linux.jpg', arq.write)
ftp.quit()

#PROBLEMA 04

ftp_ativo=False
ftp = FTP(input("Digite o FTP que se deseja conectar: "))
print(ftp.getwelcome())
usuario=input("Digite o usuario: ")
senha=input("Digite a senha: ")
ftp.login(usuario, senha)
print("Conexão bem sucedida.
Diretório atual de trabalho: ", ftp.pwd(),"

")
menu="1"
while menu=="1" or menu=="2" or menu=="3":
    menu=input("Escolha a opção desejada: "
               "
<1> - para Listar arquivos"
               "
<2> - para definir um diretório"
               "
<3> - para baixar um arquivo: ")
    if menu=="1":
        print(ftp.dir())
    elif menu=="2":
        ftp.cwd(input("Digite o diretório que deseja entrar: "))
        print("
Diretório corrente é: ", ftp.pwd())
    elif menu=="3":
        tipo=input("Digite <B> para arquivo binário ou "
                   "
qualquer outra letra para arquivo ASCII: ").upper()
        if tipo=="B":
            with open(input("Digite o nome do arquivo destino: "), 'wb') as arq:
                ftp.retrbinary('RETR ' + input("Arquivo de origem: "), arq.write)
        else:
            with open(input("Digite o nome do arquivo destino: "), 'w') as arq:
                def escreverLinha(data):
                    arq.write(data)
                    arq.write(os.linesep)
                ftp.retrlines('RETR ' + input("Arquivo de origem:"), escreverLinha)
        print("Arquivo baixado com sucesso!

")
ftp.quit()