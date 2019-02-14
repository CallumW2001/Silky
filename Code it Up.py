
sentence = str(input("Enter A Sentence : "))

split_sentence = sentence.split(" ")

newlist = []
numlist = []

for digits in sentence:   

    if(digits != " "):

        digits = ord(digits)
        digits = digits + 25
        digits = chr(digits)


        

    newlist.append(digits)

joined = "".join(newlist)
    
print(joined)

    

