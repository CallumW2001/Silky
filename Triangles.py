import math

triangle = str(input("Would You Like To Find A Side Or Type Of Triangle (Side / Type)").capitalize())

if triangle == "Type":

    a = int(input("Enter Side 1 Of The Triangle: "))
    b = int(input("Enter Side 2 Of The Triangle: "))
    c = int(input("Enter Side 3 Of The Triangle: "))


    if (a == b == c):
        print("This Is An Equilateral Triangle")

    elif (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2):
        print("This Is A Right Angled Triangle")

    elif a == b or a == c or b == c:
        print("This Is An Isoceles Triangle")

    else:
        print("This Is A Regular Triangle")

elif triangle == "Side":

    d = int(input("Enter Side 1 Of The Triangle"))
    e = int(input("Enter Side 2 Of The Triangle"))
    f = int(input("Enter The Angle Opposite The Side You Would Like To Find"))

    g = ((d**2 + e**2) - (2*d*e) * math.cos(f))

    ans = math.sqrt(g)

    print (ans)




    

else:
    
    print()

