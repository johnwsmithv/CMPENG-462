import random, sympy, math

#function for determining public keys
def getPublicK(alpha):
    rand = random.randint(20,30)
    p = sympy.prevprime(rand)
    q = sympy.nextprime(rand)

    n = p*q
    phi = (p-1)*(q-1)

    e = 2
    while (e < phi):
        if (math.gcd(e, phi) == 1):
            break
        else:
            e+=1

    #print('n, phi, e', n, phi, e) #n and e are public keys
    return [n, e]
    
def encrypt(alpha):
    n, e = getPublicK(alpha) #getting public keys
    
    #doing the actual encryption of each letter using ascii value, e, and n values
    concatNum = []
    for i in alpha:
        value = ord(i)
        value = value**e
        c = value%n
        app = str(c).zfill(3) #filling each number with leading 0's
        concatNum.append(app) #each value is string of length 3


    #print(concatNum)

    #combining 2 letters at a time = each value in finalConcat is a string of length 6
    finalConcat = []
    j = 0
    while j < len(concatNum):
        if j+1 < len(concatNum):
            finalConcat.append(concatNum[j]+concatNum[j+1])

        j+=2
        
    if len(concatNum) % 2 != 0:
        app2 = concatNum[len(concatNum)-1]+'000'
        finalConcat.append(app2)
        
    #print(finalConcat)
    return [n, e, finalConcat]
    

def main():
    alpha = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam sed nulla orci. Donec dignissim magna bibendum libero viverra, in facilisis eros luctus. Vestibulum pulvinar augue et elementum sollicitudin. Mauris cursus feugiat varius. Proin tincidunt ligula nec elit semper, in maximus est semper. Sed commodo mauris ante, et fringilla est pellentesque ut. Vivamus quis dapibus eros. Cras luctus ultricies ipsum, semper pharetra arcu accumsan in. Donec a dui nisl. Donec posuere mauris nulla, vitae blandit arcu vestibulum ut." #input
    #alpha = input("Enter message: ")

    print(encrypt(alpha)) #gives [n, e, [ciphertext numbers]]

if __name__=="__main__":
    main()
