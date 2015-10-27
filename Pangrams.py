"""
Roy wanted to increase his typing speed for programming contests. So, his friend advised him to type the sentence "The
quick brown fox jumps over the lazy dog" repeatedly because it is a pangram. ( pangrams are sentences constructed by
using every letter of the alphabet at least once. )

After typing the sentence several times, Roy became bored with it. So he started to look for other pangrams.

Given a sentence s, tell Roy if it is a pangram or not.

Input Format

Input consists of a line containing s.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        Algorithm:
        bucket, O(N). Non-brainer
        :param cipher: the cipher
        """
        bucket = [False for _ in xrange(26)]
        for char in cipher:
            char = char.lower()
            ind = ord(char) - ord('a')
            try:
                bucket[ind] = True
            except IndexError:
                pass

        is_pangram = all(bucket)
        if is_pangram:
            return "pangram"
        else:
            return "not pangram"


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    testcases = 1

    for t in xrange(testcases):
        # construct cipher
        cipher = f.readline().strip()

        # solve
        s = "%s\n" % (Solution().solve(cipher))
        print s,
