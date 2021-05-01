#!/usr/bin/env python3
import math
import sympy

def decrypt(n,e,c):
    arr = []
    arr1 = []
    
    def print_factors(x):
        for i in range(1, x + 1):
            if x % i == 0:
                arr.append(i)
                

    print_factors(n)
    #finding the phi, p = (p-1), q = (q-1)
    for i in range(len(arr) - 1):
        p = (arr[i]-1)
        q = (arr[i+1]-1)
        if(math.gcd(e,p*q) == 1):
            phi = p*q   
            break
       
    #finding the private key
    d = sympy.mod_inverse(e, phi)
    print(d)

    #decrypting two letters at a time  
    firstarr = ""
    secarr = ""
    dearr = []
    message = ""    
    for i in range(len(c)):
        firstarr = ""
        secarr = ""
        for j in range(len(c[i])-4):
            firstarr +=c[i][j]

        for j in range(len(c[i])-4, len(c[i])):
            secarr+=c[i][j]

        dearr.append(firstarr)
        dearr.append(secarr)

    intarr = []
    for k in range(len(dearr)):
        intarr.append(int(dearr[k]))

    for i in range(len(intarr)):
        m = math.ceil((pow(intarr[i],d))%n)
        message += chr(m)

    return message


n = 1271
e = 11
c = ['01961246']
print(decrypt(n,e,c))

#[n, e, [ciphertext array]]
# if(m>26):
#     print(list(str(m)))
#     final = list(str(m))
#     message = ""
#     for i in range(len(final)):
#         message += chr(int(final[i])+64)
#     print(message)
# else:
#     print(chr(m+64))

# d = (1/e)%phi
# print(d)

# m = math.ceil((pow(c,d))%n)
# print(m)