def mysum(*args):
    if not args:
        return args

    result = args[0]
    for i in args[1:]:
        result += i

    return result


if __name__ == "__main__":
    print(mysum())
    print(mysum(1, 2, 3, 4))
    print(mysum("hey", "woow"))
    print(mysum(["a", "b", "c"], ["woow", "list", "imagine"]))
    print(mysum(("a", "b", "c"), ("aa", "bb", "cc")))
