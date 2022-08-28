# '''
# class is always written in pascal case
# pascal case
# 1)Employeename
# 2)Reserved

# camel case
# 1)isnum
# 2)isfloat
# '''
# #Class attributes
# class employee:
#     company="google"
#     '''company is directly assosiated with class,coz
#     all employess work in same company
#     '''

# muneeb=employee
# #changing an attribute in class
# employee.company='youtbe'
# print(muneeb.company)


# #instance atrributes
# '''Some atributes such as age address phone number
# is diffrent of al employess so it is instance attributes'''
# class employee:
#      company="google"
#      salary=100

# muneeb=employee
# print(muneeb.company)
# print(muneeb.salary) #By default it is 100 as a class atrribute so it will print 100
# #now we will use instance attribute to change according to rrequirnmrnts
# muneeb.salary=400
# print(muneeb.salary) 
# #now it will print 400 but by default salary is 100 in class it will add new          


# #Understanding self concept 
# #self gives the identity to new object created
# class employee:
#      salary=1000
#      def getsalary(self):
#         print(f"The salary of this employee in {self.company} is {self.salary}")

# muneeb=employee()
# muneeb.salary=4900
# muneeb.getsalary()

# #@static methond, if you dont want to use self 
# class employee:
#      company="google"
#      salary=100
#      def getsalary(self):
#         print(f"The salary of this employee in {self.company} is {self.salary}")
#      @staticmethod
#      def greet():
#         print("Heloo sir")

# muneeb=employee()
# muneeb.salary=4900
# muneeb.getsalary()
# muneeb.greet()

# #_init_   case

# class employee:
#       company='youtube'
#       unit="webs"
#       def _init_(self,name,salary,unit): #This helps us in initializing the class attributes
#          self.name=name
#          self.salary=salary
#          self.unit=unit
#       print("Emplooye is created")
#       def emplooye_details(self):
   
#          print(f"The detail of this emlooye are:\nName= {self.name}\nSalary= {self.salary}\nUnit= {self.unit}")

# muneeb=employee()
# muneeb.name="Muneeb ur Rehman"
# muneeb.salary=700
# muneeb.unit="App"
# print(muneeb.emplooye_details())#you can also type ed to call this


# # Class methonds
# '''It is used in case where you want to update the class attribute of a class upto a certain level
# and its very useful coz it directly changes the value of class attribute , lets take an example'''
# "Suppose you want to update salary every year upto a rate "
# class employee:
#     salary=1000
#     def _init_(self,name,city):
#             self.name=name
#             self.city=city
#     @classmethod
#     def update_salary(cls,rate):
#         cls.salary=cls.salary+cls.salary*rate

# muneeb=employee()
# employee.update_salary(0.10)
# print(employee.salary)

#polymorphism is ability to use common interface in diffrent data typre
"Example:Peter parker to spider man"








            
   
