x = input("Current currency")
y = input("Required currency")
X1 = "USA"
X2 = "INDIA"
X3 = "EUROPE"
Amount1 = float(input())
if x==X1:
    if y==X2:
        Finalamount=Amount1*83.74
        print(Finalamount)
if x==X2:
    if y==X1:
        Finalamount=Amount1/83.74
        print(Finalamount)
if x==X3:
    if y==X2:
        Finalamount=Amount1*91.02
        print(Finalamount)
if x==X3:
    if y==X1:
        Finalamount=Amount1*1.08715
        print(Finalamount)
if x==X2:
    if y==X3:
        Finalamount=Amount1/91.02
        print(Finalamount)
if x==X2:
    if y==X3:
        Finalamount=Amount1/91.02
        print(Finalamount)
