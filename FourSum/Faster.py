from __future__ import print_function
import sys


class Faster:
    err = ""

    @staticmethod
    def main():
        N = int(sys.stdin.readline())
        vals = list(map(int, sys.stdin.readlines()))
        print(Faster.evaluate_four_sum(N, vals))
        if Faster.err != "":
            print(Faster.err, file=sys.stderr)
        sys.exit()

    @staticmethod
    def evaluate_four_sum(N, vals):
        vals.sort()
        for i in range(0, N - 3):
            for j in range(i + 1, N - 2):
                k = j + 1
                r = N - 1
                while k < r:
                    if vals[i] + vals[j] + vals[k] + vals[r] == 0:
                        Faster.err = "%s %s %s %s" % (i, j, k, r)
                        return True
                    elif vals[i] + vals[j] + vals[k] + vals[r] < 0:
                        k += 1
                    else:
                        r -= 1
        return False


if __name__ == '__main__':
    Faster.main()
