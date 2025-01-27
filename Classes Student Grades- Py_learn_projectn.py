# Classes Student Grades- Py_learn_projectn
class Student:
    def __init__(self, name, rollNum, marks):
        self.name = name
        self.rollNum = rollNum
        self.marks = marks
    def get_average(self):
        self.average = round(sum(self.marks) / len(self.marks),2) 
    def has_passed(self):
        if self.average >= 50:
            print(f'{self.name} has progressed to the next grade with an average of {self.average} %')       
        else:
            print(f'{self.name} has failed this grade')
    def achieved_cum_laude(self):
        if self.average >= 75:
            print(f'Congratulations {self.name} you have obtained a cum laude {self.average} %') 
        else:
            print(f'{self.name} you were {75 - self.average} % away from obtaining a cum laude')       
## Create instances
student1 = Student('Itumeleng Sekoma', 2202, [89,79,82])  
student2 = Student('Nkateko Msiza', 2107, [40,55,32])
student3 = Student('Jeffrey Jackson',2288, [70,63,65]) 
## Call the method to get average 
student1.get_average()
student2.get_average()
student3.get_average()
## Call function to see if student passed or failed  
student1.has_passed()
student2.has_passed()
student3.has_passed() 
## Call function to see if student achieved a distinction pass
student1.achieved_cum_laude()
student2.achieved_cum_laude()
student3.achieved_cum_laude()       
                  
        