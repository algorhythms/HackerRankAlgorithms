"""
You are given a string of lowercase letters. Your task is to figure out the index of the character on whose removal will
make the string a palindrome. There will always be a valid solution.

In case string is already palindrome, then -1 is also a valid answer along with possible indices.

Input Format
The first line contains T i.e. number of test cases.
T lines follow, each line containing a string.
"""
__author__ = 'Danyang'


class Solution_TLE(object):
    def solve(self, cipher):
        """
        Algorithm:
        brutal force. O(N^2)
        Non-brainer
        :param cipher: the cipher
        """
        for i in xrange(len(cipher)):
            if self.__is_palindrome(cipher[:i] + cipher[i + 1:]):
                return i

        return -1

    def __is_palindrome(self, s):
        return s == s[::-1]


class Solution(object):
    def solve(self, cipher):
        """
        Algorithm:
        Guarantee one and only one answer
        O(N)
        :param cipher: the cipher
        """
        l = len(cipher)
        start = 0
        end = l - 1
        while start < end and cipher[start] == cipher[end]:
            start += 1
            end -= 1

        if self.__is_palindrome(cipher[:start] + cipher[start + 1:]):
            return start
        if self.__is_palindrome(cipher[:end] + cipher[end + 1:]):
            return end

        if start >= end:
            return -1

    def __is_palindrome(self, s):
        return s == s[::-1]


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        cipher = f.readline().strip()

        # solve
        s = "%s\n" % (Solution().solve(cipher))
        print s,
