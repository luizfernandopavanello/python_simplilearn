def addition (num1, num2) :
    answer = num1 + num2
    return answer

x = addition(5, 6)
print ('The Addition:', x)

def website(font='TRT', 
            background_color='white', 
            fontsize='12', 
            font_color='black'):
    
    print('font:',font)
    print('bg:',background_color)
    print('Font Size:',fontsize)
    print('font Color:',font_color)

print('→ Default values: ')    
website() # default values
print ('→ New values: ')
website(background_color='Grey') # changed just the bg

# website('white', '12', 'black')
# the order matters
# is a great practice define default values, so if we forget any value, we do not have a problem 