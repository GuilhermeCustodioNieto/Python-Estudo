from datetime import date

class Account:
	extract = []
	
	def __init__(self, client, balance, limit):
		self.client = client
		self.balance = balance
		self.limit = limit
		
	def withdrawal(self, ammount):
		if(self.balance >= ammount):
			self.balance -= ammount
			self.extract.append(f"{date.today()}\t-{ammount}")
			print("Withdrawal performed!")
		else:
			print("Unfulfilled withdrawal")
			
	def deposit(self, ammount):
		if ammount <= self.limit:
			self.extract.append(f"{date.today()}\t+{ammount}")
			self.balance += ammount
		else:
			print("#"*50)
			print("Insufficient Funds")
	
	def get_balance(self):
		user_balance = f"Your balance:\t{self.balance}"
		return user_balance 
		
	def get_extract(self):
		all_extracts = ""
		for i in self.extract:
			all_extracts += f"{i}\n"
		return all_extracts
		