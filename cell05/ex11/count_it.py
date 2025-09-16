import sys

para = sys.argv[1:]

if not para :
    print("none")

else :
    print(f"parameters: {len(para)}")

    for para in para :
        print(f"{para} : {len(para)}")