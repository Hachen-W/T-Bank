def main():
    s = input().strip()
    n = len(s)

    a = "tbank"
    b = "study"
    m = 5
    INF = 10**9

    cost_a = [INF] * n
    cost_b = [INF] * n

    for i in range(n - m + 1):
        ca = 0
        cb = 0
        for j in range(m):
            if s[i + j] != a[j]:
                ca += 1
            if s[i + j] != b[j]:
                cb += 1
        cost_a[i] = ca
        cost_b[i] = cb

    last = n - m + 1

    pref_a = [INF] * last
    pref_b = [INF] * last
    pref_a[0] = cost_a[0]
    pref_b[0] = cost_b[0]
    for i in range(1, last):
        pref_a[i] = min(pref_a[i - 1], cost_a[i])
        pref_b[i] = min(pref_b[i - 1], cost_b[i])

    suff_a = [INF] * last
    suff_b = [INF] * last
    suff_a[-1] = cost_a[last - 1]
    suff_b[-1] = cost_b[last - 1]
    for i in range(last - 2, -1, -1):
        suff_a[i] = min(suff_a[i + 1], cost_a[i])
        suff_b[i] = min(suff_b[i + 1], cost_b[i])

    ans = INF

    for i in range(last):
        ans = min(ans, cost_a[i] + (pref_b[i - m] if i - m >= 0 else INF))
        ans = min(ans, cost_a[i] + (suff_b[i + m] if i + m < last else INF))

        ans = min(ans, cost_b[i] + (pref_a[i - m] if i - m >= 0 else INF))
        ans = min(ans, cost_b[i] + (suff_a[i + m] if i + m < last else INF))

    for start_a in range(last):
        for shift in range(-4, 5):
            start_b = start_a + shift
            if not (0 <= start_b < last):
                continue

            ok = True
            need = {}

            for j in range(m):
                pos = start_a + j
                need[pos] = a[j]

            for j in range(m):
                pos = start_b + j
                if pos in need and need[pos] != b[j]:
                    ok = False
                    break
                need[pos] = b[j]

            if not ok:
                continue

            cur = 0
            for pos, ch in need.items():
                if s[pos] != ch:
                    cur += 1

            ans = min(ans, cur)

    print(ans)


if __name__ == "__main__":
    main()
