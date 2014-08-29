def is_palindrome(x):
    x = str(x)
    string_len = len(x)
    for i in range(0,int(string_len/2)):
        if x[i] != x[string_len-1-i]:
            return False
    return True

A=[0,0,0]
for i in range(100,1000):
    for j in range(100,1000):
        if is_palindrome(i*j) == True:
            if A[0]<i*j:
                A[0]=i*j
                A[1]=i
                A[2]=j
print A