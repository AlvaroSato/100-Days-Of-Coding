'''
Write a program that calculates the BMI from a users weight and height

BMI = weight in KG / height in Meters ^ 2
'''

if __name__ == "__main__":
    height = float(input("Please insert your height in cm: "))
    weight = float(input("Please insert your weight in kg: "))

    try:
        height = height / 100
        bmi = weight / height**2
        print(f'Your BMI: {bmi}')
    except:
        print('Sorry, i think you need to review your input')
        print(f'Height: {height} | This need to be a number, float or integer')
        print(f'Weight: {weight} | This need to be a number, float or interger')