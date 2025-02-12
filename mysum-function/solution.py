def my_sum(*args: int) -> bool:
    sum = 0
    for i in args:
        if isinstance(i, int) or isinstance(i, float):
            sum += i
        else:
            raise ValueError("Only int or float are acceptable")

    return sum


if __name__ == "__main__":
    s = my_sum()
    print(s)
