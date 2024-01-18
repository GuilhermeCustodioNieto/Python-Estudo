def dictionary_ex(input_user):
  """
  Vai recebr uma string e vai retornar um dicionário que é o contador de cada letra se repetindo na string
  """
  
  alphabet = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0, "v":0, "w":0, "x":0, "y":0, "z":0}
  
  for letter in input_user:
    letter = letter.lower().replace(" ", "")
    if letter in alphabet:
      alphabet[letter] += 1
  
  return alphabet

def average_temperature(daily_temperatures):
  """
  vai receber uma tupla de int e vai retornar uma tupla com a média de numeros, o maior e o menor valor.
  """
  
  average = 0
  min_temperature = 0
  max_temperature = 0
  for temperature in daily_temperatures:
    average += temperature
  
  average /= len(daily_temperatures)
  min_temperature = min(daily_temperatures)
  max_temperature = max(daily_temperatures)
  
  return (average, min_temperature, max_temperature)

def todo_list(tasks_list = []):
  """
  É um gerenciador de tarefas, onde o usuario escolhe a operação que quer fazer e realiza ela.
  """
  
  menu = 0
  while True:
    print("""Choice a option of operation: \n
    1-\tAdd a new task \n
    2-\t Mark a task as complete \n
    3-\tShow tasks \n
    4-\tEnd program
    """)
    
    menu = int(input('Enter here: '))
    
    match menu:
      case 1:
        tasks_list.append(input('Enter the new task here: '))
      case 2:
        choice_complete_task = int(input('Enter the choice of the complete taks: \n1-\tBy index\n2-\tBy element\n'))
        match choice_complete_task:
          case 1:
            tasks_list.pop(int(input('Enter the index of the complete task: ')) -1)
          case 2:
            tasks_list.remove(input('Enter the text of the complete task'))
      case 3:
        for i in range(len(tasks_list)):
          print(f'{i+1}\t{tasks_list[i]}')
      case 4:
        print("End.")
        break
      case _:
        print("Error: this value is wrong")
        continue
    print('-'*50)

def intersection_sets(input_set1 = set(), input_set2 = set()):
  """
  recebe dois sets e retorna as intersecções neles (isso caiu na OBI eu acho)
  """
  
  return input_set1.intersection(input_set2)

print("Dictionary Exercice: ")
count_letters =  dictionary_ex(input('Write a phrase to count all letter'))

for key in count_letters.keys():
  print(f"{key.upper()}:\t{count_letters[key]}")

print("-"*50)

print("Tuple Exercice")
print(average_temperature((23,45, 78, 2)))

print("-"*50)

print("List Exercice")
todo_list()

print("-"*50)

print("Set Exercice")
print(intersection_sets({'Banana', 'Uva', 'Pera'}, {'Goiaba', 'Banana', 'Jaca'}))