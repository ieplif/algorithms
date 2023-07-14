# Hash function: insert a String and return a number.
# Dictionaries


#Ex. 1:
notebook = dict()  # or notebook = {}

notebook['apple'] = 0.67
notebook['milk'] = 1.49
notebook['avocado'] = 1.49

print(notebook)
print(notebook['avocado'])

#Ex.2:

voted = {}

def check_voter(name):
    if voted.get(name):
        print('Trun away!')
    else:
         voted[name] = True
         print('Let vote!')

check_voter('Tom')
check_voter('Mike')
check_voter('Tom')
check_voter('Maria')

