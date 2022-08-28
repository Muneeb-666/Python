#single inheritence(Class derived from parent class)

from typing_extensions import Self


class employee:
     company="google"
     salary=100
     def getsalary(self):
        print(f"The salary of this employee in {self.company} is {self.salary}")
class programmer(employee):
        def getsalary(self):
            print(f"The salary of this programmer is {self.salary}")

a=employee()
b=programmer()
b.salary=900
b.getsalary()

#multiple inheritence(more than one parent class one child class)
#basic syntax we can add atributes according to needs and we can repeat them in diffrent classes



class employee:
    company="dell"
    def _init_(self,salary,role,name):
        self.salary=salary
        self.role=role
        self.name=name
    def employee_details(self):
        print(f"Details of employee are:\nName={self.name}\nSalary={self.salary}\nRole={self.role}")
    
class freelancer:
    company="fiveer"
    def _init_(self,Oders,rating,Seller_level):
        self.Oders=Oders
        self.rating=rating
        self.Seller_level=Seller_level
    def frellancer_details(self):
        print(f"Details of Freelancer carrer are:\nOrders={self.Oders}\nrating={self.rating}\nSeller level={self.Seller_level}")

class programmer(employee,freelancer):
    def _init_(self,perfomance,experience):
        self.perfomance=perfomance
        self.experience=experience
    def programmer_details(self):
        print(f"Details of Programmer OVerall perfomance are:\nExperince={self.experience}\nPerfomance={self.perfomance}")


a=freelancer()
a.Oders=90
a.rating=5.0
a.Seller_level="level 2"
a.frellancer_details()
