# Import and test 3 of the functions from your functions exercise file. Import each function in a different way:
import function_exercises as fe
from function_exercises import calculate_tip 
import itertools as iter
import json
# Run an interactive python session and import the module. Call the is_vowel function using the . syntax.

print(fe.is_vowel('e'))

# Create a file named import_exericses.py. Within this file, use from to import the calculate_tip function directly. Call this function with values you choose and print the result.
print(calculate_tip(.1, 10))


# Create a jupyter notebook named import_exercises.ipynb. Use from to import the get_letter_grade function and give it an alias. Test this function in your notebook.

# Read about and use the itertools module from the python standard library to help you solve the following problems (Hint: wrap the itertools results in a list to see the results).




# How many different ways can you combine a single letter from "abc" with either 1, 2, or 3?
print(iter.product('ABCD'))
the_list = ['A','B','C',1, 2 ,3]
the_new_list = []
for i in iter.product(the_list, repeat=2):
    the_new_list.append(i)

print(the_new_list)
count = 0
for j in the_new_list:
    
    if type(j[1]) == type(1) and type(j[0]) == type('d'):
        count += 1
print(count)



the_second_list = []

# How many different combinations are there of 2 letters from "abcd"?
for i in iter.product('abcd',repeat=2):
    the_second_list.append(i)
for j in the_second_list:
    print(j)

print(len(the_second_list))

    

# How many different permutations are there of 2 letters from "abcd"?

list_of_strings = []
for i in the_second_list: 
    if (i[1],i[0]) not in list_of_strings:
        list_of_strings.append(i)

print(len(list_of_strings))
print(list_of_strings)
  
    


# Save this file as profiles.json inside of your exercises directory (right click -> save file as...).

# Use the load function from the json module to open this file.
# Your code should produce a list of dictionaries. Using this data, write some code that calculates and outputs the following information:
print('\n\n')

read_file = json.load(open('profiles.json')) 


    
# Total number of users
names_list = []
for i in read_file:
    names_list.append(names_list)
print('the number of users is', len(names_list),'\n\n')

# Number of active users
is_active = []
for i in read_file:
    if i["isActive"]:
        is_active.append(i["isActive"])
print('the number of active users is', len(is_active), '\n\n')

# Number of inactive users
is_inactive = []
for i in read_file:
    if not i["isActive"]:
        is_inactive.append(i["isActive"])
print('the number of inactive users is', len(is_inactive), '\n\n')

# Grand total of balances for all users

total = 0
total_list = []
the_str_total = ''
for i in read_file:
    total_list.append(i["balance"])
for i in total_list:
    the_str_total = i.replace(',', '')
    the_str_total = the_str_total.replace('$', '')
    total = total + float(the_str_total)
    
print('the total balance for all users is', total, '\n\n')


# Average balance per user
count = 0
total = 0
total_list = []
the_str_total = ''
for i in read_file:
    total_list.append(i["balance"])
for i in total_list:
    count +=1
    the_str_total = i.replace(',', '')
    the_str_total = the_str_total.replace('$', '')
    total = total + float(the_str_total)
    
print('the average balance for all users is', round((total / count), 2), '\n\n')

# User with the lowest balance

total_list = []
the_str_total = ''
for i in read_file:
    total_list.append(i["balance"])


print('the lowest balance for all users is', min(total_list), '\n\n')


# User with the highest balance


total_list = []
the_str_total = ''
for i in read_file:
    total_list.append(i["balance"])


print('the highest balance for all users is', max(total_list), '\n\n')

# Most common favorite fruit

fruit_list = []
fruit_dict = {}
the_str_total = ''
for i in read_file:
    fruit_list.append(i["favoriteFruit"])
for j in set(fruit_list):
    fruit_dict[j] = 0
for k in fruit_list:
    fruit_dict[k] += 1


old = ''
old_value = 0

for i in fruit_dict.keys():
    
    if old_value == 0:
        old_value = fruit_dict[i]
        old = i
        
    if fruit_dict[i] < old_value:
        old = i


   


print(fruit_dict)
print('the least common favorite fruit is', old, '\n\n')


# Least most common favorite fruit

old = ''
old_value = 0

for i in fruit_dict.keys():
    
    if old_value == 0:
        old_value = fruit_dict[i]
        old = i
        
    if old_value < fruit_dict[i]:
        old = i

print(fruit_dict)
print('the most common favorite fruit is', old, '\n\n')


# Total number of unread messages for all users
messages_list = []
for i in read_file:
    messages_list.append(i["greeting"])


message_number = ''

new_list = []

for j in messages_list:  
    for h in j:
        if h.isnumeric():
            message_number += h
            
            
        
    new_list.append(message_number)
    message_number = ''

    total_messages = 0
for i in new_list:
    total_messages += int(i)

print('there are a total of', total_messages, 'total messages')
    

        


