try:
    t=int(input())
    a=[]
    a.append(0)
    a.append(1)
    while(t):
        l,r=map(int,input().split())
        count=0
        if(r+1>len(a)):
            for i in range(len(a),r+1):
                y=1+a[i-a[a[i-1]]]
                a.append(y)
        for i in range(l,r+1):
            count+=a[i]**2
        print(count)
        
        
        t-=1
except:
    pass
