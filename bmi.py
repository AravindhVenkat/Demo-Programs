def bmi_range():
    if bmi < 18.5:
        print("Underweight")
    elif (bmi > 18.5) and (bmi < 25):
        print("Healthy weight!")
    elif (bmi > 25) and (bmi < 30):
        print("Overweight")
    else:
        print("Obesity")


system = input("(M)etric or (I)mperial system? ").upper()
if system == 'M':
    weight_kg = float(input("Weight in kg: "))
    height_cm = float(input("Height in cm: "))
    bmi = (weight_kg / ((height_cm / 100) ** 2))
    print('%.2f' % bmi)
    bmi_range()

elif system == 'I':
    weight_lbs = float(input("Weight in lb: "))
    height_feet = float(input("Height in feet: "))
    height_inches = float(input("remaining inches: "))
    height_total_inches = height_feet * 12 + height_inches
    bmi = ((weight_lbs * 703) / (height_total_inches ** 2))
    print('%.2f' % bmi)
    bmi_range()

else:
    print('Please use M or I !!!')
