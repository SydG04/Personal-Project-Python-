'''
Sydney Gilmore
BMI calculator
Fuctions practice
'''
def main():
    print ("Please be aware that your units are in INCHES (no feet) and pounds.")
    print ("And keep in mind this is not 100% accurate. They are other factors are play besides your weight and height.")
    name, weight, height = stats()
    calc(name, weight, height)

def stats():
    name = input("Enter your name: ")
    weight = eval(input("Enter your weight in pounds (lbs): "))
    height = eval(input("Enter your height in INCHES ONLY (in): "))
    return name, weight, height

def calc(name, weight, height):
    BMI = weight / (height * height) * 703
    print (name+"'s BMI is",BMI)
    if BMI > 0:
      if BMI < 16:
        print('You are severely underweight')
      elif BMI < 17:
        print('You are moderately underweight')
      elif BMI < 18.5:
        print('You are underweight')
      elif BMI < 25:
        print('You are healthy')
      elif BMI < 30:
        print('You are overweight')
      elif BMI < 35:
        print('You are moderately obese')
      elif BMI <= 40:
        print('You are severely obese')
      elif BMI > 40 :
        print('You are morbidly obese')
    else:
      print('The information that you put in is incorrect')    

main()

'''
Psudeocodede
- Disclaimer: These units are in inches (no feet) and pounds
- Have user input their name
- Have user input their stats (weight, height)
- Calculate BMI
- Output their stats and put disclaimer (this is NOT 100% accurate)
'''
