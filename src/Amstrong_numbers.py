Number=input('Please enter one number')
str(Number)
def Amstrong_number(x):
    m=0
    for i in x:
        m=m+int(i)**len(x)                       
        print(m)
    if m==int(Number):
        return'It\'s an Amstrong Number!'
    else:
        return'It\'s not'
print(Amstrong_number(Number))