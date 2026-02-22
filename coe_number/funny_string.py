def funnyString(s):
    reverse = [ord(letter) for letter in reversed(s)]
    original = [ord(letter) for letter in s]

    r = [abs(reverse[i] - reverse[i + 1]) for i in range(len(reverse) - 1)]
    o = [abs(original[i] - original[i + 1]) for i in range(len(original) - 1)]

    if r == o:
        return "Funny"
    return "Not Funny"


if __name__ == "__main__":
    q = int(input())
    for _ in range(q):
        s = input().strip()
        print(funnyString(s))