m = 3
b = 5
h = 1

print((m * 3) + (b * 3) + (h * 3 ))

#----------------------

g = 400 #google
a = 380 #amazon
f = 350 #facebook

print((f * 10) + (g * 6) + (a * 4))
#----------------------
class_full = False
class_interfers = False

student_can_enroll = class_full and not class_interfers

print (student_can_enroll)

#----------------------
people_buy_two = True
offer_not_expired = True

can_be_applied = people_buy_two and offer_not_expired

print (can_be_applied)

#BOOLEAN----
username = 'codeup'
password = 'notastrongpassword'

safe_pass = None

#measure length of password
if (len(password)) >= 5:
    pass_char_stro = True
#measure length of username
if (len(username)) <= 20:
    right_size = True
# testing equality of password and username
if password != username:
    no_match = True

#setting safe_pass value
safe_pass = pass_char_stro and right_size and no_match

safe_pass



#if <condition>:
 #   var = True
#else:
 #   var = False

