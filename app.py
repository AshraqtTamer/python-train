
word = input()

if len(word) <= 10:
    print(word)


elif len(word) > 10:

    middle = int(len(word) - 2)
    first = word[0]
    last = word[-1]
    print(f"{first}{middle}{last}")







