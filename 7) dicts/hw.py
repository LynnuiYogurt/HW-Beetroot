# Kondratskyi



# 1
# #user_input=input().split()
# words=set(user_input)
# numbers=[user_input.count(i) for i in words ]
# print(dict(zip(words,numbers)))


#2
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
total_price=dict(zip([i for i in stock],[stock[i]*prices[i] for i in stock]))
print(total_price)

#3
print(*list(dict.items(dict(zip([i for i in range(1,10)],[j*2 for j in range(1,10)])))))

#4
days=['monday','tuesday ','wednesday','thursday','friday','saturday','sunday']
nums=[i for i in range(1,8)]
print(dict(zip(days,nums)))
print(dict(zip(nums,days)))