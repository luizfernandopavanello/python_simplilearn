x = 2
y = 7
z = 10

if x > y:
    print(x, 'is greater than', y)
if x < y:
    print(x, 'is less than', y)
if x != y & y != z:
    print(True)

#cannot do this → TypeError: '<' not supported between instances of 'int' and 'str'
# if x < '2':
#     print(x)

if z > y > x :
    print('True again')