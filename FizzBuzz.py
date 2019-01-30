
print ("Welcome to Fizz Buzz")

number = int(input("Enter A Number:"))


numberstr = str(number)

for x in range(1, number):


    if (x % 3 == 0) and (x % 5 == 0):
        print()
        print(x)
        print("Fizz Buzz")

    elif x % 3 == 0:
        print()
        print(x)
        print("Fizz")

    elif x % 5 == 0:
        print()
        print(x)
        print("Buzz")

