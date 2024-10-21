def nameAge(school, name, age):
    print("Hi, I am ", name)
    print("My age is ", age)
    print("The name of my school is ", school)

# nameAge("unilag", name="Richard", age=24)
# nameAge("Unibadan", name="Benson", age=21)




def greet_user(first_name, last_name="LastName", middle_name="MiddleName"):
    # return "My name is " + first_name + ' ' + middle_name + ' ' + last_name
    return f"My name is {first_name} {middle_name} {last_name}"


# print(greet_user('Yusuf', 'Adeyemi', 'Raymond'))
# print(greet_user("Rooney"))
# print(greet_user("Sarah"))

# def thesquare(thenum):
#     return (thenum * thenum)
    
# print(thesquare(3))

thesquare = lambda thenum: thenum * thenum

myfullname = lambda first_name, last_name: f'My name is {first_name} {last_name}'

anotherlambda = lambda myname: "Welcome to coding class"

print(anotherlambda("Gbenga"))
# print(thesquare(4))
# print(myfullname("yusuf", "Adeyemi"))

# let thesquare2 = function() => {}

# kwargs

# newsquare = thesquare(4)

# print(newsquare)
# print(thesquare(4))


# def myinfo(name, age, school):
#     thename = f'My name is {name} '
#     theage = f'I am {age} years old '
#     theschool = f'The name of my school is {school}'
#     theinfo = thename + theage + theschool
#     return theinfo

# print(myinfo("Yusuf Adeyemi", 26, "Unilag"))
# newinfo = myinfo("Yusuf Adeyemi", 26, "Unilag")
# print(newinfo)



def calsquare(thenum):
    # return thenum * thenum
    theresult = thenum * thenum
    return "THe adddition of 3 + 3 is "+ str(theresult)

# print(calsquare(3))

# result = calsquare(4)
# print(result)


# devname = input("What is your name?")

# def greetuser(name):
#     print(f'Hi {name}')
#     print('Welcome onboard developer')


# greetuser("Smith", first_name="John")

# def clickme():
#     print("This is the click me button")

# clickme()