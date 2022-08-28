#Program 1
players_in_cricket=12
players_you_have= int(input("how many players you have?: "))

if players_you_have>players_in_cricket:
    print("You have exceeded the limit")
elif players_you_have>=players_in_cricket:
    print("you have fulfilled the criteria")
else:
    print("You have less players")

#Conditional expression harry modification
#1
a=input("Write a number: ")
a=int(a)
if(a>9):
    print("It is greater")
else:
    print("It is less")

#2
ali_score=input("Write a number: ")
ali_score=int(ali_score)
if(ali_score==100):
    print("Ali has scored a century")
elif(ali_score==50):
    print("Ali has completed his half century")
elif(ali_score>=200):
    print("Ali has scored a double century")
else:
    print("Ali has scored less runs")

#Statements with logic AND
age= int(input('What is your age= '))
if(age>25 and age<40):
    print("You can work with us")


#Statements with logic or
age= int(input('What is your age= '))
if(age==20 or age<40):
    print("You can work with us")

#statements with in 
a=[1,4,3]
if(3 in a):
    print("yes")
else:
    print("no")




