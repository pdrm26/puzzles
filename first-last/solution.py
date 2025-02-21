def firstlast(input: str | list | tuple) -> str | list | tuple:
    if not len(input) or len(input) == 1:
        return input

    # BAD WAY
    # if isinstance(input, str):
    #     return input[0] + input[-1]
    # elif isinstance(input, list):
    #     return [input[0], input[-1]]
    # elif isinstance(input, tuple):
    #     return (input[0], input[-1])

    return input[:1] + input[-1:]
