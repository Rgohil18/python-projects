a = input("Enter the Number")
print(f"Table of {a} is : ")
try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")

except Exception as tryagain:
    print(f"Sorry some error is there{tryagain} ")

