"""
iven two integers: L and R,

find the maximal values of A xor B given, L <= A <= B <= R

Input Format
The input contains two lines, L is present in the first line.
R in the second line.

Constraints
1 <= L <= R <= 103

Output Format
The maximal value as mentioned in the problem statement.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        main solution function
        :param cipher: the cipher
        """
        global_max = -1
        A, B = cipher
        for i in xrange(A, B + 1):
            for j in xrange(i + 1, B + 1):
                global_max = max(global_max, i ^ j)
        return global_max


if __name__ == "__main__":
    import sys
    # f = open("1.in", "r")
    f = sys.stdin
    A = int(f.readline().strip())
    B = int(f.readline().strip())
    cipher = (A, B)

    s = "%s\n" % (Solution().solve(cipher))
    print s,
