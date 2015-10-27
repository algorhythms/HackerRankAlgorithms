"""
Bill Gates is on one of his philanthropic journeys to a village in Utopia. He has N packets of candies and would like to
 distribute one packet to each of the K children in the village (each packet may contain different number of candies).
 To avoid any fighting among the children, he would like to pick K out of N packets, such that unfairness is minimized.

Suppose the K packets have (x1, x2, x3,....xk) candies in them, where xi denotes the number of candies in the ith
, then we define unfairness as

max(x1,x2,...xk) - min(x1,x2,...xk)

where max denotes the highest value amongst the elements, and min denotes the least value amongst the elements. Can you
figure out the minimum unfairness and print it?

Input Format
The first line contains an integer N.
The second line contains an integer K. N lines follow. Each line contains an integer that denotes the candy in the ith
packet.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve_TLE(self, cipher):
        """
        Naive approach - simulate combination.

        Sort and group as K
        :param cipher: the cipher
        """
        N, K, lst = cipher
        lst.sort()
        global_min = 1 << 32 - 1
        for i in xrange(N - K):
            seq = lst[i: i + K]
            global_min = min(global_min, max(seq) - min(seq))

        return global_min

    def solve_TLE2(self, cipher):
        """
        Sliding window

        :param cipher: the cipher
        """
        N, K, lst = cipher
        lst.sort()

        seq = lst[0: K]
        mini = min(seq)
        maxa = max(seq)
        global_min = maxa - mini
        for i in xrange(K, N):
            popped = seq.pop(0)
            cur = lst[i]
            seq.append(cur)
            if popped != mini:
                mini = min(mini, cur)
            else:
                mini = min(seq)
            if popped != maxa:
                maxa = max(maxa, cur)
            else:
                maxa = max(seq)

            global_min = min(global_min, maxa - mini)

        return global_min


    def solve(self, cipher):
        """
        Sliding window
        O(n lgn)

        :param cipher: the cipher
        """
        N, K, lst = cipher
        lst.sort()

        mini = lst[0]
        maxa = lst[K - 1]
        global_min = maxa - mini
        for i in xrange(1, N - K):
            mini = lst[i]
            maxa = lst[i + K - 1]
            global_min = min(global_min, maxa - mini)

        return global_min


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    N = int(f.readline().strip())
    K = int(f.readline().strip())
    lst = []
    for t in xrange(N):
        # construct cipher
        lst.append(int(f.readline().strip()))

    cipher = (N, K, lst)
    # solve
    s = "%s\n" % (Solution().solve(cipher))
    print s,
