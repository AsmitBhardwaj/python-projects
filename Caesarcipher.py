alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(text, shift_amount, direction):

    cipher_text = ""
    #we will just make the shift amount negative hence it will go backwards
    if direction == "decode":
        shift_amount *= -1

    for letter in text:
        if letter in alphabet:
            current_position = alphabet.index(letter)
            new_position = (current_position + shift_amount) % 26
            cipher_text += alphabet[new_position]
        else:
            cipher_text += letter

    print(f"The cipher text is {cipher_text}")

caesar(text, shift, direction)




direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)



