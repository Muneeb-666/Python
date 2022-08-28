#maximum three numbers
def maximun(a,b,c):
    if (a>=b) and (a>=c):
        largest=a
    elif (c>=a) and (c>=b):
        largest=c
    else:
        largest=b
    return largest

print(maximun(1,2,3))

#2 celcuis to farhaniet
def cel_far(num):
    formula= (num*1.8)+32
    return formula
print(cel_far(34.4))

#3 sum of n numbers
def sum_of(num):
 sum=0
 for i in range(0, num+1):
    sum = sum+i
 return sum 


print(sum_of(2))

#4 multiplication table
def multiplication_tab(n):
    for i in range(1,11):
     mul=n*i
     print(mul)
    #  print( str(n) +  "x"  + str(i)+  "="  +str(i*n))  
    
    return print
print(multiplication_tab(2))