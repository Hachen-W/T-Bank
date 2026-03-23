def main():
    s = input()
    answer = ''
    digits_count = [0] * 10
    for symbol in s:
        digits_count[ord(symbol) - ord('0')] += 1
    for digit in range(1, 10):
        if digits_count[digit] != 0:
            answer += str(digit)
            digits_count[digit] -= 1
            break
    for digit in range(10):
        while digits_count[digit] != 0:
            answer += str(digit)
            digits_count[digit] -= 1
    print(answer)


if __name__ == '__main__':
    main()
