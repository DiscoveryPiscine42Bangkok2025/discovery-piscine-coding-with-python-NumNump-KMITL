while True:
    user_input = input("What you gotta say? : ").strip()
    if user_input == "STOP":
        # เมื่อพิมพ์ STOP (ไม่สนตัวใหญ่/เล็ก) จะจบโปรแกรม
        break
    else:
        print("I got that! Anything else? : ", end="")