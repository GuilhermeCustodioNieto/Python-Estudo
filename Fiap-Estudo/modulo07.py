#MÓDULO 07 DO CURSO FIAP PYTHON

#--------Biblioteca Serial--------------

#PROBLEMA 01

import serial
conexao=""
for porta in range(10):
    try:
        conexao = serial.Serial("COM"+str(porta), 115200, timeout=0.5)
        print("Conectado na porta: ", conexao.portstr)
        break
    except serial.SerialException:
        pass
if conexao!="":
    conexao.close()
    print("Conexão encerrada")
else:
    print("Sem portas disponíveis")
    
#PROBLEMA 02

conexao=""
for porta in range(10):
    try:
        conexao = serial.Serial("COM"+str(porta), 115200, timeout=0.5)
        print("Conectado na porta: ", conexao.portstr)
        break
    except serial.SerialException:
        pass
if conexao!="":
    acao=input("Digite:
<L> para Ligar
<D> para Desligar: ").upper()
    while acao=="L" or acao=="D":
        if acao=="L":
            conexao.write(b'1')
        else:
            conexao.write(b'0')
        acao = input("Digite:
<L> para Ligar
<D> para Desligar: ").upper()
    conexao.close()
    print("Conexao encerrada")
else:
    print("Sem portas disponíveis")
    

"""
C++ códigos

void setup()
{
  pinMode(10, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  int intervalo_pisca;
  intervalo_pisca=4000;
  digitalWrite(10, LOW);
  Serial.write('0');
  delay(intervalo_pisca);
  digitalWrite(10, HIGH);
  Serial.write('1');
  delay(intervalo_pisca);
}
"""

#PROBLEMA 03

"""
C++ código

void setup()
{
  pinMode(10, OUTPUT);
  Serial.begin(115200);
}

void loop() {
  int intervalo_pisca;
  intervalo_pisca=4000;
  digitalWrite(10, LOW);
  Serial.write('0');
  delay(intervalo_pisca);
  digitalWrite(10, HIGH);
  Serial.write('1');
  delay(intervalo_pisca);
}
"""

conexao=""
for porta in range(10):
    try:
        conexao = serial.Serial("COM"+str(porta), 115200)
        print("Conectado na porta: ", conexao.portstr)
        break
    except serial.SerialException:
        pass
if conexao!="":
    while True:
        resposta = conexao.read()
        if resposta==b'1':
            print("LED Ligado")
        else:
            print("LED Desligado")
    conexao.close()
    print("Conexão encerrada")
else:
    print("Sem portas disponíveis")
    
#PROBLEMA 04

"""
C++ código

void setup() {
  Serial.begin(115200);
}
void loop() {
  int luz=analogRead(1); 
  Serial.println(luz);
  delay(5000); 
}

"""

import json
import time
from datetime import datetime
conexao=""
for porta in range(10):
    try:
        conexao = serial.Serial("COM"+str(porta), 115200)
        print("Conectado na porta: ", conexao.portstr)
        break
    except serial.SerialException:
        pass
if conexao!="":
    dicionario={}
    cont=0
    while cont<10:
        resposta=conexao.readline()
        dicionario[str(datetime.now())]=[resposta.decode('utf-8')[0:3]]
        print(resposta.decode('utf-8')[0:3])
        cont+=1
    with open('Temperatura.json', "w") as arq:
        json.dump(dicionario, arq)
    conexao.close()
    print("Conexão encerrada")
else:
    print("Sem portas disponíveis")