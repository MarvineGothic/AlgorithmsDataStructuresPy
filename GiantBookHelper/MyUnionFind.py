import math


class MyUnionFind:
    setOfVertices = set()
    lastIsolatedV = -1
    giantComp = -1
    conn = -1
    time = 0

    def __init__(self, n):
        """
        Initializes an empty union-find data structure with n sites,
        0 through n-1. Each site is initially in its own component.

        :param n: the number of sites
        """
        self._n = n
        self._count = n
        self._parent = list(range(n))
        self._size = [1] * n

    def _validate(self, p):
        # validate that p is a valid index
        n = len(self._parent)
        if p < 0 or p >= n:
            raise ValueError('index {} is not between 0 and {}'.format(p, n))

    def union(self, p, q):
        """
        Merges the component containing site p with the
        component containing site q.

        :param p: the integer representing one site
        :param q: the integer representing the other site
        """
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q:
            return

        # make root of smaller rank point to root of larger rank
        if self._size[root_p] < self._size[root_q]:
            small, large = root_p, root_q
        else:
            small, large = root_q, root_p

        self._parent[small] = large
        self._size[large] += small

        self._count -= 1
        self.erdosRenyi(p, q)

    def erdosRenyi(self, p, q):
        self.setOfVertices.add(p)
        MyUnionFind.setOfVertices.add(q)
        MyUnionFind.time += 1
        # finding the last isolated vertice using HashSet
        if MyUnionFind.setOfVertices.__sizeof__() == self._n & MyUnionFind.lastIsolatedV == -1:
            MyUnionFind.lastIsolatedV = MyUnionFind.time
        # finding the first giant component(number of vertices >= half of total number)
        if MyUnionFind.giantComp == -1 & self.find(p) >= math.ceil(self._n / 2):
            MyUnionFind.giantComp = MyUnionFind.time
        # if count == 1 then size array has total number of vertices and graph is connected
        if self.count() == 1 & MyUnionFind.conn == -1:
            MyUnionFind.conn = MyUnionFind.time

    def find(self, p):
        """
        Returns the component identifier for the component containing site p.

        :param p: the integer representing one site
        :return: the component identifier for the component containing site p
        """
        self._validate(p)
        while p != self._parent[p]:
            p = self._parent[p]
        return p

    def connected(self, p, q):
        """
        Returns true if the two sites are in the same component.

        :param p: the integer representing one site
        :param q: the integer representing the other site
        :return: true if the two sites p and q are in the same component; false otherwise
        """
        return self.find(p) == self.find(q)

    def count(self):
        return self._count

    def getSize(self):
        return self._size

    def get_last_isol_vertex(self):
        return self.lastIsolatedV

    def get_giant_comp(self):
        return self.giantComp

    def get_connected(self):
        return self.conn
