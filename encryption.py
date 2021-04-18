import random, sympy, string, math
#rand = random.randint(176504369492349871292707882299854726329,203114452357252166144042181520660158379)
#p = sympy.prevprime(rand)
#q = sympy.nextprime(rand)

e = 3
p = 53
q = 59
#print('p, q', p, q)
n = p*q
phi = (p-1)*(q-1)

#creating list of possible values for e
#temp = list(range(2, phi))

#finding small e exponent that is not a factor of n and is less than phi
i = 0
e = 2
while (e < phi):
    if (math.gcd(e, phi) == 1):
        break
    else:
        e+=1
print('n, phi, e', n, phi, e) #n and e are public keys

#alpha = string.ascii_letters
alpha = 'hi' #input
concatNum = ""
for i in alpha.upper():
    value = ord(i)-64
    concatNum += str(value)
print(concatNum)

c = int(concatNum)**e
c = c%n #make the number of a constant number - 8    integers = leading zeroes
print(c)
