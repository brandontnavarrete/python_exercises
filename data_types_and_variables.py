m = 3 #mermaid
b = 5#brother bear
h = 1#hercules


print((m * 3) + (b * 3) + (h * 3 ))

#----------------------

g = 400 #google
a = 380 #amazon
f = 350 #facebook


print((f * 10) + (g * 6) + (a * 4))
#----------------------
class_not_full = True
class_doest_conflict= True
student_can_enroll = class_not_full and class_doest_conflict


print (student_can_enroll)

#----------------------
people_buy_two = True
offer_not_expired = True
premium_member = False

can_be_applied = offer_not_expired and (people_buy_two or premium_member)

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

#check_1 = len(password)>=5
#check_2 = len(username) <20
#check_3 = username != password


#if <condition>:
 #   var = True
#else:
 #   var = False

