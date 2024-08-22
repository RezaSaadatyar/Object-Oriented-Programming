class student:
    users = []                   # Class variable to store list of user names
    users_course = {}            # Class variable to store dictionary mapping user names to their courses
    
    def __init__(self, name, email, password, receive):
        self.name = name         # Instance variable to store the student's name
        self.email = email       # Instance variable to store the student's email
        self.password = password # Instance variable to store the student's password
        self.receive = receive   # Instance variable to store whether the student wants to receive updates
        student.users.append(self.name)  # Adds the new student's name to the class variable list `users`
        print(f"{self.name} is added.")

    def __del__(self):
        # Remove the student's name from users and their course registration when object is deleted
        if self.name in student.users:
            student.users.remove(self.name)
            print(f"{self.name} removed from users list.")
        if self.name in student.users_course:
            del student.users_course[self.name]
            print(f"{self.name} course registration removed.")

    def login(self, name):
        # Print the account status based on the presence in the users list
        if name in student.users:
            print(f"{name} has an account.")
        else:
            print(f"{name} must register.")

    def buy(self, coursename):
        student.users_course[self.name] = coursename  
        print(f"{self.name} bought {coursename}.")

# Creating and managing students
student_jame = student("jame", "jame@.com", "1234", True)
student_jame.buy("matlab")

student_sara = student("sara", "sara@.com", "5678", True)
student_sara.buy("python")

student_f = student("f", "f@.com", "5478", True)
student_f.login("f")

# Printing initial state
print(student.users)  # Expected: ['jame', 'sara', 'f']
print(student.users_course)  # Expected: {'jame': 'matlab', 'sara': 'python'}

# Explicitly delete the student_jame to trigger __del__
del student_jame

# Printing state after deleting 'jame'
print(student.users)  # Expected: ['sara', 'f']
print(student.users_course)  # Expected: {'sara': 'python'}
