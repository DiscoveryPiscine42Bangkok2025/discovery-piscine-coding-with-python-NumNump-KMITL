number_input = input("Give me a number : ")
number = float(number_input)

if number.is_integer() : 
    print("This number is an integer.")
else:
    print("This number is a decimal.")