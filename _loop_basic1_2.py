_loop_basic1.py
Basics
def basic():
for i in range(151):
    print(i)
basic()

Multiples of Five
def multiples_of_five():
# for num in range(5,1001, 1):
#     if num % 5 == 0:
#         print(num)
multiples_of_five()

Counting, the Dojo Way
def the_dojo_way():
for num in range(101):
    if num % 5 == 0:
        print("Coding")
    elif num % 10 == 0:
        print("Coding Dojo")
    else:
        print(i)
the_dojo_way()

Whoa. That Sucker's Huge
def woah_huge():
sum = 0
for num in range(500000):
    if num % 2 != 0:
        sum += num
        print(sum)
woah_huge()

def countdown_by_fours():
for num in range(2018,0, -4):
        print(num)
countdown_by_fours()

def flexible_counter(low_num, high_num, mult):
for num in range(low_num, high_num, mult):
    if num % mult == 0:
        print(num)
flexible_counter(2,9,3)