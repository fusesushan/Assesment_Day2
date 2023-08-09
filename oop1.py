"""Create a Python class to represent a University. The university should have
attributes like name, location, and a list of departments. Implement encapsulation to
protect the internal data of the University class. Create a Department class that
inherits from the University class. The Department class should have attributes like
department name, head of the department, and a list of courses offered. Implement
polymorphism by defining a common method for both the University and
Department classes to display their details.
"""

class University:
    def __init__(self, name, location):
        self.__name = name #__ is for private members/attributes
        self.__location = location
        self.__departments = []

    def add_department(self, department):
        self.__departments.append(department)

    def display_details(self):
        print(f"University Name: {self.__name}")
        print(f"Location: {self.__location}")
        print("Departments:")
        for department in self.__departments:
            print(f"- {department.get_name()}")
        print("\n")

class Department(University):
    def __init__(self, name, location, dept_name, head):
        super().__init__(name, location)
        self.__dept_name = dept_name
        self.__head = head
        self.__courses = []

    def add_course(self, course):
        self.__courses.append(course)

    def get_name(self):
        return self.__dept_name

    def display_details(self):
        print(f"Department Name: {self.__dept_name}")
        print(f"Head of Department: {self.__head}")
        print("Courses Offered:")
        for course in self.__courses:
            print(f"- {course}")
        print("\n")


# Create instances of University and Department
university = University("Tribhuvan University", "Balkhu")

dept1 = Department("Tribhuvan University", "Pulchowk", "Engineering", "Dr. Sashidhar Ram Joshi")
dept1.add_course("Computer Engineering")
dept1.add_course("Civil Engineering")
dept1.add_course("Electronics And Communication Engineering")

dept2 = Department("Tribhuvan University", "Balkhu", "Management", "Dr. ABC")
dept2.add_course("BBS")
dept2.add_course("BBA")
dept2.add_course("HM")

# Add departments to the university
university.add_department(dept1)
university.add_department(dept2)

# Display university and department details
university.display_details()

for department in university._University__departments:
    department.display_details()
