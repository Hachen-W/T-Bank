def process(people_count, numbers, index):
    same_number = 0
    for number in numbers:
        if number == numbers[index]:
            same_number += 1
    flag = 1
    for number in numbers:
        a1 = numbers[index - 1]
        a2 = numbers[index]
        a3 = numbers[(index + 1) % people_count]
        if number == a2 and (a2 == a1 or a2 == a3 or (a2 > a1 and a2 > a3) or (a2 < a1 and a2 < a3)):
            flag = 0
    return people_count - same_number + flag

def main():
    people_count = int(input())
    numbers = list(map(int, input().split()))
    answer = list()
    for index in range(people_count):
        answer.append(process(people_count, numbers, index))
    print(*answer)


if __name__ == '__main__':
    main()
