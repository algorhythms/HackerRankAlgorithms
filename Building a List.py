"""
Problem Statement

Chan has decided to make a list of all possible combinations of letters of a given string S. If there are two strings
with the same set of characters, print the lexicographically smallest arrangement of the two strings.

abc acb cab bac bca
all the above strings' lexicographically smallest string is abc.

Each character in the string S is unique. Your task is to print the entire list of Chan's in lexicographic order.

for string abc, the list in lexicographic order is given below

a ab abc ac b bc c
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        main solution function
        :param cipher: the cipher
        """
        s = cipher
        s = "".join(sorted(list(s)))
        result = []
        self.dfs(s, "", result)
        return "\n".join(result[1:])

    def dfs(self, seq, cur, result):
        result.append(cur)
        if seq:
            for i in xrange(len(seq)):
                self.dfs(seq[i + 1:], cur + seq[i], result)


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        N = int(f.readline().strip())
        cipher = f.readline().strip()

        # solve
        s = "%s\n" % (Solution().solve(cipher))
        print s,
