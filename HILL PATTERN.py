h=int(input())
l=int(input())
strlen=h*(l*2)
nostr=h
strs=[]
for i in range(nostr):
    x=[]
    for j in range(strlen):
        y=" "
        x.append(y)
    strs.append(x)
j=-1
char=64

for i in range(strlen):
    char+=1
    if(char>90):
        char=65
    if(j>=-1 and j<(h-1)):
        j+=1
        x=len(strs)
        y=j%x
        strs[y][i]=chr(char)
        if(j==(h-1)):
            k=h
        continue
    elif(j>=(h-1) and k!=0):
        k-=1
        x=len(strs)
        y=k&x
        strs[k][i]=chr(char)
        if(k==0):
            j=-1
        continue
    
for i in range(len(strs)-1,-1,-1):
    for j in range(strlen):
        print(strs[i][j],end='')
    print()
    
       
       
