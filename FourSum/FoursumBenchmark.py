import glob
from os.path import expanduser

from algs4.stdlib.stdrandom import shuffle
import time

from algs4.stdlib.stdstats import mean, stddev

from FourSum.Fastest import Fastest
from FourSum.Simple import Simple


class FousumBenchmark:
    @staticmethod
    def run_test(number_of_tests, test_size):
        tree_map = dict()
        for files in glob.glob(expanduser("~") + "/PycharmProjects/AD/data/foursum/*.txt"):
            with open(files) as file:
                N = int(file.readline())
                vals = [int(x) for x in file.read().split()]
                file.close()
                if N == test_size:
                    print(file.name)
                    print(N)
                    for test in range(0, number_of_tests):
                        shuffle(vals)
                        start_time_ms = int(round(time.time() * 1000))
                        Fastest.evaluate_four_sum(N, vals)
                        run_time_ms = int(round(time.time() * 1000)) - start_time_ms
                        if N not in tree_map:
                            tree_map[N] = []
                        tree_map[N].append(run_time_ms)
        return tree_map

    @staticmethod
    def print_results(tree_map):
        for entry in tree_map:
            array = tree_map.get(entry)
            print(array)
            print("N = %d\t\tT = %d\t\tMin = %.2f\t\tAvg = %.2f ms\t\tMax = %.2f\t\tstdDev = %.2f\n"
                  % (entry, len(tree_map.get(entry)), min(array), mean(array), max(array), stddev(array)))


if __name__ == '__main__':
    FousumBenchmark.print_results(FousumBenchmark.run_test(10, 200))
    FousumBenchmark.print_results(FousumBenchmark.run_test(1, 400))
    FousumBenchmark.print_results(FousumBenchmark.run_test(1, 800))
