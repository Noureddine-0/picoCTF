from Crypto.Util.number import * 

## the gcdExtended function is copied from GeeksforGeeeks and u must at least know that it exist.

def gcdExtended(a, b):

    if a == 0:
        return b, 0, 1
 
    gcd, x1, y1 = gcdExtended(b % a, a)
 

    x = y1 - (b//a) * x1
    y = x1
 
    return gcd ,x ,y

def get_d(phi,e):
    number=gcdExtended(phi,e)[2]
    if number<0:
        return number +phi
    else:
        return number

e=65537
n=1584586296183412107468474423529992275940096154074798537916936609523894209759157543
c=964354128913912393938480857590969826308054462950561875638492039363373779803642185
phi=(650809615742055581459820253356987396346062)*(2434792384523484381583634042478415057960) # You can find p and q in factordb.com
d=get_d(phi,e)                                                                              # or in termainal by using factordb
m=pow(c,d,n)
print(long_to_bytes(m).decode('ascii'))
