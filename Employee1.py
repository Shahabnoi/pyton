

class Employee:
      def __init__(self, name, family, WorkingHoursAct):
          self.name = name
          self.family = family
          self.WorkingHoursAct = WorkingHoursAct
      workHours = 190
      Salary = 10000
      Rate = 2
      ExteraHours = 0                                          
      ExteraSalary = 0 
      
      def pay(self):
       if self.workHours < self.WorkingHoursAct:                     
          self.ExteraHours = self.WorkingHoursAct - self.workHours                
          self.ExteraSalary = (self.ExteraHours*self.Rate)*(self.Salary)             
          self.Salary=(self.Salary * (self.WorkingHoursAct - self.ExteraHours))+(self.ExteraSalary)         
          print(int(self.Salary))
       else:                                                     
          print(int(self.Salary*self.workHours)) 

      def EmployeePay(self):
             print( "Mizan daryafti " + self.name,self.family  )
     
p1 = Employee("John", "Cage" , 200)
p2 = Employee("jak", "polman", 190)
p1.EmployeePay()  
p1.pay()  
print("mibashad")
p2.EmployeePay()    
p2.pay()  
print("mibashad")

