import random, sympy, string, math

def encrypt(alpha):
    rand = random.randint(20,30)
    p = sympy.prevprime(rand)
    q = sympy.nextprime(rand)

    n = p*q
    phi = (p-1)*(q-1)

    #finding small e exponent that is not a factor of n and is less than phi
    i = 0
    e = 2
    while (e < phi):
        if (math.gcd(e, phi) == 1):
            break
        else:
            e+=1

    #print('n, phi, e', n, phi, e) #n and e are public keys

    concatNum = []
    for i in alpha:
        value = ord(i)
        value = value**e
        c = value%n
        concatNum.append(c)
    #print(concatNum)

    return [n, e, concatNum]
    

def main():
    #take input
    alpha = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam sed nulla orci. Donec dignissim magna bibendum libero viverra, in facilisis eros luctus. Vestibulum pulvinar augue et elementum sollicitudin. Mauris cursus feugiat varius. Proin tincidunt ligula nec elit semper, in maximus est semper. Sed commodo mauris ante, et fringilla est pellentesque ut. Vivamus quis dapibus eros. Cras luctus ultricies ipsum, semper pharetra arcu accumsan in. Donec a dui nisl. Donec posuere mauris nulla, vitae blandit arcu vestibulum ut." #input
    #alpha = input("Enter message: ")

    print(encrypt(alpha)) #gives [n, e, [ciphertext numbers]]

if __name__=="__main__":
    main()
