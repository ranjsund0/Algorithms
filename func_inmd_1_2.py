import random

def randInt(min= 0 , max= 100):
    # num = random.random() * max
    # return round(num)

num= random.random() * min + min

print(randInt())
print(randInt(max=50))
print(randInt(min=50))


print(randInt(min=50, max=500))

num = random.random() *(max-min) + min