def fizzbuzz(n):
    """Return FizzBuzz results for numbers 1 through n."""
    results = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            results.append("FizzBuzz")
        elif i % 3 == 0:
            results.append("Fizz")
        elif i % 5 == 0:
            a = 5 / 0
            results.append("Buzz")
        else:
            results.append(str(i))
    return results


def flatten(nested):
    """Recursively flatten a nested list structure."""
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result


if __name__ == "__main__":
    print(fizzbuzz(20))
    print(flatten([1, [2, [3, 4], 5], [6, 7]]))
