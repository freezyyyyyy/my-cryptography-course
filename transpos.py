import math

def main():
    print("")
    j = 0
    while j < 2:
        message = input("Enter a message : ")
        pkey = int(input("enter a key : "))
        encrypted = encryptTxt(pkey, message)
        encryptstr = ''.join(encrypted)
        decrypted = decryptTxt(pkey, encryptstr)
        for i in encrypted:
            print('|'+i+'|')
        print('|'+encryptstr+'|')
        print(decrypted)
        print("\n")
        j += 1

def encryptTxt(key, text):
    ciphertxt = ['']*key

    for column in range(key):
        pointer = column # make next column when pointer exceeds the plaintext lenght

        while pointer < len(text):
            ciphertxt[column] += text[pointer]
            pointer += key
    return ciphertxt

def decryptTxt(key, cipher):
    colNum = int(math.ceil(len(cipher)/ float(key)))
    rowNum = key
    shBoxes = (colNum*rowNum) - len(cipher)
    decrypted = ['']*colNum
    column = 0
    row = 0
    for symbol in cipher:
        decrypted[column] += symbol
        column+=1
        if(column == colNum) or (column == colNum - 1 and row >= rowNum-shBoxes):
            column = 0
            row+=1
    return ''.join(decrypted)

if __name__ == '__main__':
    main()