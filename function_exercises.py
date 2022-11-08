# would like to use regexp
import re

def is_two(x):
    #testing to see if x arg is equivalent to 2 or two
    if x == 2 or x == "two":
         result = True
         #send back the answer
         return result
          
#2---
def is_vowel(x):
    #lower case to avoid mistakes
    x = x.lower()
    # checking to see = any vowerl
    if x == 'a' or x == 'e' or x == 'i' or x =='o' or x == 'u':
        result = True
        return result
    else:
        
        result = False
        return result


#3---
def is_constant(x):
    #lower case to avoid mistakes
    x = x.lower()
    # checking to see = any vowerl
    if x == 'a' or x == 'e' or x == 'i' or x =='o' or x == 'u':
        result = False
        return result
    else:
        
        result = True
        return result


#4---
def is_word(char):
    # accepts string and if string index 0 is not a vowel, capitalize it
    if char[0] == 'a' or char[0] == 'e' or char[0] == 'i' or char[0] =='o' or char[0] == 'u':
        return char
    else:
        up_char = char.capitalize()
        return up_char


#5-----
def calculate_tip(per,check):
    #two arguments
    #take the percent and divide it by 100 for deciaml
    grat = per/100
    #how much the tip os
    total_tip = ( grat * check)

    return total_tip
#6-----
def apply_discount(op,dp):
    #discount price * original price
    dp_per = dp/100
    #original price - subtract amount for the price you will pay
    
    new_price = (1-dp_per)* op
    return new_price


#7----
def handle_commas(char):
    #remove commas
    no_commas = char.replace(',','')
    #cast int type to string
    num_commas =int(no_commas)
    
    return num_commas


#8----
def get_letter_grade(x):
    #if, elif to categorically find grade letter
    if x == 100 or x > 89:
        return "A"
    elif x == 89 or x > 79:
        return "B"
    elif x == 79 or x  > 69:
        return "C"
    elif x == 69 or x > 59:
        return "D" 
    else:
        return "F" 
#9----
#import re
def remove_vowels(char):
    #using re.sub to take list, apply to char as well as ingore casing
    result = re.sub(r'[AEIOU]', '', char, flags=re.IGNORECASE)
    return result

remove_vowels(' howdy nav,MYE ENAMEIOS NAVU ')
    
#10---

def normalize_name(char):
    #strip trailing white space and leading
    no_white = char.strip()
    #lower case all
    low_char = no_white.lower()
    #replace spaces with underscore
    space_char = low_char.replace(' ','_')
    
#11---

def cumulative_sum(list):
    #creat new list
    new_ls = []
    #take len of input list and store in variable
    length= len(list)
    #apply list attributes for the range of length + 1, sum, then apply to new list.
    new_ls = [sum(list[0:x:1]) for x in range(1,length+1)]
    
    return new_ls

    