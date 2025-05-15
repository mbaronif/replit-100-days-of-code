class Job:
    name = None
    salary = None
    hoursWorked = None

    def __init__ (self, name, salary, hoursWorked):
        self.name = name
        self.salary = salary
        self.hoursWorked = hoursWorked
        
    def jobInfo(self):
        print(f"Job: {self.name}")
        print(f"Salary: ${self.salary}")
        print(f"Hours Worked: {self.hoursWorked}")

class Doctor(Job):
    experience = None
    speciality = None

    def __init__ (self, experience, speciality):
        super().__init__("Doctor", 100000, 40) #super() calls the parent class properties, to avoid repeating the same code
        self.experience = experience
        self.speciality = speciality

    def jobInfo(self): #This method overrides the parent class method and display its info before the new info.
        super().jobInfo()
        print(f"Experience: {self.experience} years")
        print(f"Speciality: {self.speciality}")       

class Teacher(Job):
    subject = None
    position = None

    def __init__ (self, subject, position):
        super().__init__("Teacher", 50000, 40)
        self.subject = subject
        self.position = position   
    
    def jobInfo(self):
        super().jobInfo()
        print(f"Subject: {self.subject} years")
        print(f"Position: {self.position}") 

lawer = Job("Lawyer", 120000, 50)
lawer.jobInfo()
print(f"-----------------------")   
doctor = Doctor(7, "Paediatric Consultant")
doctor.jobInfo()
print(f"-----------------------")   
teacher = Teacher("Computer Science", "Teacher")
teacher.jobInfo()

