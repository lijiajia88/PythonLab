class Student:
    def __init__(self, first_name, last_name, course):
        self.first_name = first_name
        self.last_name = last_name
        self.course = course
        self.enrolled_modules = []

    def enrolStudent(self, module_code):
        self.enrolled_modules.append(module_code)

    def changeCourse(self, new_course):
        self.course = new_course

    def showDetails(self):
        enrolled_modules_str = ", ".join(self.enrolled_modules)
        print(f"Student: {self.first_name} {self.last_name}")
        print(f"Course: {self.course}")
        print(f"Enrolled Modules: {enrolled_modules_str}")
        print()


class Module:
    def __init__(self, name, code, tutor):
        self.name = name
        self.code = code
        self.tutor = tutor
        self.enrolled_students = []

    def enrolStudent(self, student):
        self.enrolled_students.append(student)
        student.enrolStudent(self.code)

    def showAllEnrolledStudents(self):
        enrolled_students_str = ", ".join([f"{student.first_name} {student.last_name}" for student in self.enrolled_students])
        print(f"Module: {self.name}")
        print(f"Code: {self.code}")
        print(f"Tutor: {self.tutor}")
        print(f"Enrolled Students: {enrolled_students_str}")
        print()



def main():

    # Create some students and some modules ...
    s1 = Student('ken','barlow','english')
    s2 = Student('mike','baldwin','business')
    s3 = Student('harold','legg', 'medicine')

    m1 = Module('English language and semantics', 'A101','Wanda Pickle')
    m2 = Module('Engineering principles','E102','Buzz Jones')
    m3 = Module('Anatomy','M105','Greg House')

    # Now enrol some students on some modules ...
    m1.enrolStudent(s1)
    m1.enrolStudent(s2)
    m2.enrolStudent(s1)
    m2.enrolStudent(s3)

    # Have a look at some students and some modules ...
    s1.showDetails()
    s2.showDetails()
    s3.showDetails()

    m1.showAllEnrolledStudents()
    m2.showAllEnrolledStudents()
    m3.showAllEnrolledStudents()

    # Change a course ...
    s1.changeCourse('engineering')
    s1.showDetails()


if __name__ == "__main__":
    main()
