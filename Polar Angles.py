"""
A point (x,y), on the cartesian plane, makes an angle theta with the positive direction of the x-axis. Theta varies in
the interval [0 ,2PI) radians, i.e, greater than or equal to zero; but less than 2*PI radians.

For example, the polar angle of the point (1,2) as marked in this plane below, is (approximately) 63.4 degrees (multiply
by PI/180 to convert to radians)

Ref http://eldar.mathstat.uoguelph.ca/dashlock/Outreach/Articles/images/PRfig1.jpg

The Task

Given a list of points in the 2D plane, sort them in ascending order of their polar angle. In case multiple points share
exactly the same polar angle, the one with lesser distance from the origin (0,0) should occur earlier in the sorted list.

Input Format
The first line contains an integer N.
This is followed by N lines containing pairs of space separated integers, x and y which represent the coordinates of the
points in the cartesian plane.
"""
import math

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        main solution function
        :param cipher: the cipher
        """
        cipher.sort(cmp=self.cmp)


    def cmp_polar(self, a, b):
        """
        cross product, but what if \pi?
        error, can only sort by clockwise
        """
        x1 = a[0]
        y1 = a[1]
        x2 = b[0]
        y2 = b[1]
        # (0, 0) as anchor point
        cross_product = x1 * y2 - x2 * y1
        if cross_product > 0:
            return -1
        elif cross_product < 0:
            return 1
        else:
            if x1 * x1 >= 0 and y1 * y1 >= 0:
                return x1 * x1 + y1 * y1 - x2 * x2 - y2 * y2
            else:
                if y1 > 0:
                    return -1
                if y2 > 0:
                    return 1
                if y1 == 0 and x1 > 0:
                    return -1
                else:
                    return 1

    def cmp(self, a, b):
        """
        polar coordinate
        """
        x1 = a[0]
        y1 = a[1]
        x2 = b[0]
        y2 = b[1]
        r1 = x1 * x1 + y1 * y1
        r2 = x2 * x2 + y2 * y2
        phi1 = math.atan2(y1, x1)
        phi2 = math.atan2(y2, x2)
        if phi1 < 0:
            phi1 += math.pi * 2
        if phi2 < 0:
            phi2 += math.pi * 2
        if phi1 < phi2:
            return -1
        elif phi1 > phi2:
            return 1
        else:
            return r1 - r2


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    N = int(f.readline().strip())

    cipher = []
    for t in xrange(N):
        # construct cipher
        cipher.append(map(int, f.readline().strip().split(' ')))
        # solve
    Solution().solve(cipher)
    for point in cipher:
        print "%d %d" % (point[0], point[1])
