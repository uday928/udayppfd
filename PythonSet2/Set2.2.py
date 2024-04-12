class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"Student: {self.name}, Age: {self.age}, Grade: {self.grade}"

class Teacher:
    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject
        self.courses_taught = []

    def assign_course(self, course):
        self.courses_taught.append(course)

    def __str__(self):
        return f"Teacher: {self.name}, Age: {self.age}, Subject: {self.subject}, Courses taught: {', '.join(self.courses_taught)}"

class Course:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.students_enrolled = []

    def enroll_student(self, student):
        self.students_enrolled.append(student)

    def __str__(self):
        return f"Course: {self.name}, Teacher: {self.teacher.name}, Students enrolled: {[student.name for student in self.students_enrolled]}"

# Sample usage
if __name__ == "__main__":
    student1 = Student("Alice", 15, 10)
    student2 = Student("Bob", 16, 11)

    teacher1 = Teacher("Mr. Archimedes", 35, "Math")
    teacher2 = Teacher("Ms. Newton", 40, "Science")

    course1 = Course("Mathematics", teacher1)
    course2 = Course("Physics", teacher2)

    teacher1.assign_course("Mathematics")
    teacher2.assign_course("Physics")

    course1.enroll_student(student1)
    course2.enroll_student(student2)

    print(student1)
    print(student2)
    print(teacher1)
    print(teacher2)
    print(course1)
    print(course2)