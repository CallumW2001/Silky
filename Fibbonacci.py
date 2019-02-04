a = 1
b = 0
c = 1

digits = int(input("Enter The Number Of Places You Would Like It To: "))


while len(str(c)) <= (digits):
    
    c = (a + b)
    b = a
    a = c

    if (len(str(c)) <= digits):
        
        print (c)

    else:
        print()
