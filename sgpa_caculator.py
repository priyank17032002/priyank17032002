class sgpa:
    def __init__(self):
        self.n_course = 0
        self.total_credit = 0.0
        self.courseCredit = []
        self.courseGradePoint = []
        self.sgpa = 0.0
        self.temp2 = 0
        self.temp3 = 0
        self.temp4 = 0
        self.temp5 = 0
   def details(self):
        print("Sgpa Calculator! \n")
        self.total_credit = eval(input("Enter total credit of this semester :"))
        self.n_course = int(input("How many courses you have : "))
        for i in range(0,self.n_course):
            self.temp2 = int(input("%s Credit Hour : \n" %self.courseCode[i]))
            self.courseCredit.append(self.temp2)
            self.temp3 = int(input("%s Grade Point : \n" %self.courseCode[i]))
            self.courseGradePoint.append(self.temp3)
   def calculation(self):
        for i in range(0,self.n_course):
            self.temp5 = self.courseGradePoint[i] * self.courseCredit[i]
            self.temp4 = self.temp4 + self.temp5
        self.sgpa = (self.temp4 / self.total_credit)
   def result(self):
        print ("Your Courses : \n%s\n" %self.courseCode)
        for i in range(0,self.n_course):
            print ("Credit of %s = %d" %(self.courseCredit[i]))
            print("Grade Point of %s = %d" %(self.courseCode[i], self.courseGradePoint[i]))
        print ("\nYour SGPA is : %.2f" %(self.sgpa))

ob = sgpa()

ob.details()

ob.calculation()

ob.result()
