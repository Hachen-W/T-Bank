def process(s, l, r):
    left = s[:l - 1]
    middle = s[l - 1:r]
    right = s[r:]

    doubled_middle = ''.join(symbol * 2 for symbol in middle)

    return left + doubled_middle + right


def main():
    n, q = map(int, input().split())
    s = input().strip()

    answers = []

    for _ in range(q):
        query = list(map(int, input().split()))

        if query[0] == 1:
            _, l, r = query
            s = process(s, l, r)
        else:
            _, pos = query
            answers.append(s[pos - 1])

    print('\n'.join(answers))


if __name__ == '__main__':
    main()
