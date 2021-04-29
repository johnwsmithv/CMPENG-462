import random, sympy, math

#function for determining public keys
def getPublicK(alpha):
    rand = random.randint(20,30)
    p = 31
    q = 41
    #p = sympy.prevprime(rand)
    #q = sympy.nextprime(rand)

    n = p*q #n = 1271
    phi = (p-1)*(q-1)

    e = 2
    while (e < phi):
        if (math.gcd(e, phi) == 1):
            break
        else:
            e+=1

    #print('n, phi, e', n, phi, e) #n and e are public keys
    return [n, 11]
    
def encrypt(alpha):
    n, e = getPublicK(alpha) #getting public keys
    
    #doing the actual encryption of each letter using ascii value, e, and n values
    concatNum = []
    for i in alpha:
        value = ord(i)
        #print(value)
        value = value**e
        c = value%n
        #print(c)
        app = str(c).zfill(4) #filling each number with leading 0's
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
    #input
    alpha = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam non massa nulla. Donec at odio tortor. Curabitur porta, nisl id imperdiet sollicitudin, lectus ante consectetur magna, nec facilisis magna magna quis sapien. Integer faucibus, nulla quis sagittis bibendum, erat dui condimentum magna, et congue eros sapien vitae lectus. Phasellus non sapien sed justo consectetur sodales. Lorem ipsum dolor sit amet, consectetur adipiscing elit. In hac habitasse platea dictumst. Curabitur dignissim accumsan aliquet. Nunc malesuada erat a erat venenatis venenatis. Aliquam et quam malesuada, vulputate sapien in, tristique lorem. Proin imperdiet sodales consectetur."
    #alpha = input("Enter message: ")

    print(encrypt(alpha)) #gives [n, e, [ciphertext numbers]]

if __name__=="__main__":
    main()
