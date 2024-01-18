"""
Escreva uma funç˜ao que recebe um objeto de coleç˜ao e retorna o valor do maior numero dentro dessa coleç˜ao e outra funç˜ao que retorna o menor valor dessa coleç˜ao
"""

def bigger(colecao):
	maior =0
	for i in colecao:
		maior = i
		break
	for i in colecao:
		if i >= maior:
			maior = i
	return maior

def smaller(colecao):
	menor = 0
	for i in colecao:
		menor = i
		break

	for i in colecao:
		if i <= menor:
			menor = i
	return menor
	
my_collection = set()
size_collection = int(input('Write the size of collection: '))

for i in range(size_collection):
	my_collection.add(int(input(f'Write the {i+1} number: ')))

print(f"The bigger of collection is: \t{bigger(my_collection)}")
print(f"The smaller of collection is: \t{smaller(my_collection)}")