"""
Alice recently started learning about cryptography and found that anagrams are very useful. Two strings are anagrams of
each other if they have same character set. For example strings "bacdc" and "dcbac" are anagrams, while strings "bacdc"
and "dcbad" are not.

Alice decides on an encryption scheme involving 2 large strings where encryption is dependent on the minimum number of
character deletions required to make the two strings anagrams. She need your help in finding out this number.

Given two strings (they can be of same or different length) help her in finding out the minimum number of character
deletions required to make two strings anagrams. Any characters can be deleted from any of the strings.

Input Format
Two lines each containing a string.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve_MLE(self, cipher):
        """
        Memory Limit Exceeds
        dp
        dp[i][j] = min(dp[i-1][j], dp[i][j-1])+1 if a[i]!=b[j]
        dp[i][j] = dp[i-1][j-1] if a[i]==b[j]
        :param cipher: the cipher
        """
        a, b = cipher
        a, b = list(a), list(b)
        m = len(a)
        n = len(b)
        a.sort()
        b.sort()

        dp = [[0 for _ in xrange(n + 1)] for _ in xrange(m + 1)]
        for i in xrange(m + 1):
            dp[i][0] = i
        for j in xrange(n + 1):
            dp[0][j] = j
        for i in xrange(1, m + 1):
            for j in xrange(1, n + 1):
                if a[i - 1] == b[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + 1

        return dp[-1][-1]

    def solve(self, cipher):
        """
        bucket
        :param cipher: the cipher
        """
        a, b = cipher
        bucket = [0 for _ in xrange(26)]
        for char in a:
            bucket[ord(char) - ord('a')] += 1
        for char in b:
            bucket[ord(char) - ord('a')] -= 1

        counter = 0
        for ind, val in enumerate(bucket):
            counter += abs(val - 0)

        return counter


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    cipher = []
    cipher.append(f.readline().strip())
    cipher.append(f.readline().strip())

    s = "%s\n" % (Solution().solve(cipher))
    print s,
