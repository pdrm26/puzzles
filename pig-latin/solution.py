def pig_latin(sentence: str) -> str:
    output = []

    for word in sentence.split():
        if word[0] in "aeiou":
            output.append(word + "way")
        else:
            output.append(word[1:] + word[:1] + "ay")

    return " ".join(output)


if __name__ == "__main__":
    print(pig_latin("air"))
    print(pig_latin("eat"))
    print(pig_latin("python"))
    print(pig_latin("computer"))
    print(pig_latin("this is a test translation"))
