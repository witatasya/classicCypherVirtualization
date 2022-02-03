

def matrix(x,y,initial):
    return [[initial for i in range(x)] for j in range(y)]
    
def generateKeyMatrix(key):
    key=key.replace(" ", "")
    key=key.upper()
    result=list()

    for c in key: #storing key
        if c not in result:
            if c=='J':
                result.append('I')
            else:
                result.append(c)
    flag=0

    #generate alphabet
    # 65 = A in ASCII order
    for i in range(65,91): 
        if chr(i) not in result:
            if i==73 and chr(74) not in result:
                result.append("I")
                flag=1
            elif flag==0 and i==73 or i==74:
                pass    
            else:
                result.append(chr(i))
    k=0
    # initialize matrix
    my_matrix=[["" for i in range(5)] for j in range(5)]
    # Fill the matrix 
    for i in range(0,5): 
        for j in range(0,5):
            my_matrix[i][j]=result[k]
            k+=1

def locindex(c,matrixKey): #get location of each character
    loc=list()
    if c=='J':
        c='I'
    for i ,j in enumerate(matrixKey):
        for k,l in enumerate(j):
            if c==l:
                loc.append(i)
                loc.append(k)
                return loc
            
def encrypt(PlainText, matrixKey):  #Encryption
    
    PlainText=PlainText.upper()
    PlainText=PlainText.replace(" ", "")
    cipherText = []

    i=0
    for s in range(0,len(PlainText)+1,2):
        if s<len(PlainText)-1:
            if PlainText[s]==PlainText[s+1]:
                PlainText=PlainText[:s+1]+'X'+PlainText[s+1:]
    if len(PlainText)%2!=0:
        PlainText=PlainText[:]+'X'
    
    while i<len(PlainText):
        loc=list()
        loc=locindex(PlainText[i],matrixKey)
        loc1=list()
        loc1=locindex(PlainText[i+1],matrixKey)
        if loc[1]==loc1[1]:
            cipherText.append("{}{}".format(matrixKey[(loc[0]+1)%5][loc[1]],matrixKey[(loc1[0]+1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            cipherText.append("{}{}".format(matrixKey[loc[0]][(loc[1]+1)%5],matrixKey[loc1[0]][(loc1[1]+1)%5]),end=' ')  
        else:
            cipherText.append("{}{}".format(matrixKey[loc[0]][loc1[1]],matrixKey[loc1[0]][loc[1]]),end=' ')    
        i=i+2
    return ("" . join(cipherText))        
                 
def decrypt(CipherText,matrixKey):  #decryption
    
    CipherText  =  CipherText.upper()
    CipherText  =  CipherText.replace(" ", "")
    plainText = []

    i=0
    while i<len(CipherText):
        loc=list()
        loc=locindex(CipherText[i],matrixKey)
        loc1=list()
        loc1=locindex(CipherText[i+1],matrixKey)
        if loc[1]==loc1[1]:
            plainText.append("{}{}".format(matrixKey[(loc[0]-1)%5][loc[1]],matrixKey[(loc1[0]-1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            plainText.append("{}{}".format(matrixKey[loc[0]][(loc[1]-1)%5],matrixKey[loc1[0]][(loc1[1]-1)%5]),end=' ')  
        else:
            plainText.append("{}{}".format(matrixKey[loc[0]][loc1[1]],matrixKey[loc1[0]][loc[1]]),end=' ')    
        i=i+2
    return ("" . join(plainText))            