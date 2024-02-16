def atbash_cipher(text):
    # Definir el alfabeto normal y el invertido
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    reverse_alphabet = alphabet[::-1]
    
    # Diccionario para cifrar y descifrar
    atbash_dict = {alphabet[i]: reverse_alphabet[i] for i in range(len(alphabet))}
    atbash_dict.update({alphabet[i].lower(): reverse_alphabet[i].lower() for i in range(len(alphabet))})

    # Traducir el texto
    result = ''
    for char in text:
        if char in atbash_dict:
            result += atbash_dict[char]
        else:
            result += char

    return result

# Prueba del método Atbash
text = "PAQUITO"
ciphered = atbash_cipher(text)
print("Texto cifrado:", ciphered)
# Dado que Atbash es simétrico, aplicarlo de nuevo descifrará el mensaje
deciphered = atbash_cipher(ciphered)
print("Texto descifrado:", deciphered)
