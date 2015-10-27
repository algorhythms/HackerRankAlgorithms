"""
Given an array with n elements, can you sort this array in ascending order using just one of the following operations?
You can perform only one of the following operations:
1. Swap two elements.
2. Reverse one sub-segment

Input Format
The first line contains a single integer n, which indicates the size of the array. The next line contains n integers
seperated by spaces.

n
d1 d2 ... dn
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        O(n lgn) brute force
        O(n) scanning

        Array pointers
        Logic thinking
        Divide and Conquer rather than dealing with multiple things together

        A very good interview question

        main solution function
        :param cipher: the cipher
        """
        # find start
        A = cipher
        N = len(A)
        start = 0
        while start + 1 < N and A[start] <= A[start + 1]:
            start += 1

        # find test swap or reverse
        end = start + 1
        while end + 1 < N and A[end] >= A[end + 1]:
            end += 1

        if end == start + 1:  # swap
            # find the item to be swapped
            j = start + 1
            while j + 1 < N and A[j] < A[j + 1]:
                j += 1

            # not found
            if j != start + 1 and j + 1 == N:  # test cases: [3, 1], [3, 1, 2]
                return "no"
            # test tailing
            i = j + 1
            while i + 1 < N:
                if not A[i] < A[i + 1]:
                    return "no"
                i += 1

            if j != start + 1:
                j += 1
            return "yes\nswap %d %d" % (start + 1, j + 1)
        else:  # reverse
            # test tailing
            i = end + 1
            while i + 1 < N:
                if not A[i] < A[i + 1]:
                    return "no"
                i += 1

            if end + 1 < N and A[start] > A[end + 1]:  # even though reversed
                return "no"

            return "yes\nreverse %d %d" % (start + 1, end + 1)


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    testcases = int(f.readline().strip())


    # construct cipher
    cipher = map(int, f.readline().strip().split(' '))

    # solve
    s = "%s\n" % (Solution().solve(cipher))
    print s,
