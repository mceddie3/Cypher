
def cypher(text_input, displacement: int):
    line = ""
    for letter in text_input:
        line += chr((((ord(letter) + displacement) - 97) % 26) + 97)
    return line
