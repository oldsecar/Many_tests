b=input('Please enter numbers(at least two defferent numbers):')
list(b)
'''if len(b)!=4:
    print("Four numbers!!!")'''
f=0
for k in b:
    i=0
    if b[i]==b[i+1]:
        f+=1
if f>2:
    print('At least two defferent numbers!')
def bigger(x):
    c=list(x)
    g=list(x)
    for i in range(3):
        for i in range(3):
            if c[i]<c[i+1]:
                l=c[i]
                c[i]=c[i+1]
                c[i+1]=l
    for i in range(3):
        for i in range(3):
            if g[i]>g[i+1]:
                l=g[i]
                g[i]=g[i+1]
                g[i+1]=l
    c=''.join(c)
    g=''.join(g)
    p=int(c)-int(g)
    return p
t=bigger(b)
while t!=bigger(str(t)):
    t=bigger(str(t))
print(t)
