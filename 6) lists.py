#	Kondratskyi

import random

list1=[]
while len(list1)!=10:
	list1.append(random.randint(1,55))
print(max(list1))




list1=[]
list2=[]
while len(list2)!=10:
	list1.append(random.randint(1,10))
	list2.append(random.randint(1, 10))
print(set(list1+list2))





list1, i = [], 1
while i != 101:
	i += 1
	if i % 7 == 0 and i % 5 != 0:
		list1.append(i)
print(list1)