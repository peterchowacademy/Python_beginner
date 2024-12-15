def Push(x,stack1,stack2):
    '''
    x: value to push
    stack1: list
    stack2: list
    '''
    stack1.append(x)

#Function to pop an element from queue by using 2 stacks.
def Pop(stack1,stack2):
    
    '''
    stack1: list
    stack2: list
    '''
    if not stack2:
        if not stack1:
            return -1
            
        while stack1:
            r=stack1.pop()
            stack2.append(r)
    
        k=stack2.pop()
    
        while stack2:
            l=stack2.pop()
            stack1.append(l)
        return k
    return -1