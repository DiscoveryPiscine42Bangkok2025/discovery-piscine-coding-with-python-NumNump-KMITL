while True:
    user_input = input("What you gotta say? : ").strip()
    if user_input == "STOP":
        break
    else:
        print("I got that! Anything else? : ", end="")
