from typing import List, Tuple


class OVJMedianMaximizer:
    def __init__(self, n: int, s: int, segments: List[Tuple[int, int]]):
        self.n = n
        self.s = s
        self.segments = sorted(segments)
        self.base_sum = sum(elem for elem, _ in segments)
        self.max_r = max(r for _, r in segments)
        self.need_cnt = n // 2 + 1

    def _can(self, x: int) -> bool:
        total = self.base_sum
        already = 0

        for elem, _ in self.segments:
            if elem >= x:
                already += 1

        need = self.need_cnt - already
        if need <= 0:
            return total <= self.s

        # добираем тех, кого можем поднять до x
        for i in range(self.n - 1, -1, -1):
            l, r = self.segments[i]
            if l < x <= r:
                total += x - l
                need -= 1
                if need == 0:
                    break

        return need == 0 and total <= self.s

    def solve(self) -> int:
        lo, hi = 1, self.max_r
        ans = 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if self._can(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans


def main():
    n, s = map(int, input().split())
    segments = []
    for _ in range(n):
        l, r = map(int, input().split())
        segments.append((l, r))

    solver = OVJMedianMaximizer(n, s, segments)
    print(solver.solve())


if __name__ == "__main__":
    main()
