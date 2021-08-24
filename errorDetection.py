# Commons Errors:

# NameError:
# varaible = 55
#print(variable) # → NameError: name 'variable' is not defined / The word is spelling wrong.

'''
# IndentationError: expected an indented block (Syntax Error)
def func1() :
    We define of the function but never write any code...
    So, we cannot keep going with the next one
    
def func2():
    print(2)
    
# # →   line 8
#     def func2():
#     ^
We could use the func2 as a child of func1 with the right indentantion
'''
'''
IndentationError: unexpected indent:

def task():
    print('1') # When we change the indentation, python understand we gonna start a new command, a new function... Indentation is very import!
print('2')
    print('3')
    
task()
'''
'''
#SyntaxError: EOL while scanning string literal → 'open and close'
print('Hey there...
print('Hey there)
'''
'''
#SyntaxError: unexpected EOF while parsing → (open and close)
print('Hey there...'

print(
    ...

If we don't close the parentheses we gonna have an indentation...
'''
