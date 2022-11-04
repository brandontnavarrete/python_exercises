
#1a----------------------
day_of_week = input( "What day of the week is it * using m, t, w, th, f, sa, su *" )

if day_of_week == 'm':
    print("I hate mondays, am i right?")
else:
    print(" At least it's  not monday.")
#b-----------------------
day_of_week = input( "What day of the week is it * using m, t, w, th, f, sa, su *" )

if day_of_week == 'm':
    print("I hate mondays, am i right?")
elif day_of_week == 't':
    print("Hang in there, weekend will be here before you know it.") 
elif day_of_week == 'w':
    print("The weekend is just around the bend.") 
elif day_of_week == 'th':
    print("The weekend is just over the horizon.") 
elif day_of_week == 'f':
    print("TGIF!!!") 
else:
    print("The weekend couldn't come fast enough")
    
#2----------------------
#a
i = 5
while i <= 15:
    print (i)
    i += 1

#---
i = 0
while i <= 100:
    print(i)
    i += 2
#---
i = 100
while i >= -15:
    print(i)
    i -= 5
#---
i = 2
while i <= 1000000:
  
    print(i)
    i = i * i

#---
i = 100
while i >= 5:
    print(i)
    i -= 5
#---

#b--
your_num = int(input("What number would you like to see multiplied?"))


for n in range (1,11):
    print (your_num,' x ', n ,' = ',your_num * n)
 
    
#c---
n = 9

for x in range(1, n+1):
   for y in range (1,x+1):
        print (x) \n
        
print()
 
 #c---
neg_num = int(input("a NEGATIVE NUM please?"))


i = neg_num
while i <= 1:
    print(i)
    i += 1
         
#---
pos_num = int(input("a POSITIVE NUM please?"))


i = pos_num
while i >= 0:
    print(i)
    i -= 1
     
#--Prompt the user for an odd number between 1 and 50.
# Use a loop and a break statement to continue prompting the user if 
# they enter invalid input. 
# (Hint: use the isdigit method on strings to determine this). 
# Use a loop and the continue statement to output all the odd numbers 
# between 1 and 50,
# except for the number the user entered.

odd_num = int(input("an ODD number BETWEEN 1 - 50 please?"))

i = 1
while i < 2:
    if odd_num % 2 == 0 or odd_num > 50 or odd_num < 1 :
     print ("this num doesn't work")
     odd_num = int(input("an ODD number BETWEEN 1 - 50 please?"))
    
    else: 
        break

for i in range (odd_num):
    if i % 2 == 1:
        if i == 27:
            print('yikes! skipping number : 27')
    
            continue
    print(i)
    
#3-----------
i = 1

for n in range (100):
   print (i)
   i += 1

#----

i =1

for i in range(1,101):
    if i % 3 == 0:
        print("Fizz")
   
    else:
        print(i)
#--
i = 1

for i in range(1,101):
    if i % 5 == 0:
        print("Buzz")
   
    else:
        print(i)
        
#--
i = 1

for i in range(1,101):
    if i % 3== 0 and i % 5 == 0:
        print("FizzBuzz")
        
    else:
        print(i)
      
        
#or
   
    
for i in range(1,101):
    if i % 3== 0 and i % 5 == 0:
        print("FizzBuzz")
        continue
    elif i % 3== 0:
            print("Fizz")
    elif i % 5 == 0:
                print("Buzz")
    else:
        print(i)

#


def go():
    stop = int(input("Choose a stopping point."))
    
    for x in range(1,stop+1):
     square = x * x
     cube = x * x * x
     print(F'{x}  |\t{square}  |\t{cube} ')

go()
    
again = str(input('would you like to go again?y/n'))

if again == 'y':
    go()
else:
    print('Goodbye')


            
#----
def test_res():
    grade = int(input("enter grade from 0 -100 "))

    if grade >= 0 or grade <= 100:
        print("calculating...")
        if grade == 100 or grade >= 88:
            print('A')
        elif grade == 87 or grade >= 80:
            print('B')
        elif grade == 79 or grade >= 67:
            print('C')
        elif grade == 66 or grade >= 60:
            print('D')
        else:
            print('F')

    again = str(input("Do you need any more evals? y/n?"))
    if again == 'y':
        test_res()
    else:
        print('Stay Sharp!')
        

test_res()

#----
ls_book = [ {'title': 'jam', 'author':'micheal bay','genre':'spook'},
            
            {'title': 'pb and j', 'author':'brandon','genre':'fiction'},
            
            {'title': 'cars', 'author':'musk','genre':'fantasy'},
            
            {'title': 'health tips', 'author':'michelle obama','genre':'lifestyle'},
             
            {'title': 'how george washington defeated anakin', 'author':'J.R.T','genre':'nonfiction'},
            
            {'title': 'space admin', 'author':'usaf','genre':'military'} ]
           

#---
g_p = (str(input("pick a genre ")))
gen_pick = g_p.lower()
match = [item for item in ls_book if item['genre'] == gen_pick]

for ls_book in match:
    print('title:',ls_book['title'])
    print('author:',ls_book['author'])
    print('genre:',ls_book['genre'])