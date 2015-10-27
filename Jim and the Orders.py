# -*- coding: utf-8 -*-
"""
In Jim's Burger, n hungry burger fans are ordering burgers. The ith order is placed by the ith fan at ti time and it
takes di time to procees. What is the order in which the fans will get their burgers?

Input Format
On the first line you will get n, the number of orders. Then n lines will follow. On the (i+1)th line, you will get ti
and di separated by a single space.

Output Format
Print the order ( as single space separated integers ) in which the burger fans get their burgers. If two fans get the
burger at the same time, then print the smallest numbered order first.(remember, the fans are numbered 1 to n).

Constraints
1≤n≤103
1≤ti,di≤106

Sample Input #00

3
1 3
2 3
3 3
Sample Output #00

1 2 3
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        simple sorting
        :param cipher: the cipher
        """
        A = cipher
        n = len(A)
        idx = sorted(range(n), key=lambda k: A[k][0] + A[k][1])
        return " ".join(map(lambda x: str(x + 1), idx))


if __name__ == "__main__":
    import sys

    f = open("0.in", "r")
    # f = sys.stdin
    solution = Solution()
    n = int(f.readline().strip())

    cipher = []
    for i in xrange(n):
        # construct cipher
        t = map(int, f.readline().strip().split(' '))
        cipher.append(tuple(t))

    # solve
    s = "%s\n" % (solution.solve(cipher))
    print s,
