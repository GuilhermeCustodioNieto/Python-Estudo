'''
EXERCICIO:
FaÃ§a um programa que pergunte a idade, o peso e a altura
de uma pessoa e decide se ela estÃ¡ apta a ser do Exercito
Para entrar no exercito Ã© preciso ter mais de 18 anos
pesar mais ou igual  60 kilos
e medir mais ou igual 1,70 metros
'''

idade = int(input("digite sua idade: "))
peso = float(input('digite seu peso: '))
altura = float(input("Digite sua altura: "))

if idade >= 18 and peso >= 60 and altura>= 1.70: 
  print("Você está apto a entrar para o exercito! ")
else:
  print("Você não tem od requisitos minimos para entrar no exercito")
