name = input("enter your name: ")
weight = float(input("Enter your weight in kilogramss : "))
height = float(input("Enter your height in meters : "))
BMI = (weight)/(height *height)
print(f"BMI = {BMI}")
print(weight)
if (BMI > 0):
    if(BMI < 18.5):
        print(name +", You are under-weight.")
    elif(BMI <= 24.9):
        print(name +", You are normal-weight.")
    elif(BMI <= 29.9):
        print(name +", You are over-weight.")
    elif(BMI <= 34.9):
        print(name +", You are obese.")
    elif(BMI <= 39.9):
        print(name +", You are severely-obese.")
    elif(BMI >= 40):
        print(name +", You are morbidly-obese")
else:
    print("Enter valid input.")