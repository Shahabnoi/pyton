
workHours=int(input("Pls Enter Your Work Housrs: "))       # mizan saat kar
Salary=float(input("Pls Enter Your Salary: "))             # mablagh hoghoghe paye
WorkingHoursAct=int(input("Pls Enter WorkingHoursAct: "))  # saat kar movazzaf 
Rate=float(input("Plz Enter Rate Of ExteraWork: "))        # Zarib ezafe karkar
ExteraHours=0                                              # saat ezafekar
ExteraSalary=0                                             # mablaghe ezafekar
if workHours>WorkingHoursAct:                              #agar mizane karkard bish az movazafi bashad
    ExteraHours=workHours-WorkingHoursAct                  #meghdar edafekar moshakhs
    ExteraSalary = (ExteraHours*Rate)*(Salary)             #va mizan hoqoq ezafe mohasebe mishavad
    Salary=(Salary*WorkingHoursAct)+(ExteraSalary)         #mizane hoqoq paye + hoqoqe ezafekar = daryafti
    print(int(Salary))
else:                                                      #darsorate karkard normal faghat mohase hoghogh
    print(int(Salary*workHours))  
    
    ###          

