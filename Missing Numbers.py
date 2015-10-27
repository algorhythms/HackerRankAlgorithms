"""
Problem Statement

Numeros, The Artist, had two lists A and B, such that, B was a permutation of A. Numeros was very proud of these lists.
Unfortunately, while transporting them from one exhibition to another, some numbers from List A got left out. Can you
find out the numbers missing from A?
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """

        :param cipher: the cipher
        """
        m, A, n, B = cipher

        result = set()  # {} is for dictionary
        hm = {}
        for a in A:
            if a not in hm:
                hm[a] = 1
            else:
                hm[a] += 1

        for b in B:
            if b not in hm or hm[b] <= 0:
                result.add(b)
            else:
                hm[b] -= 1
        result = sorted(list(result))
        return " ".join(map(str, result))


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    solution = Solution()
    m = int(f.readline().strip())
    A = map(int, f.readline().strip().split(' '))
    n = int(f.readline().strip())
    B = map(int, f.readline().strip().split(' '))

    cipher = m, A, n, B
    # solve
    s = "%s\n" % (solution.solve(cipher))
    print s,
