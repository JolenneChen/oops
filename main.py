class Students:
    school_name = "nanyang"

    # constructor
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.grades = {}
    
    def study(self):
        print(f"{self.name} is studying ")

    def report_card (self,subject,grade):
        self.grades[subject] = grade
        # {"maths": 90}
        print(f"\n**{self.name}'s report card**")   

        for subject,grade in self.grades.items():
            print(f"{subject} : {grade}")

if __name__ == "__main__":
    # create an object
    s1 = Students("Maggie",15,"Female")
    s1.study()
    s1.report_card("Physics" , 79)
    s1.report_card("Chemistry", 92)

    s2 = Students("Darren", 14, "Male")
    s2.study()
    s2.report_card("Physics",81)
    


