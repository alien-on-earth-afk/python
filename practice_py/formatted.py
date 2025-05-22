#a python script to wrap the string in a width of 50 chars each line
import textwrap

s = input("Enter the string: ")

f = textwrap.fill(s, 50)
print(f)