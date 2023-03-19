alphabet = "abcdefghijklmnopqrstuvwxyz"
key = "zyxwvutsrqponmlkjihgfedcba"
text = "ulfa nur rohma"

result = ""
for letter in text:
    if letter.lower() in alphabet:
        result += key[alphabet.find(letter.lower())]
    else:
        result += letter

print(text)
print(result)
