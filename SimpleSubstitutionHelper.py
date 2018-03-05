cipherFilePath = input("Open the ciphertext file: ")

cipherFile = open(cipherFilePath)
ciphertext = cipherFile.read().upper()
plaintext = ''

alphabets = ['A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'U',
    'V',
    'W',
    'X',
    'Y',
    'Z']

key = dict({
    'A': '*',
    'B': '*',
    'C': '*',
    'D': '*',
    'E': '*',
    'F': '*',
    'G': '*',
    'H': '*',
    'I': '*',
    'J': '*',
    'K': '*',
    'L': '*',
    'M': '*',
    'N': '*',
    'O': '*',
    'P': '*',
    'Q': '*',
    'R': '*',
    'S': '*',
    'T': '*',
    'U': '*',
    'V': '*',
    'W': '*',
    'X': '*',
    'Y': '*',
    'Z': '*'
    })

print('\n\n\n\n')


while True:
    for i in range(5):
        for j in range(6):
            if (i * 6 + j) < 26:
                print(alphabets[i * 6 + j] + ' -> ' + key[alphabets[i * 6 + j]] + '\t', end='')
        print()
    print('\n\n\n')

    print("Ciphertext: \n" + ciphertext + "\n\n\n")

    plaintext = ciphertext
    for i in range(len(plaintext)):
        if plaintext[i] in key:
            plaintext = plaintext[:i] + key[plaintext[i]] + plaintext[i + 1:]
    print("Plaintext: \n" + plaintext + "\n\n\n")

    x = input("Modify mapping (Type (X Y enter) to map X in ciphertext to Y in plaintext, type * to print texts): ")
    while x is not '*':
        y = x.split(' ')
        if y[0].isalpha() and (y[1].isalpha() or y[1] is '*'):
            y[0] = y[0].upper()
            if y[1].isalpha():
                y[1] = y[1].upper()
            key[y[0]] = y[1]
        x = input("Modify mapping ([A-Z A-Z], * means skip): ")
    print('\n\n\n\n')