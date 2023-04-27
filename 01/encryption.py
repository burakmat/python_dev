alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
def encrypt(text, shift):
  ptext=""
  encalp=alphabet.copy()
  for i in range(0,26):
    if shift+i>25:
      encalp[i]=alphabet[i+shift-26]
    else:
      encalp[i]=alphabet[i+shift]
  for letter in text:
    ptext+=encalp[alphabet.index(letter)]
  print(ptext)
encrypt(text, shift)


def decrypt(text, shift_amount):
    cipher_text = ""
    for letter in text:
        alphabet.reverse()
        position = alphabet.index(letter)
        new_position = position + shift_amount

        cipher_text += alphabet[new_position]
        alphabet.reverse()
    print(f"The decoded text is {cipher_text}")

if direction.lower()=="encode":
  encrypt(text, shift)
elif direction.lower()=="decode":
  decrypt(text,shift)