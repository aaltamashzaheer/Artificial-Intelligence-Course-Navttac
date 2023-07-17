class Teacher():
    def move(self):
        print("Hello I am move of Teacher class")
        
class Student():
    def move(self):
        print("Hello I am move of Student class")
        
class Room():
    def move(self):
        print("Hello I am move of C1 room class")
        
teacher_obj = Teacher()
student_obj = Student()
room_obj = Room()

teacher_obj.move()
student_obj.move()
room_obj.move()