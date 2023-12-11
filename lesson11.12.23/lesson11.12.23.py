#print("1 ==1", 1==1)
#print("1 ==2", 1==2)
#print("1 !=1", 1!=1)
#print("1 !=2", 1!=2)
#print("1 > 1", 1>1)
#print("1 > 2", 1>2)
#print("1 < 2", 1<2)
#print("1 < 1", 1<1)
#print("1 >= 1", 1>=1)
#print("1 >= 2", 1>=2)
#print("1 <= 1", 1<=1)
#print("1 <= 2", 1<=2)
#print(bool(""))
#print(bool(0.0))
#print(bool(0))
#print(bool(None))
#print(bool("Hello"))
#print(bool(2))
#
##and
#competent= True 
#responsible= False
#print(competent and responsible)
#
##or
#print(competent or responsible)
#
##not
##true - false
##false- true
#print(not competent)

#age= int(input("Enter your age"))
#if age>=18 and age<=120:
 #   print("u can enter")
#else:
#    print("Age is not valid")

#if 18<= age <=120:
#     print("u can enter")
#else:
#    print("Age is not valid")



#if age <18 :
 #   print("age is too small")
#day = int(input("Enter number day of week "))

#if day == 1:
#    print("Monday")
#elif day == 2:
#    print("Tuesday")
#elif day == 3:
#    print("Wednesday")
#elif day == 4:
#    print("Thursday")
#elif day == 5:
#    print("Friday")
#elif day == 6:
#    print("Saturday")
#elif day == 7:
#    print("Sunday")
#else :
#    print("It is not a day of week")

login = input("Enter login: ")
if login == "admin":
    password = input("Enter passsword: ")
    if password == "step":
        print("Welcome to the program: ")
    else :
        print("Password id invalid: ")
elif login == "exit" :
    print("Gooodbye")
else :
    print("Error login ")