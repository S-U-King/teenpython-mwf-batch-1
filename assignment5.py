print("Task No: 01")
number_input = input("Please enter any whole number: ")
num = int(number_input)
marks_input = input("Now, please enter your test score (0-100): ")
marks = float(marks_input)
print("\nCalculating your results...")
if num % 2 == 0:
    print(f"-> The number {num} you entered is an even number.")
else:
    print(f"-> The number {num} you entered is an odd number.")
print("-> Your Grade Report: ", end="")
if 90 <= marks <= 100:
    print(f"An amazing score of {marks}% gives you an A+. Excellent work!")
elif 80 <= marks < 90:
    print(f"With {marks}%, you earned an A. Great job!")
elif 70 <= marks < 80:
    print(f"A solid score of {marks}% gives you a B. Well done!")
elif 60 <= marks < 70:
    print(f"You passed with {marks}%, receiving a C. Good effort!")
elif 50 <= marks < 60:
    print(f"Your score is {marks}%, which is a D. You can improve this next time!")
elif 0 <= marks < 50:
    print(f"A score of {marks}% means a Fail grade. Keep studying, you will do better next time.")
else:
    print("The score you entered seems to be out of the valid 0-100 range.")
