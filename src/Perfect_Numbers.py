IN=int(input('Enter your number:'))
i=0
s=0
while i<(IN-1):
    i+=1
    f=IN%i
    if f==0:
        s=s+i
if s==IN:
    print(s,"That's it")
else:
    print(s,"Nope")