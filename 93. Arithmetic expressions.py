from itertools import product
from operator import itemgetter
from time import clock

def op(a,b,i):
    if i==1:
        return(a+b);
    elif i==2:
        return(a-b);
    elif i==3:
        return(a*b);
    elif i==4:
        if b!=0:
            return(a/b);
        else:
            return "no"

def create_array(a,b,c,d):
    a=float(a)
    b=float(b)
    c=float(c)
    d=float(d)
    A=[a,b,c,d]
    B=[]
    for i,j,k in product(range(1,5),range(1,5),range(1,5)):
        for x,y,z,w in product(A,A,A,A):
            if x!=y and x!=z and x!=w and y!=z and y!=w and z!=w:
                a1=op(op(op(x,y,i),z,j),w,k)
                if op(op(x,y,i),op(z,w,j),k)!="no":
                    a2=op(op(x,y,i),op(z,w,j),k)
                if op(x,op(y,op(z,w,i),j),k)!="no":
                    a3=op(x,op(y,op(z,w,i),j),k)
                if op(x,op(op(y,z,i),w,j),k)!="no":
                    a4=op(x,op(op(y,z,i),w,j),k)
                a5=op(op(x,op(y,z,i),j),w,k)
                if a1>0 and a1%1==0:
                    B.append(a)
                if a2>0 and a2%1==0:
                    B.append(a2)
                if a3>0 and a3%1==0:
                    B.append(a3)
                if a4>0 and a4%1==0:
                    B.append(a4)
                if a5>0 and a5%1==0:
                    B.append(a5)
    C=[[a,b,c,d],sorted(set(B))]
    return C

def get_largest(array):
    check=True
    i=0
    while check and i<len(array[1])-1:
        if array[1][i]!=array[1][i+1]-1:
            check=False
            return [array[0],i+1]
        i+=1

start=clock()
X=[]
for x,y,z,w in product(range(1,10),range(1,10),range(1,10),range(1,10)):
    if x<y and y<z and z<w:
        X.append(get_largest(create_array(x,y,z,w)))

X=sorted(X, key=itemgetter(1))
print str(int(X[len(X)-1][0][0]))+str(int(X[len(X)-1][0][1]))+str(int(X[len(X)-1][0][2]))+str(int(X[len(X)-1][0][3]))
print clock()-start