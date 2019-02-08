import random

gridlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]




def main():

    print("Welcome To Noughts And Crosses")
    
    grid()
    checkwin()

    while(checkwin() == False):

        
            playermove(int(input("Please Pick A Position (1 - 9) To Move To : ")))
            checkwin()
            if(checkwin() == True):
                break
            grid()
            computermove()
            checkwin()
            if(checkwin() == True):
                break
            grid()

        

def grid():

    print(str(gridlist[0]) + " | " + str(gridlist[1]) + " | " + str(gridlist[2]))
    print(str(gridlist[3]) + " | " + str(gridlist[4]) + " | " + str(gridlist[5]))
    print(str(gridlist[6]) + " | " + str(gridlist[7]) + " | " + str(gridlist[8]))

def playermove(text):

    if(gridlist[text-1] != 'O'):
    
        gridlist[text-1] = 'X'

    else:
       print("This Slot Is Already Taken!")

    print()

def computermove():

    rnd = random.randint(1,9)

    if(gridlist[rnd-1] != 'X'):

        gridlist[rnd-1] = 'O'
       
    else:
       print("This Slot Is Already Taken!")


    print()

def checkwin():

    win = False

    if(gridlist[0] == 'X' and gridlist[4] == 'X' and gridlist[8] == 'X' or gridlist[0] == 'X' and gridlist[1] == 'X' and gridlist[2] == 'X' or gridlist[3] == 'X' and gridlist[4] == 'X' and gridlist[5] == 'X' or gridlist[6] == 'X' and gridlist[7] == 'X' and gridlist[8] == 'X' or gridlist[0] == 'X' and gridlist[3] == 'X' and gridlist[6] == 'X' or gridlist[2] == 'X' and gridlist[5] == 'X' and gridlist[8] == 'X' or gridlist[2] == 'X' and gridlist[4] == 'X' and gridlist[6] == 'X' or gridlist[1] == 'X' and gridlist[4] == 'X' and gridlist[7] == 'X'):
       
       print("The Player Has Won!")
       win = True

    elif(gridlist[0] == 'O' and gridlist[4] == 'O' and gridlist[8] == 'O' or gridlist[0] == 'O' and gridlist[1] == 'O' and gridlist[2] == 'O' or gridlist[3] == 'O' and gridlist[4] == 'O' and gridlist[5] == 'O' or gridlist[6] == 'O' and gridlist[7] == 'O' and gridlist[8] == 'O' or gridlist[0] == 'O' and gridlist[3] == 'O' and gridlist[6] == 'O' or gridlist[2] == 'O' and gridlist[5] == 'O' and gridlist[8] == 'O' or gridlist[2] == 'O' and gridlist[4] == 'O' and gridlist[6]== 'O' or gridlist[1] == 'O' and gridlist[4] == 'O' and gridlist[7] == 'O'):
       print("The Computer Has Won!")
       win = True

    return win

    
if __name__ == "__main__":
    main()
