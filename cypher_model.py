# Encoding Function using Vignere Cypher

def vigEncode(PlainText, Key):
    cipherText = []
    PlainText = PlainText.replace(" ", "")
    PlainText = PlainText.upper()
    superkey = []
    Key = Key.upper()
    for i in range(0, len(PlainText)):
        superkey.append(Key[i % len(Key)])
    
    print(superkey)
    for j in range(0, len(PlainText)):
        x = (ord(PlainText[j]) +
             ord(superkey[j])) % 26
        x += ord('A')
        cipherText.append(chr(x))
    return("" . join(cipherText))

# Decoding Function using Vignere Cypher
def vigDecode(CypherText, Key):
    plainText = []
    superkey = []
    Key = Key.upper()

    for i in range(0, len(CypherText)):
        superkey.append(Key[i % len(Key)])
        
    for j in range(len(CypherText)):
        x = (ord(CypherText[j]) -
             ord(superkey[j]) + 26) % 26
        x += ord('A')
        plainText.append(chr(x))

    return("" . join(plainText))

# Encoding Function using Vignere Cypher ASCII
def vigASCIIEncode(PlainText, Key):
    cipherText = []
    PlainText = PlainText.replace(" ", "")
    PlainText = PlainText.upper()
    superkey = []
    Key = Key.upper()

    for i in range(0, len(PlainText)):
        superkey.append(Key[i % len(Key)])
    for j in range(0, len(PlainText)):
        x = (ord(PlainText[j]) +
             ord(superkey[j])) % 256
        cipherText.append(chr(x))
    
    return("" . join(cipherText))

# Decoding Function using Vignere Cypher ASCII
def vigASCIIDecode(CypherText, Key):
    plainText = []
    superkey = []
    Key = Key.upper()

    for i in range(0, len(CypherText)):
        superkey.append(Key[i % len(Key)])
        
    for j in range(len(CypherText)):
        x = (ord(CypherText[j]) -
             ord(superkey[j]) + 256) % 256
        
        plainText.append(chr(x))
    return("" . join(plainText))
