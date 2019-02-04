palindrome = False



while True:

    user = str(input("Input Your Word To Check If It Is A Palindrome Or Not: "))

    for x in range(0, len(str(user))):

        if (user[x] == user[-x-1]):

            palindrome = True
            

        elif (user[x] != user[-x]):

            palindrome = False
            

                
    if (palindrome == True):

        print("This Is A Palindrome")


    elif (palindrome == False):

        print("This Is Not A Palindrome")
        

    rewind = str(input("Would You Like To Play Again? (Yes / No): "))

    if (rewind == "Yes"):

        print()
        
    elif (rewind == "No"):
            
        break

            
