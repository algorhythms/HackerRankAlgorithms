# -*- coding: utf-8 -*-
"""
There are n groups of friends, and each group is numbered from 1 to n. The ith group contains ai people.

They live near a bus stop, and only a single bus operates on this route. An empty bus arrives at the bus stop and all
the groups want to travel by the bus.

However, group of friends do not want to get separated. So they enter the bus only if the bus can carry the entire
group.

Moreover, the groups do not want to change their relative positioning while travelling. In other words, group 3 cannot
travel by bus, unless group 1 and group 2 have either (a) already traveled by the bus in the previous trip or (b) they
are also sitting inside the bus at present.

You are given that a bus of size x can carry x people simultaneously.

Find the size x of the bus so that (1) the bus can transport all the groups and (2) every time when the bus starts from
the bus station, there is no empty space in the bus (i.e. the total number of people present inside the bus is equal to
x)?

Input Format
The first line contains an integer n (1≤n≤105). The second line contains n space-separated integers a1,a2,…,an
(1≤ai≤104).
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        sum
        brute force - how to improve?
        prune - can we do better?
        Algorithm:
        rather than simulate the bus trip, consider the math model
        1k, 2k, 3k, 4k, 5k

        :type cipher: list
        :param cipher: the cipher
        """
        N = len(cipher)
        sum_set = set()
        s = 0
        for val in cipher:
            s += val
            sum_set.add(s)

        result = []
        for k in sum_set:
            if s % k == 0:
                j = 1
                while j < s / k + 1 and j * k in sum_set:
                    j += 1
                if j == s / k + 1:
                    result.append(k)

        result.sort()  # need sort since set does not preserve order
        return " ".join(map(str, result))


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    N = int(f.readline().strip())


    # construct cipher
    cipher = map(int, f.readline().strip().split(' '))

    # solve
    s = "%s\n" % (Solution().solve(cipher))
    print s,
