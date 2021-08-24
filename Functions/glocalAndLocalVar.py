x = 6
print('Global X →',x)


def example() :
    z = 7
    print('Local Z →',z)
    
example()
# print(z) → in this case the variable x is local, so we can't call globally.

def example2() :
    z2 = 7
    print('Local Z2 →',z2)
    print('Inside Function → Local X →',x) # Cause we call the X variable inside the function, we cannot change the value if we work in the function.
    
    # x += 1
    #print(x) # UnboundLocalError: local variable 'x' referenced before assignment.
    y = x + 1
    print('We create a new variable and use the X value →',y)
    # Here we can use the X and change the value of Y
    return y # Doing this is the BEST practice, and then we can use this value settint it to the X value ↓.
    
example2()
x = example2()
print(x) # And here we can just print X because we set the return of Y, and assign the value of X equal to the example2().
# print(z2) → is local, so we can't call globally.

def example3():
    global x # Here we 'alloud' the global function to be work like local, but is the not the best practice at all.
    x += 1
    print('Redefing x:',x)
    
example3()