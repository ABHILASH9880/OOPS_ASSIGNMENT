class Student:
    def _init_(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_grade(self):
        return self.grade
    
    def set_name(self, name):
        self.name = name
    
    def set_age(self, age):
        self.age = age
    
    def set_grade(self, grade):
        self.grade = grade


# Create new student 
student1 = Student("John Doe", 18, "A")

# Get student's name
name = student1.get_name()
print("Name:", name)

# Get student's age
age = student1.get_age()
print("Age:", age)

# Get student's grade
grade = student1.get_grade()
print("Grade:", grade)

# Update student's name
student1.set_name("john king")
new_name = student1.get_name()
print("New Name:", new_name)

    