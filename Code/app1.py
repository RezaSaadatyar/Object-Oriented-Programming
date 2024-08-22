class student:
    users = []                   # Class variable to store list of user names
    users_course = {}            # Class variable to store dictionary mapping user names to their courses
    
    def __init__(self, name, email, password, recive):
        self.name = name         # Instance variable to store the student's name
        self.email = email       # Instance variable to store the student's email
        self.password = password # Instance variable to store the student's password
        self.recive = recive     # Instance variable to store whether the student wants to receive updates
        student.users.append(self.name)  # Adds the new student's name to the class variable list `users`
        print(f"{self.name} is added.")
    
    def __del__(self):
        if self.name in student.users:
            student.users.remove(self.name)  # Remove the student's name from the users list when object is deleted
            print(f"{self.name} removed from users list.")
        if self.name in student.users_course:
            del student.users_course[self.name]  # Also clean up any course registration
            print(f"{self.name} course registration removed.")

    def login(self, name):
        if name in student.users:
            print(f"{name} has an account.")
        else:
            print(f"{name} must register.")
            
    def buy(self, coursename):
        student.users_course[self.name] = coursename
        print(f"{self.name} bought.")  

# Create instances and manage them
student_aa = student("jame", "a@.com", "2547", True)
student_aa.buy("matlab")
student_rr = student("sara", "r@.com", "247", True)
student_rr.buy("python")

# Continue with other operations
student_rr.login("f")
student_f = student("f", "f@.com", "5478", True)
student_f.login("f")
print(student.users) 
print(student.users_course)

# To remove "aa", delete the student_aa object
del student_aa  # This should trigger __del__ for student_aa

print(student.users)  # Expected: ['rr']
print(student.users_course)  # Expected: {'rr': 'python'}