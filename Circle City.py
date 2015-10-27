"""
Problem Statement

Roy lives in a city that is circular in shape on a 2D plane. The city center is located at origin (0,0) and it has
suburbs lying on the lattice points (points with integer coordinates). The city Police Department Headquarters can only
protect those suburbs which are located strictly inside the city. The suburbs located on the border of the city are
still unprotected. So the police department decides to build at most k additional police stations at some suburbs. Each
of these police stations can protect the suburb it is located in.

Given the radius of the city, Roy has to determine if it is possible to protect all the suburbs.

Input Format
The first line of input contains integer t, t testcases follow.
Each of next t lines contains two space separated integers: r, the square of the radius of the city and k, the maximum
number of police stations the headquarters is willing to build.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        Boarder detection
        Binary search for coordinates.

        Python time out, use C++ instead.
        :param cipher: the cipher
        """
        r2, k = cipher

        required = 0
        r = r2 ** 0.5

        for x in xrange(0, int(r) + 1):
            # binary search
            low = 0
            high = int(r) + 1
            while low <= high:
                mid = (low + high) / 2
                if x * x + mid * mid == r2:
                    if mid == 0 or x == 0:
                        required += 2
                    else:
                        required += 4
                    if required > k: return "impossible"
                    break
                elif x * x + mid * mid < r2:
                    low = mid + 1
                else:
                    high = mid - 1

        if required > k: return "impossible"
        return "possible"


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        cipher = map(int, f.readline().strip().split(' '))

        # solve
        s = "%s\n" % (Solution().solve(cipher))
        print s,
