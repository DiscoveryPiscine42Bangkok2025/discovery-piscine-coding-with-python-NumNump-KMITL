number = int(input("Enter a number less than 25\n"))

if number <= 25:
    while number <= 25 :
        print("Inside the loop, my vatiable is",number)
        number += 1

elif number > 25:
    print("Error")
