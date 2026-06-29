
print("assignment no : 8")

class MyName:
    def __init__(self, fullname, user_multiplication):
       self.fullname = fullname
       self.user_multiplication = user_multiplication
       
    def getmyname(self):
        return f"fullname = {self.fullname} , user_multiplication = {self.user_multiplication}"

    def multiply_with(self, number):
        return number * self.user_multiplication

object = MyName(input("Enter your fullname : ") , int(input("Enter your number : ")))

print(object.getmyname())

result = object.multiply_with(int(input("Enter your number : ")))
print(f"Multiplication Result: {result}")
