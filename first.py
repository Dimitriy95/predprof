f = open('space.txt')
k=0
for s in f:
    a = [x for x in s.split('*')]
    k+=1
    if k>1:
        n=int(((a[0].split('-'))[-1])[0])
        m=int(((a[0].split('-'))[-1])[1])
        t = int(len(a[1]))
        xd = int((a[-1].split(' '))[0])
        yd = int((a[-1].split(' '))[-1])

        h = [n,m,t,xd,yd]
        j=[(a[-2].split(' '))[0],(a[-2].split(' '))[-1]]
        
        if int((a[-2].split(' '))[0])==0 and int((a[-2].split(' '))[-1])==0:
            if n>5:
                j[0] = str(n + xd)

            if n<=5:
                j[0] = str(-1*(n+xd)*4 + t)

            if m>3:
                j[-1] =str(m + t +yd)

            if m<=3:
                j[-1] = str(-1*(m+yd)*m)

        r = (a[0]+'*'+a[1]+'*' +(str(j[0]) +' ' +str(j[-1]))+'*'+a[3])
        #print(r)

        if ((a[0].split('-'))[0])[-1]=='V':
            print('<'+a[0]+'> - (<' + str(xd) + '>, <' + str(yd) + '>)')

