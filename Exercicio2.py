from unittest import result


def CriptografiaCesar(text,s):
    result = ""
    
    for i in range(len(text)):
        char = text[i]
        
        #Criptografa caracteres maiúsculos
        if(char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
            
        #Criptografar caracteres minúsculos
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result

text = "ATTACKATTONCE"
s = 4
print("Text: " + text)
print("Shift: " + str(s))
print("Cipher: " + CriptografiaCesar(text,s))