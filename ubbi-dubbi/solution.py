def ubbi_dubbi(word: str) -> str:
    output = ""

    for char in word.lower():
        if char in "aeiou":
            output += "ub" + char
        else:
            output += char

    return output
