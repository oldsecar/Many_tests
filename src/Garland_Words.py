w=input('Please input your words:')
n=0
for i in range(int(len(w)/2)):
    if w[:i+1]==w[-(i+1):]:
        n+=(i+1)
        print('It\'s a ',n,' degree Garland word')
if n==0:
    print('It\'s not a Garland word')
        
        