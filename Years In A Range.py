#Years In Range
#12/02/2019




for x in range(1000,9999):

    newlist = []

    stringx = str(x)

    for digits in stringx:
     
        newlist.append(digits)

    if (newlist[0] == newlist[1] or newlist[0] == newlist[2] or newlist[0] == newlist[3] or newlist[1] == newlist[2] or newlist[1] == newlist[3] or newlist[2] == newlist[3]):


     print(newlist)
    

   
