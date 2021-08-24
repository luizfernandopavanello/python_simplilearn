def example():
    x = 9
    y = 9
    print( x + y)

    if x < y:
        print('x < y →', x + y)
    elif x > y:
        print('x > y →', y - x)
    elif x == y:
        print('x == y →', x * y)
    else:
        print('else →',x / y)

def main():
    example()

main()