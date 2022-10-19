# Kondratskyi
import functools


# 1
def favorite_movie(name):
	print(f'My favorite movie is named {name}')


# 2
def countries(countrie, capital):
	my_dict = {}
	my_dict[countrie]=capital
	print(my_dict)


#3
def make_operation(operator,*nums):
	if operator=='+':
		print(functools.reduce(lambda a, b: a+b, nums))
	elif operator=='*':
		print(functools.reduce(lambda a, b: a*b, nums))
	else:
		print(functools.reduce(lambda a, b: a-b, nums))





