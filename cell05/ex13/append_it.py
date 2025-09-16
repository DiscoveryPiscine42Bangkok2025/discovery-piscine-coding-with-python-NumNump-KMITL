import sys

param = sys.argv[1:]

if not param:
    print("none")
else:
    for param in param:
        if not param.endswith("ism"):
            print(f"{param}ism")
