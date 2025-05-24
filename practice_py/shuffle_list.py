import random 

s = input("ENter the list: ").split()

#suffle(s)
random.shuffle(s)

print(s)

#sample input: ENter the list: hello i am alien
#ouput: ['alien', 'i', 'am', 'hello']