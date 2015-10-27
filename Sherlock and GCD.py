"""
Sherlock is stuck. He has an array A1,A2, ..., AN. He wants to know if there exists a subset, B={Ai1,Ai2,...,Aik}
where 1<=i1<i2<...<ik<=N, of this array which follows the property

B is non-empty subset.
There exists no integer x(x>1) which divides all elements of B. Note that x may or may not be an element of A.
Input Format
First line contains T, the number of testcases. Each testcase consists of N in one line. The next line contains
N integers denoting the array A.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        main solution function
        :param cipher: the cipher
        """
        N, lst = cipher
        for i in xrange(N):
            for j in xrange(i + 1, N):
                if self.gcd(lst[i], lst[j]) == 1:
                    return "YES"
        return "NO"

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        N = int(f.readline().strip())
        lst = map(int, f.readline().strip().split(' '))
        cipher = (N, lst)
        # solve
        s = "%s\n" % (Solution().solve(cipher))
        print s,
