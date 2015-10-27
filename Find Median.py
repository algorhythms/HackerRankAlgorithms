"""
Problem Statement

The median of a finite list of numbers can be found by arranging all the integers from lowest to highest value and
picking the middle one. For example, the median of {3,3,5,9,11} is 5. If there is an even number of integers, then
there is no single middle value, and the median is then usually defined to be the mean of the two middle values. For
examples, the median of {3,5,7,9} is (5+7)2=6.

Given that integers are read from a data stream, find the median of elements read so far in an efficient way.
"""
__author__ = 'Daniel'
import heapq


class DualHeap(object):
    def __init__(self):
        """
        Dual Heap is great in the case where there is no removal.
        :return:
        """
        self.min_h = []
        self.max_h = []

    def insert(self, num):
        if not self.min_h or num > self.min_h[0]:
            heapq.heappush(self.min_h, num)
        else:
            heapq.heappush(self.max_h, -num)
        self.balance()

    def balance(self):
        l1 = len(self.min_h)
        l2 = len(self.max_h)
        if l1 - l2 > 1:
            heapq.heappush(self.max_h, -heapq.heappop(self.min_h))
            self.balance()
        elif l2 - l1 > 1:
            heapq.heappush(self.min_h, -heapq.heappop(self.max_h))
            self.balance()
        return

    def get_median(self):
        l1 = len(self.min_h)
        l2 = len(self.max_h)
        m = (l1 + l2 - 1) / 2
        if (l1 + l2) % 2 == 1:
            if m == l2 - 1:
                return -self.max_h[0]
            elif m == l2:
                return self.min_h[0]
            raise Exception("not balanced")
        else:
            return (-self.max_h[0] + self.min_h[0]) / 2.0


class Solution:
    def __init__(self):
        self.dh = DualHeap()

    def solve(self, cipher):
        """
        :param nums: A list of integers.
        :return: The median of numbers
        """
        self.dh.insert(cipher)
        return self.dh.get_median()


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    # f = sys.stdin
    solution = Solution()
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        cipher = int(f.readline().strip())
        s = "%.1f\n" % (solution.solve(cipher))
        print s,
