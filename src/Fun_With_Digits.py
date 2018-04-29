c=('','+','-')
n=['1']
for i in range(2,9):
    for p in range(len(n)):
        for l in c:
            n.append(n[p]+l+str(i))
for i in n:
    if eval(i)==578:
        print(i)