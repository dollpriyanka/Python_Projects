def vowel(char):
    if char.lower() in "aeiou":
        return True
    else:
        return False

chars = ["A","s","S","e","a"]
print(list(filter(vowel,chars)))