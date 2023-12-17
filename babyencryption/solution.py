# 0 - 32 are control characters which we dont expect to find in flag 
def findLetter(char):
    for val in range(33,126):
        if ((123 * val + 18) % 256) == char:
            return chr(val)
    return "" 

def decryption(cmsg):
    return map(findLetter,cmsg)

if __name__ == "__main__":
    with open("./msg.enc", 'r') as f:
        cypherText = bytes.fromhex(f.read())    
        print("".join(list(decryption(cypherText))))
