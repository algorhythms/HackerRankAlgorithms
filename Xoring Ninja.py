"""
Given a list containing N integers, calculate the XOR_SUM of all the non-empty subsets of the list and print the value
of sum % (109 + 7).

XOR operation on a list (or a subset of the list) is defined as the XOR of all the elements present in it.
E.g. XOR of list containing elements {A,B,C} = ((A^B)^C), where ^ represents XOR.

E.g. XOR_SUM of list A having three elements {X1, X2, X3} can be given as follows.
All non-empty subsets will be {X1, X2, X3, (X1,X2), (X2,X3), (X1,X3), (X1,X2,X3)}

XOR_SUM(A) = X1 + X2 + X3 + X1^X2 + X2^X3 + X1^X3 + ((X1^X2)^X3)

Input Format
An integer T, denoting the number of testcases. 2T lines follow.
Each testcase contains two lines, first line will contains an integer N followed by second line containing N integers
separated by a single space.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        Algorithm:
        From the prospective of bit
        http://math.stackexchange.com/questions/712487/finding-xor-of-all-subsets
        :param cipher: the cipher
        """
        length, lst = cipher

        return reduce(lambda x, y: x | y, lst) * 2 ** (length - 1) % (10 ** 9 + 7)


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        length = int(f.readline().strip())
        lst = map(lambda x: int(x), f.readline().strip().split(" "))
        cipher = [length, lst]
        # solve
        s = "%s\n" % (Solution().solve(cipher))
        print s,
