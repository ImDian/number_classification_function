numbers = list(map(int, input().split(", ")))


def classification(a: list):
    positive = []
    negative = []
    even = []
    odd = []

    for number in a:
        if number >= 0:
            positive.append(number)
        elif number < 0:
            negative.append(number)
        if number % 2 == 0:
            even.append(number)
        else:
            odd.append(number)

    return (f"Positive: {', '.join(map(str, positive))}\nNegative: {', '.join(map(str, negative))}\n"
          f"Even: {', '.join(map(str, even))}\nOdd: {', '.join(map(str, odd))}")


print(classification(numbers))