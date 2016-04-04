height = input("Height (m): ")
weight = input("Weight (kg): ")
bmi = weight/(height*height)
print bmi
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25.0:
    print("Normal Weight")
elif 25.0 <= bmi < 30.0:
    print("Overweight")
else:
    print("Obese")