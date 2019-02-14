
def printStacks(s1,s2,s3):
    #Prints All 3 Stacks
    s1.print()
    s2.print()
    s3.print()




#Trying to move from one stack to another
def move(stackA, stackB):
    #If the stack is empty, print the selected stack is empty - meaning there is nothing to take out of the stack.
    if (stackA.isEmpty() == True):
        print("Stack selected is empty.")

    elif (stackB.isEmpty() == True):

          #A value is popped off the end and stored as a variable, this number stored is then added to the end of a new stack.
          value1 = stackA.pop()
          stackB.push(value1)
          print(value1, "moved.")

    else:

        value1 = stackA.peek()
        value2 = stackB.peek()
        
        #If both stacks have values, check the values at the top of both of the stacks. If the value being moved is smaller than the top item on the
        # stack it is being moved too, then the value can be taken off A and added onto B.
        
        if value1 < value2:
            value1 = stackA.pop()
            stackB.push(value1)
            print(value1, "moved.")
        
        #If Value 1 is > than value 2, than the value can not be moved onto the second stack.
        
        else:
            print(value1, "cannot be moved here.")
        

class Stack:

    #new stacks are created as a blank list
    def __init__(self):
        self.items = []

    #peek will check if stack is not empty returns the end value in the stack.
    def peek(self):
        if self.isEmpty() != True:
            return self.items[self.size()-1]
        else:
            return 0


    #check if stack is empty and return True or False
    def isEmpty(self):
        return self.items == []

    #push will add a value to the end of the stack
    def push(self, item):
        self.items.append(item)

    #pop will remove the end value from the stack and return it
    def pop(self):
        return self.items.pop()

    #size will return the number of items in the stack
    def size(self):
        return len(self.items)

    #print will print the list of items in the stack
    def print(self):
        print(self.items)



def main():
    
    s1 = Stack()
    s2 = Stack()
    s3 = Stack()

    s1.push(4)
    s1.push(3)
    s1.push(2)
    s1.push(1)

    printStacks(s1,s2,s3)

    while(len(str((s2))) != 4 or len(str(s3))) != 4:

        p_1 = int(input("Enter The Stack To Move From : "))
        p_2 = int(input("Enter The Stack To Move To : "))

        if(p_1 == 1 and p_2 == 2):
            move(s1,s2)

        elif(p_1 == 1 and p_2 == 3):
            move(s1,s3)

        elif(p_1 == 2 and p_2 == 1):
            move(s2,s1)

        elif(p_1 == 2 and p_2 == 3):
            move(s2,s3)

        elif(p_1 == 3 and p_2 == 1):
            move(s3,s1)

        elif(p_1 == 3 and p_2 == 2):
            move(s3,s2)

        printStacks(s1,s2,s3)

    

if __name__ == "__main__":
    main()
