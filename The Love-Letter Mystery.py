"""
James found a love letter his friend Harry has written for his girlfriend. James is a prankster, so he decides to meddle
 with the letter. He changes all the words in the letter into palindromes.

To do this, he follows 2 rules:

(a) He can reduce the value of a letter, e.g. he can change 'd' to 'c', but he cannot change 'c' to 'd'.
(b) In order to form a palindrome, if he has to repeatedly reduce the value of a letter, he can do it until the letter
becomes 'a'. Once a letter has been changed to 'a', it can no longer be changed.

Each reduction in the value of any letter is counted as a single operation. Find the minimum number of operations
required to convert a given string into a palindrome.


Input Format
The first line contains an integer T, i.e., the number of test cases.
The next T lines will contain a string each. The strings do not contain any spaces.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        scan from both sides, doing operation
        :param cipher: the cipher
        """
        start_ptr = 0
        end_ptr = len(cipher) - 1

        cnt = 0
        while start_ptr < end_ptr:
            ord1 = ord(cipher[start_ptr]) - ord('a')
            ord2 = ord(cipher[end_ptr]) - ord('a')
            cnt += abs(ord1 - ord2)
            start_ptr += 1
            end_ptr -= 1

        return cnt


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
