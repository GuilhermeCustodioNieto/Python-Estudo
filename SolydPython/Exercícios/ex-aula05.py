"""
EXERCICIO: Faça um programa que leia a quantidade de pessoas que
serao convidadas para uma festa.
Após isso o programa irá¡ perguntar o nome de todas as pessoas e
colocar numa lista de convidados
Após isso irá¡ imprimir todos os nomes da lista
"""
number_guests = int(input("Write the number of guests: "))
guests_list = []

for i in range(number_guests):
  guests_list.append(input(f"Write the name of {i  + 1 } guest"))

print("The guests list is: ")
for i in range(len(guests_list)):
  print(f" {i+1}: \t {guests_list[i]}")