def hext_output(string_number: str) -> int:
    decnum = 0

    # I use reversed instead of slicing string_number[::-1] because reversed returns an iterator which consumes less memory rather than slicing that creates a new string
    for power, digit in enumerate(reversed(string_number)):
        decnum += pow(16, power) * int(digit, 16)

    return decnum


if __name__ == "__main__":
    hext_output("50")
    hext_output("8cf")
