def encrypt(message):
    encrypted = ""
    global char
    
    for char in message:
        encrypted += "💀"

    return encrypted

print(encrypt("test"))