class TinkoffTreeSolver:
    def __init__(self):
        self.n = 0
        self.k = 0
        self.company_to_id = {}
        self.parent = []
        self.cost = []
        self.company_mask = []
        self.children = []
        self.mask = []
        self.subsum = []
        self.root = -1
        self.FULL_MASK = 0

    def read_input(self):
        self.n, self.k = map(int, input().split())

        for idx in range(self.k):
            name = input().strip()
            self.company_to_id[name] = idx

        self.parent = [0] * (self.n + 1)
        self.cost = [0] * (self.n + 1)
        self.company_mask = [0] * (self.n + 1)
        self.children = [[] for _ in range(self.n + 1)]

        for i in range(1, self.n + 1):
            p_i, a_i, c_i = input().split()
            p_i = int(p_i)
            a_i = int(a_i)

            self.parent[i] = p_i
            self.cost[i] = a_i

            cid = self.company_to_id[c_i]
            self.company_mask[i] = 1 << cid

            if p_i == 0:
                self.root = i
            else:
                self.children[p_i].append(i)

        self.FULL_MASK = (1 << self.k) - 1
        self.mask = [0] * (self.n + 1)
        self.subsum = [0] * (self.n + 1)

    def dfs(self, v: int):
        m = self.company_mask[v]
        s = self.cost[v]
        for u in self.children[v]:
            self.dfs(u)
            m |= self.mask[u]
            s += self.subsum[u]
        self.mask[v] = m
        self.subsum[v] = s

    def solve(self) -> int:
        self.dfs(self.root)

        ans = None
        for v in range(1, self.n + 1):
            if self.mask[v] == self.FULL_MASK:
                if ans is None or self.subsum[v] < ans:
                    ans = self.subsum[v]

        return -1 if ans is None else ans


def main():
    solver = TinkoffTreeSolver()
    solver.read_input()
    print(solver.solve())


if __name__ == "__main__":
    main()
