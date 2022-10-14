
# Kondratskyi

import random

while True:
	player = input('write guess number: ')
	if player == 'break':
		break
	player = int(player)
	if not type(player == int):
		print('Chek if its number')
	comp = random.randint(1, 3)
	if comp == player:
		print('Congrats')
		break
	else:
		print('the number is ', comp)
		print('c`mon again or break')


print(f'Hello {input("Your name:")}, on your next birthday you’ll be {int(input("Your age: "))+1} years')


word=input('enter the word: ')
print(*[''.join(random.sample(word,len(word))) for _ in range(5)],sep='\n')