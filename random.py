import random

#
# x = random.randint(1, 6)
# y = random.random()
#
# myList = ['rock', 'paper', 'scissors']
# z = random.choice(myList)
#
# cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 'j', 'k', 'q', 'a']
# random.shuffle(cards)
#
# print(cards)

x = []
n = 200
for i in range(n):
    x.append(random.randint(1, 600))
print(x)
