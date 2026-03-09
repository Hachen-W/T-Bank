def solve():
    n = int(input())
    a = list(map(int, input().split()))

    last = {0: 0}
    pref = 0
    start = 0
    ans = 0

    for r in range(1, n + 1):
        pref += a[r - 1]
        if pref in last:
            start = max(start, last[pref] + 1)
        ans += start
        last[pref] = r

    print(ans)


solve()
