def example() :
    return 15, 19, 23

a, b, c = example()

print(a)
print(b)
print(c)

x = [6, 2, 3, 7, 8, 9, 4, 3, 7]  #list

print(x)
print(x[5])
x.append(5) # add on the last position in the list
print(x)
x.insert(5, 1) # add the number 1 at the position 5th in the list
print(x)
x.remove(7) # remove the first element match. Do not remove all equals
print(x)
print(x.index(8)) # index of
print(x.count(3)) # how many in the list
x.remove(3)
x.sort() # order
print(x)
x.reverse() # reverse the order of the list
print(x)
