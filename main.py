from random import randint
from random import shuffle
 
  # random
  # Python comes with a built in random library. There are a lot of functions included in this random library, so we will only 
  #show you two useful functions for now.
print("random")

dice1 = randint(1,7)
print(f"dice1  : {dice1}" )

dice2 = randint(1,7)
print(f"dice2  : {dice2}" )

rolled_doubles = dice1 == dice2

if rolled_doubles:
  print("you rolled doubles")
else:
  print("not double")

if dice1 and dice2 == 1:
  print("you rolled snake eye")
else:
  print("you did not roll snake eyes")


my_list = range(1,51)
print(list(my_list))
my_list = list(my_list)
shuffle(my_list)
print(my_list)


new_list = randint(1,201)
print("new_list")
print(new_list)

if new_list % 2==0:
  print("even")
else:
  print("odd")