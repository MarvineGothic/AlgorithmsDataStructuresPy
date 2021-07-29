from algs4.stdlib import stdio

from GiantBookHelper.MyUnionFind import MyUnionFind


class GBH:
        with open("C://Users\Admin\PycharmProjects\AD\data\oneUF.txt") as file:
         print(file.read())
        n = stdio.readInt()
        uf = MyUnionFind(n)
        while stdio.hasNextLine():
            p = stdio.readInt()
            q = stdio.readInt()
            uf.erdosRenyi(p, q)
        print("{} {} {} {}".format(n, uf.get_last_isol_vertex(), uf.get_giant_comp(), uf.get_connected()))
