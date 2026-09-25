def encrypt(message):
    encrypted = ""

    for char in message:
        encrypted += format(ord(char), "08b")

    return encrypted