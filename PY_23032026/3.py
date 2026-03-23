def make_table(string):
    n = len(string)
    doubled = string + string

    best = 0
    current = 0

    for symbol in doubled:
        if symbol == '1':
            current += 1
            if current > best:
                best = current
        else:
            current = 0

    if best > n:
        best = n

    return best


def process(table):
    ones_len = table

    if ones_len == 0:
        print(0)
        return

    answer = 0
    for width in range(1, ones_len + 1):
        height = ones_len - width + 1
        area = width * height
        if area > answer:
            answer = area

    print(answer)




def main():
    count = int(input())
    strings = [input() for _ in range(count)]
    for num_elem in range(count):
        table = make_table(strings[num_elem])
        process(table)



if __name__ == '__main__':
    main()
