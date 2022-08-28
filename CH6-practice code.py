#Program 1
num1=int(input("Write num1: "))
num2=int(input("Write num2: "))
num3=int(input("Write num3: "))
num4=int(input("Write num4: "))
if(num1>num2):
    f1=num1
else:
    f1=num2

if(num3>num4):
    f2=num3
else:
    f2=num4
if(f1>f2):
    print("It is highest number: ",f1)
else:
    print("It is highest number: ",f2)   

#Program 2
Student_percentage1=int(input("Write percentage1 of student: "))
Student_percentage2=int(input("Write percentage1 of student: "))
Student_percentage3=int(input("Write percentage1 of student: "))
if(Student_percentage1<33 or Student_percentage2<33 or  Student_percentage3<33):
    print("You are fail due to less marks in subject")
else:
    print("you are pass")
if((Student_percentage1+Student_percentage2+Student_percentage3)/3)<40:
    print("You are fail because of less percentage")
else:
    print("you are pass")

#program3
spam_list=["make a lot of money",'buy now','subscribe this','click this']
write=input("write your line: ")
if("make a lot of money" in write):
  spam=True
elif('buy now'in write):
  spam=True
elif('buy now'in write):
  spam=True
elif('buy now'in write):
  spam=True
else:
    spam=False
if(spam):
    print("This is spam")
else:
    print('this is not spam')
 

#Program5
User_name=input('Write a user name: ')
Character_count=len(User_name)
if(Character_count<10):
    print("It is less than 10")
else:
    print("It is not less than 10")

#program6
List_1=["make a lot of money",'buy now','subscribe this','click this']
name_Give=input("Write the name: ")
if(name_Give in List_1 ):
    print("It is in list")
else:
    print("It is not in list")

#program 7
marks=int(input("enter your marks"))
if marks>=90:
    print("Excellent")
elif marks>=80:
    print("A")
elif marks>=70:
    print("B")
elif marks>=60:
    print("C")
elif marks>=50:
    print("D")
elif marks<50:
    print("Fail")

#program7
post=input("Write down the post\n")
if("Harry" in post):
    post=True
elif("harry" in post):
    post=True
else:
    post=False

if(post):
    print("Its talking about harry")
else:
    print("Its not talking about harry")