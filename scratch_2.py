alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction=='encode':
    def encrypt(t,s):
        cipher=" "
        for letter in text:
            position=alphabet.index(letter)
            n_position=position + s
            n_letter = alphabet[n_position]
            cipher+= n_letter
        print(f"encode text is {cipher}")

    encrypt(t=text,s=shift)
else:
    def decrypt(t,s):
        cipher=" "
        for letter in text:
            position=alphabet.index(letter)
            n_position=position-s
            n_letter=alphabet[n_position]
            cipher+=n_letter
        print(f"decode text is {cipher}")
    decrypt(t=text,s=shift)