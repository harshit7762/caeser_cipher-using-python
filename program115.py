#caeser cipher algorithim
def caeser_cipher(message,key):
    result=""
    for char in message:
        if char.isalpha():
            if char.isupper():
                result+=chr((ord(char)-65+key)%26+65)
            else:
                result+=chr((ord(char)-97+key)%26+97)
        else:
            result+=char
    return result
        
a=input("Enter a message to be decrypted:")
key=int(input("Enter the the key to be used in the caeser cipher:"))
enc=caeser_cipher(a,key)
print("Encrypted Message:",enc)
dec=caeser_cipher(enc,-key)
print("Decrypted Message:",dec)