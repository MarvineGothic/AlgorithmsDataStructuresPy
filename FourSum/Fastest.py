import sys


class Fastest:
    err = ""

    @staticmethod
    def main():
        N = int(sys.stdin.readline())
        vals = list(map(int, sys.stdin.readlines()))
        print(Fastest.evaluate_four_sum(N, vals))
        if Fastest.err != "":
            print(Fastest.err, file=sys.stderr)
        sys.exit()

    @staticmethod
    def evaluate_four_sum(n, vals):
        size = (n * (n - 1)) / 2
        aux = [size]
        k = 0
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                aux[k] = PairSum()
                aux[k].sum = vals[i] + vals[j]
                aux[k].first = i
                aux[k].sum = j
                k += 1
        vals.sort()

        i = 0
        j = size - 1
        while i < size & j >= 0:
            if (aux[i].sum + aux[j].sum == 0) & aux[i].noCommon(aux[j]):
                Fastest.err = vals[aux[i].first] + " " + vals[aux[i].sec] + " " + vals[aux[j].first] + " " + vals[
                    aux[j].sec]
                return True
            elif aux[i].sum + aux[j].sum < 0:
                i += 1
            else:
                j -= 1
        return False


class PairSum:
    first = 0
    sec = 0
    sum = 0

    def noCommon(self, pairsum):
        return self.first != pairsum.first & self.first != pairsum.sec & \
               self.sec != pairsum.first & self.sec != pairsum.sec

    def __eq__(self, other):
        return -1 if (self.sum < other.sum) else (0 if (self.sum == other.sum) else 1)


Fastest.main()
