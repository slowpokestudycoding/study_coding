user_name = input("Hello！ How would I address you :")
user_name_title = user_name.title()

while True:
      try:
        user_height = float(input("Hello %s！ Please enter your height in centimeters :" % user_name_title))
        break
      except:
        print("Sorry！ Please check your height is a number, don't enter any alphabet and symbol!")
print()
print("Thank you!")
while True:
      try:
        user_weight = float(input("Please enter your weight in kilograms :"))
        break
      except:
        print("Sorry！ Please check your weight is a number, don't enter any alphabet and symbol!")
print()
height_in_meters = user_height/100
user_bmi = user_weight / height_in_meters**2

if user_bmi > 30:
  print("Hello %s!Your BMI is %3.2f. You are obese, pay attention to your body!" % (user_name_title , user_bmi))
elif user_bmi <= 30 and user_bmi > 25:
  print("Hello %s!Your BMI is %3.2f. You are overweight, pay attention to your body!" % (user_name_title , user_bmi))
elif user_bmi <= 25 and user_bmi > 18.5:
  print("Hello %s!Your BMI is %3.2f. Your weight is normal, keep it up!" % (user_name_title , user_bmi))
elif user_bmi <= 18.5:
  print("Hello %s!Your BMI is %3.2f. You are underweight, remember to eat more nutritious foods!" % (user_name_title , user_bmi))
else:
  print("Hello %s! Please check your height and weight again, something wrong in your value!" % user_name_title)

print("Have a nice day!")