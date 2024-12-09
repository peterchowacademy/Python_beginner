def reserve (value):
    string = str(value)  
    if string[0] == '-':
        print("-"+string[:0:-1])
    else:
        print(string[::-1])
        


#test cases
reserve("-5432")
reserve("appletree")
reserve("happy-")
reserve("5349")
reserve("-0.921")