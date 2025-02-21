def pig_latin(sentence: str) -> str:
    output = []

    for word in sentence.lower().split():
        if word[0] in "aeiou":
            output.append(word + "way")
        else:
            output.append(word[1:] + word[:1] + "ay")

    return " ".join(output)
