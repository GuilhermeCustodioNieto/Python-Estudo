"""
EXERCICIO: Crie um software de gerenciamento banc´ario
Esse software poder´a ser capaz de criar clientes e contas
cada cliente possui nome, cpf, idade
cada conta possui um cliente, saldo, limite, sacar, depositar e consultar saldo
"""
from entities.Account import Account
from entities.Client import Client

#Registro dos clientes
print("Clients Register: ")
client_list = []
number_custommers = int(input("Write the number of custommers: "))

for i in range(number_custommers):
	print("."*50)
	print(f"\tClient {i+1}")
	custommer_name = input("Write the custommer name: ")
	custommer_rg = input("Write the custommer rg: ")
	custommer_cpf = input("Write the CPF: ")
	
	client_list.append(Client(custommer_name, custommer_rg, custommer_cpf))
	
#Registro das contas dos usuarios
print("-"*50)

print("Enter the accounts of users")
account_list = []
for i in client_list:
	account_limit = float(input("Enter the account limit: "))
	account_balance = float(input("Enter the account_balance: "))
	account_list.append(Account(i, account_balance, account_limit))

#Uso das contas
#O usuario escolhe uma opção e de acordo com ela, algo ocorre
current_account = 0
while True:
	print("-"*50)
	print("Choose a option: ")
	chosen_option = int(input((f"""
	1\tChoose a account
	2\tMake deposit
	3\tMake withdrawal
	4\tGet balance
	5\tGet extract
	""")))
	
	if chosen_option == 1:
		for j in range(len(account_list)):
			print(f"{j}:\t{account_list[j].client.name}")
		current_account = account_list[int(input("Choose a account_option: "))]
	
	elif chosen_option == 2:
		account_list[current_account].deposit(float(input("Write the quantity for deposit: ")))
	
	elif chosen_option == 3:
		account_list[current_account].withdrawal(float(input("Write the quantity for withdrawal: ")))
	
	elif chosen_option == 4:
		print(f"Name:\t{account_list[current_account].client.name}")
		print(f"Balance:\t{account_list[current_account].get_balance()}")
		
	elif chosen_option == 5:
		print(account_list[current_account].get_extract())
	
	else:
		print("#"*50)
		print("Invalid option! ")