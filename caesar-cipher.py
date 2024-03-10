#ord() returns the number representing the unicode code of a specified character.

def caesar_encode(plain_text, shift_number):
    text_ascii = []
    shift_text_ascii = []
    encode_message = ''
    
    for characters in plain_text:
        text_ascii.append(ord(characters))
        
    while shift_number > 25:
        shift_number = shift_number - 26
        
    for character_unicode in text_ascii:
        if character_unicode < 97:
            character_unicode = character_unicode + 0
        else:
            character_unicode = character_unicode + shift_number
        
        while character_unicode > 122:
            character_unicode = character_unicode - 26
            
        shift_text_ascii.append(chr(character_unicode))
        
    for item in shift_text_ascii:
        encode_message += str(item) 
    print(f"The encoded message is: {encode_message}")
        
def caesar_decode(secret_text, shift_number):
    plain_text = []
    decode_message = ''
    for characters in secret_text:
        if ord(characters) < 97:
            characters_unicode = characters
            plain_text.append((characters_unicode))
            
        else:
            characters_unicode = ord(characters) - shift_number
            if characters_unicode < 97:
                characters_unicode = characters_unicode + 26
            plain_text.append(chr(characters_unicode))
    
    for item in plain_text:
        decode_message += str(item)
    print(f"The decoded message is: {decode_message}")
        

    

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
message = input("Type your message:\n").lower()
shift_number = int(input("Type the shift number:\n"))

if direction == "encode":
    caesar_encode(message, shift_number)
elif direction == "decode":
    caesar_decode(message, shift_number)
else:
    print("Please choose a correct direction!")