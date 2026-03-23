MOD = 10**9 + 7


def cells(i):
    if i % 2 == 1:
        return (i // 4) * 2 + 1
    return ((i - 1) // 4) * 2 + 2


def main():
    n, k = map(int, input().split())

    if k > 2 * n - 1:
        print(0)
        return

    dp = [[0] * (k + 1) for _ in range(2 * n)]
    for i in range(2 * n):
        dp[i][0] = 1

    if k >= 1:
        dp[1][1] = 1

    for i in range(2, 2 * n):
        for j in range(1, k + 1):
            dp[i][j] = dp[i - 2][j]
            free = cells(i) - j + 1
            if free > 0:
                dp[i][j] = (dp[i][j] + dp[i - 2][j - 1] * free) % MOD

    answer = 0
    for x in range(k + 1):
        answer = (answer + dp[2 * n - 1][x] * dp[2 * n - 2][k - x]) % MOD

    print(answer)


if __name__ == '__main__':
    main()
