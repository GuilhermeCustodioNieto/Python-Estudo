'''
EXERCICIO: FaÃ§a um formulario que pergunte
o nome, cpf, endereco, idade, altura e telefone
e imprima isso em um relatorio organizado
'''

nome = input("digite seu nome")
cpf = input("digite seu CPF")
endereco = input("digite seu endereço")
altura = float(input("digite sua altura"))
telefone = input("digite seu telefone")

print(f"nome: \t {nome} \nCPF: \t{cpf} \nEndereço: \t{endereco} \nAltura: \t{altura}\nTelefone: \t{telefone}")