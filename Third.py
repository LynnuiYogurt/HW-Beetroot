import random

word=input('enter the word: ')
print(*[''.join(random.sample(word,len(word))) for _ in range(5)],sep='\n')