from math import sqrt
def list_divisors(n):
    A=[1]
    if n>3:
        for i in range(2,int(sqrt(n))):
            if n%i==0:
                A.append(i)
                A.append(n/i)
#if the sqare root of n is an integer & it | n then we only add 1
        if int(sqrt(n)) == sqrt(n):
            if n%int(sqrt(n))==0:
                A.append(int(sqrt(n)))
    return A

def array_sum(A):
#just sum all the elements in the array A
    sum=0
    for i in range(0,len(A)):
        sum+=A[i]
    return sum

def amicable(n):
    if n == array_sum(list_divisors(array_sum(list_divisors(n)))) and n!=array_sum(list_divisors(n)):
        return True
    else:
        return False

A=[]
i=6
j=0
final_check=True
while final_check:
    A[j].append(i)
    check=True
    while chek:
        if array_sum(list_divisors(n))==n:
            A[j].append(array_sum(list_divisors(i)))
            i=array_sum(list_divisors(i))