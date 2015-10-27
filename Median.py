"""
The median of M numbers is defined as the middle number after sorting them in order, if M is odd. Or it is the average
of the middle 2 numbers (again after sorting), if M is even. You have an empty number list at first. Then you can add in
 or remove some number from the list. For each add or remove operation, output the median of numbers in the list.

Example :
For a set of M = 5 numbers {9, 2, 8, 4, 1} the median is the third number in sorted set {1, 2, 4, 8, 9} which is 4.
Similarly, for a set of M = 4, {5, 2, 10, 4}, the median is the average of second and the third element in the sorted
set {2, 4, 5, 10} which is (4+5)/2 = 4.5.

Input:
The first line is an integer N that indicates the number of operations. Each of the next N lines is either a x or r x .
a x indicates that x is added to the set, and r x indicates that x is removed from the set.
"""
__author__ = 'Danyang'
# from Queue import PriorityQueue  # PriorityQueue does not support removal
import heapq


class Solution_TLE(object):
    def __init__(self):
        self.heap = []

    def solve(self, cipher):
        """
        Heap

        :param cipher: the cipher
        """
        op = cipher[0]
        num = int(cipher[1])
        if op == "r":
            try:
                self.heap.remove(num)
            except ValueError:
                return "Wrong!"
            heapq.heapify(self.heap)
        else:
            heapq.heappush(self.heap, num)

        length = len(self.heap)
        if not self.heap:
            return "Wrong!"
        pq = list(self.heap)
        pq = [heapq.heappop(pq) for _ in xrange(length)]
        if length & 1 == 0:
            return 0.5 * (pq[length / 2 - 1] + pq[length / 2])
        else:
            return pq[length / 2]


class Solution_TLE2(object):
    def __init__(self):
        self.min_heap = []
        self.max_heap = []  # no max heap in Python

    def solve(self, cipher):
        """
        Median_Heap

        Still TLE
        Notice that 6, 7, 8 test cases time out

        :param cipher: the cipher
        """
        op = cipher[0]
        num = int(cipher[1])
        if op == "r":
            try:
                # if self.max_heap and -num>self.max_heap[0]:
                if self.min_heap and num >= self.min_heap[0]:
                    self.min_heap.remove(num)
                    heapq.heapify(self.min_heap)
                else:
                    self.max_heap.remove(-num)
                    heapq.heapify(self.max_heap)
                if not self.min_heap and not self.max_heap:
                    return "Wrong!"
                self.__balance()
            except ValueError:
                return "Wrong!"
        else:
            # if self.max_heap and -num>self.max_heap[0]:
            if self.min_heap and num >= self.min_heap[0]:
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)
            self.__balance()

        # return "%g"%self.__get_median()  # %g rather than %s to avoid trailing zero  # general format # fail
        output = str(self.__get_median())
        if output[-2:] == ".0":
            output = output[:-2]
        return output

    def __balance(self):
        if len(self.min_heap) > len(self.max_heap) + 1:
            item = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, -item)
            return
        if len(self.max_heap) > len(self.min_heap) + 1:
            item = heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, -item)
            return

    def __get_median(self):
        if len(self.min_heap) == len(self.max_heap):
            return 0.5 * (self.min_heap[0] + (-1) * self.max_heap[0])
        elif len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        else:
            return -self.max_heap[0]


from bisect import bisect_left


class Solution(object):
    def __init__(self):
        self.A = []

    def solve(self, cipher):
        """
        bisect
        """
        op = cipher[0]
        val = int(cipher[1])

        pos = bisect_left(self.A, val)
        if op == "r":
            if pos >= len(self.A) or self.A[pos] != val:
                return "Wrong!"
            else:
                del (self.A[pos])
        else:  # "a"
            self.A.insert(pos, val)

        l = len(self.A)
        if l == 0:
            return "Wrong!"
        elif l & 1 == 1:
            return self.A[l / 2]
        else:
            output = str(0.5 * (self.A[l / 2 - 1] + self.A[l / 2]))
            if output[-2:] == ".0":
                output = output[:-2]
            return output


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    # f = sys.stdin
    testcases = int(f.readline().strip())
    solution = Solution()
    for t in xrange(testcases):
        # construct cipher
        cipher = f.readline().strip().split(' ')

        # solve
        s = "%s\n" % (solution.solve(cipher))
        print s,
