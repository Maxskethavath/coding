g=list(input("guest name"))
al=len(g)
h=list(input("host name"))
bl=len(h)
p=list(input("piles"))
cl=len(p)
def no_of(a,al,b,bl,c,cl):
    d={}
    k=[int(al),int(bl),int(cl)]
    for i in range(3):

        for j in range(k[i]):
            if (i==0):
                if a[j] in d.keys():
                    # do notheing
                    d[a[j]]+=1
                else:
                    d[a[j]]=1
            elif (i==1):
                 if b[j] in d.keys():
                    # do notheing
                    d[b[j]]+=1
                 else:
                    d[b[j]]=1
            else:
                if c[j] in d.keys():
                    # do notheing
                    d[c[j]]-=1
                else:
                    d[c[j]]=1
    return d
if (al+bl==cl):
    D=no_of(g,al,h,bl,p,cl)
    flag = all(value == 0 for value in D.values())
    print(flag)
else:
    print(False)
    


    
