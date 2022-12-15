alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

lol='yes'
while lol=='yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encoded=[]
    decoded=[]

    def caesar(texts,shift,direction):
        if direction=='encode':
            array = list(texts)
            for i in array:
                if i in alphabet:
                    enc = alphabet.index(i) + shift
                    if enc > 25:
                        enc=enc%26
                        encoded.append(alphabet[enc])
                    else:
                        encoded.append(alphabet[enc])
                else:
                    encoded.append(i)
            encoded_up = ''.join(encoded)
            print(f"The encoded text is:{encoded_up}")

        elif direction=='decode':
            array = list(texts)
            for i in array:
                if i in alphabet:
                    dec = alphabet.index(i) - shift
                    if dec < 0:
                        dec=dec%26
                        decoded.append(alphabet[dec])
                    else:
                        decoded.append(alphabet[dec])
                else:
                    decoded.append(i)
            decoded_up = ''.join(decoded)
            print(f"The decoded text is:{decoded_up}")
    caesar(text,shift,direction)

    lol=input("Do you want to continue?(Enter any key to exit)\n")





