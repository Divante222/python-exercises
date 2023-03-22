# Define a function named is_two. It should accept one 
# input and return True if the passed input is either 
# the number or the string 2, False otherwise.

def is_two(a):
    if a == 2 or a == '2':
        return True
    return False

# is_two('3')


# Define a function named is_vowel. 
# It should return True if the passed string 
# is a vowel, False otherwise.

def is_vowel(a):
    vowels = ['a','e','i','o','u']
    if a.lower() in vowels:
        return True
    return False


# is_vowel('e')


# Define a function named is_consonant. 
# It should return True if the passed string is a consonant, 
# False otherwise. Use your is_vowel function to accomplish this.

def is_consonant(a):
    vowels = ['a','e','i','o','u']
    if a.lower() not in vowels:
        return True
    return False


is_consonant('e')


# Define a function that accepts a string that is a word. 
# The function should capitalize the first letter of the word 
# if the word starts with a consonant.

def the_funct(word):
    vowels = ['a','e','i','o','u']
    print(word)
    if word[0].lower() not in vowels:
        return word.capitalize()
    return word
    
# the_funct('eating')  


# Define a function named calculate_tip. 
# It should accept a tip percentage (a number between 0 and 1) and the bill total, 
# and return the amount to tip.

def calculate_tip(tip_percent, bill_total):
    return (tip_percent * bill_total) + bill_total

# calculate_tip(.1, 10)

# Define a function named apply_discount. 
# It should accept a original price, 
# and a discount percentage, and return the price after the discount is applied.

def apply_discount(orig_price, disc_percent):
    return orig_price - (orig_price * disc_percent)

# apply_discount(10, .1)

# Define a function named handle_commas. 
# It should accept a string that is a number that contains commas 
# in it as input, and return a number as output.

def handle_commas(num_str):
    num_str = num_str.split(',')
    new_str = ''
    for i in num_str:
        if i != ' ':
            new_str += i
    return int(new_str)

# the_str = handle_commas('12,323,45,')
# print(the_str)

# Define a function named get_letter_grade. 
# It should accept a number and return the 
# letter grade associated with that number (A-F).

def get_letter_grade(number):
    if number < 101 and number > 89:
        return 'A'
    elif number <= 89 and number >= 80:
        return 'B'
    elif number <= 79 and number >= 70:
        return 'C'
    elif number <= 69 and number >= 60:
        return 'D'
    elif number <= 59 and number >= 0:
        return 'F'
    return 'You did not return a valid grade'
# print(get_letter_grade(100))
    


# Define a function named remove_vowels that accepts 
# a string and returns a string with all the vowels removed.

def remove_vowels(the_str):
    new_str = ''
    vowels = ['a','e','i','o','u']
    for i in the_str:
        if i not in vowels:
            new_str = new_str + i
            
    return new_str

# remove_vowels('apple')



# Define a function named normalize_name. 
# It should accept a string and return a valid python identifier, that is:

# anything that is not a valid python identifier should be removed

# leading and trailing whitespace should be removed

# everything should be lowercase

# spaces should be replaced with underscores

# for example:
    
# Name will become name

# First Name will become first_name

# % Completed will become completed

def normalize_name(the_str):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t',
               'u','v','w','x','y','z', ' ', '_']
    alphabet_x = 'abcdefghijklmnopqrstuvwxyz _'
    new_str = ''
    for i in the_str:
        if i.lower() in alphabet:
            new_str = new_str + i
            
    new_str = new_str.lower()
    new_str = new_str.lstrip()
    new_str = new_str.rstrip()
    new_str = new_str.replace(' ', '_')
    
    return new_str
    
# print(normalize_name('%     dIvante walter parness     %'))

# Write a function named cumulative_sum that accepts a list of numbers 
# and returns a list that is the cumulative sum of the numbers in the list.

# cumulative_sum([1, 1, 1]) returns [1, 2, 3]

# cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

def cumulative_sum(list_of_numbers):
    total = 0
    new_list = []
    for i in list_of_numbers:
        
        total = total + i
        new_list.append(total)
    return new_list
        
    
# print(cumulative_sum([1, 2, 3, 4]))
# print(cumulative_sum([1, 1, 1]))

# Create a function named twelveto24. function_exercises.py
# It should accept a string in the format 10:45am or 
# 4:30pm and return a string that is the representation 
# of the time in a 24-hour format. 

def twelveto24(the_str):
    str_to_return = '0'
    
    str_to_return_condensed = ''
    
    last_two_letters = the_str[len(the_str):len(the_str) - 3: -1]
    last_two_letters = last_two_letters[1:] + last_two_letters[0:1]
    
    
    if last_two_letters.lower() == 'am':
        
        if len(the_str[:len(the_str) - 2]) == 5:
            
            str_to_return = the_str[:len(the_str) - 2]
            
            for i in str_to_return:
                str_to_return_condensed = str_to_return_condensed + i
            
            return str_to_return_condensed
        
        else:
            str_to_return = (str_to_return + the_str[:len(the_str) - 2]).split(':')
            for i in str_to_return:
                str_to_return_condensed = str_to_return_condensed + i
            
            return str_to_return_condensed
        
    if last_two_letters == 'pm':
        first_two_numbers = str(int(the_str[:2]) + 12)
        str_to_return_for_pm = first_two_numbers + the_str[2:] 
        
        
        str_to_return_for_pm = str_to_return_for_pm.replace('pm', '')
        
        return str_to_return_for_pm
    

# print(twelveto24('10:45am'))

# Bonus write a function that does the opposite.
def totwelve(the_str):
    
    first_two_numbers = int(the_str[:2])
    if first_two_numbers > 12:
        first_two_numbers = str(first_two_numbers - 12)
        first_two_numbers = first_two_numbers + the_str[2:] + 'pm'
        return first_two_numbers
    
    elif first_two_numbers <= 12:
        first_two_numbers = str(first_two_numbers - 12)
        if first_two_numbers == '0':
            first_two_numbers = first_two_numbers + '0'
            
        first_two_numbers = first_two_numbers + the_str[2:] + 'am'
        return first_two_numbers

        

# print(totwelve('12:45'))

# url = "https://gist.githubusercontent.com/ryanorsinger/bec2f59a9cef8ae7428cb70b3541354a/raw/ef64298da52e5d70f4d388f5fd48eccdb02ed3f1/ice_cream.csv"
# Create a function named col_index. 
# It should accept a spreadsheet column name, and return the index number of the column.
# col_index('A') returns 1
# col_index('B') returns 2
# col_index('AA') returns 27

def col_index(spreadsheet_column_name):
    number_im_on = 1
    multiply_the_letter = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    the_letter_multiplied = ''
    the_dictionary_of_letters = {}

    for i in range(spreadsheet_column_name):
        multiply_the_letter += 1
        
        for i in alphabet:
            the_letter_multiplied = i.upper() * multiply_the_letter
            the_dictionary_of_letters[the_letter_multiplied] = number_im_on
            number_im_on += 1
            


    for j in the_dictionary_of_letters.items():
       print(j)

    while True:
        print('Enter a letter to get the column number')
        column_letter = input('')

        print('the letter', column_letter, 'is at column', the_dictionary_of_letters[column_letter.upper()])
        print()
        print('Do you want to continue? y/n')
        choice = input('')
        if choice.upper() == 'N':
            break
    return the_dictionary_of_letters

# print('enter a number')
# the_size_of_the_csv = int(input(''))
# the_dictionary = col_index(the_size_of_the_csv)

