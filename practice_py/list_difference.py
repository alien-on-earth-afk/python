#write a Python program to calculate the difference between the two lists.

list1 = input("Enter the list1: ").input()
list2 = input("Enter the list2: ").input()

diff_list1_list2 = list(set(list1) - set(list2))
diff_list2_list1 = list(set(list2) - set(list1))

total_diff = diff_list1_list2 + diff_list2_list1

print(total_diff)