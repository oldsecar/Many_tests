import random as rd
i=0
box={}
while i<100:
    box[i]=rd.randint(10,20)
    i+=1
b=rd.randint(0,99)
box[b]=rd.randint(0,10) or rd.randint(20,30)
for i in box:
    if box[i]>20 or box[i]<10:
        print('The black box is box',i)