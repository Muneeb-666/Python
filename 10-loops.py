# # While and for loops
# # 1)while loops
x=1
while(x<15):
    x=x+2
    print(x)
# 2) For loop
for x in range(5,10):
    print(x)

# #break and continue command
d={"muneeb","ali","asad"}
for days in d:
    # if(days=="ali"):break #loop stops when ali comes
    if(days=="ali"):continue #skips value in d and prints all others
    print(days)

# #While loop code with harry
i=0
while i<10:
    print("This loop will run until i is less than 10 " +str(i))
    i=i+1

# #Quick quiz 
i=0
while i<50:
    i=i+1
    print(i)
# #Reading contents of list using while loop
list=['a','c','d','h','u','r','q','r']
print(len(list))
i=0
while i<len(list):
    print(list[i])
    i=i+1

# #Reading contents of list using for loop
list=['a','c','d','h','u','r','q','r']
for items in list:
    print(items)

# #Range function
for i in range(8):
    print(i) #It will print values upto "i-1"
for i in range(1,8):
    print(i)
for i in range(1,8,2):  #step size
    print(i)

# #For loop with else statement
for i in range(1,5,2):  #step size
    print(i)
else:
    print("Loop is stop now")

# #Break statement
for i in range(1,5,2):  #step size
     print(i)
     if i==3:
       break

# #Continue statement, It skips the number and print all others
for i in range(1,20):  #step size
     if i==3:             
#It will print numbers from 1 to 20 but 3 will not be included
      continue
     print(i)

# #List of odd number using for and range function
for i in range(1,20):  #step size
     if (i%2==0):
      continue
     print(i)#It will skip the numbers meeting the condition 

# #List of Even number using for and range function
for i in range(1,20):  #step size
     if (i%2==1):
      continue
#      print(i)#It will skip the numbers meeting the condition


#Practice programs
#1)Multiplication table of a given number
num=int(input("Enter a number= "))
for i in range(1,11):
 print( str(num) +  "x"  + str(i)+  "="  +str(i*num))  
# 
#f string (In refrence to previous program)
print(f"{num}X{i}={num*i}")

#To print table in reversed order
num=int(input("Enter a number= "))
for i in reversed(range(1,11)):

 print(f"{num}x{i}= {num*i}")

#2)Start with function and use of if in for loop
l1= ['muneeb','samad','rehan','ali',"asad"]
for name in l1:
    if name.startswith('a'):
        print("Hello " + name)








