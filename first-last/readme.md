# Exercise 9: First-last

For many programmers coming from a background in Java or C#, the dynamic nature of Python is quite strange. How can a programming language fail to police which type can be assigned to which variable? Fans of dynamic languages, such as Python, respond that this allows us to write generic functions that handle many different types.

Indeed, we need to do so. In many languages, you can define a function multiple times, as long as each definition has different parameters. In Python, you can only define a function once—or, more precisely, defining a function a second time will overwrite the first definition—so we need to use other techniques to work with different types of inputs.

In Python, you can write a single function that works with many types, rather than many nearly identical functions, each for a specific type. Such functions demonstrate the elegance and power of dynamic typing.

The fact that sequences—strings, lists, and tuples—all implement many of the same APIs is not an accident. Python encourages us to write generic functions that can apply to all of them. For example, all three sequence types can be searched with `in`, can return individual elements with an index, and can return multiple elements with a slice.

## Task

We’ll practice these ideas with this exercise. Write a function called `firstlast` that takes a sequence (string, list, or tuple) and returns the first and last elements of that sequence in a two-element sequence of the same type. 

### Examples

- `firstlast('abc')` will return `'ac'`.
- `firstlast([1, 2, 3, 4])` will return `[1, 4]`.
- `firstlast((10, 20, 30))` will return `(10, 30)`.

## Notes

- Ensure your function handles edge cases such as empty sequences and single-element sequences.
- This exercise helps reinforce the concept of dynamic typing and generic programming in Python.
