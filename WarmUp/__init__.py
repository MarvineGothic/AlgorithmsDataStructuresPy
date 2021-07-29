
from algs4.fundamentals.uf import WeightedQuickUnionUF
from algs4.stdlib import stdio


class UFW:
    if __name__ == '__main__':
        n = stdio.readInt()
        uf = WeightedQuickUnionUF(n)
        while not stdio.isEmpty():
            p = stdio.readInt()
            q = stdio.readInt()
            uf.union(p, q)
        print(uf.connected(0, 1))
