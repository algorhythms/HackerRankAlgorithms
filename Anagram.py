"""
Sid is obsessed about reading short stories. Being a CS student, he is doing some interesting frequency analysis with
the books. He has two short story books. He chooses strings having length a from the first book and strings having
length b from the second one. The strings are such that the difference of length is <= 1

i.e.

|a-b|<=1, where |x| represents the absolute value of x.
He believes that both the strings should be anagrams based on his experiment. Your challenge is to help him find the
minimum number of characters of the first string he needs to change to make it an anagram of the second string. He can
neither add a character nor delete a character from the first string. Only replacement of the original characters with
the new ones is allowed.

Input Format

The first line will contain an integer T representing the number of test cases. Each test case will contain a string
having length (a+b) which will be concatenation of both the strings described above in the problem. The string will only
contain small letters and there will be no spaces in the string.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        main solution function
        :param cipher: the cipher
        """
        cipher = cipher[0]
        length = len(cipher)
        if length & 1 == 1:
            return -1
        str1 = cipher[:length / 2]
        str2 = cipher[length / 2:]
        # str1_lst.sort()
        # str2_lst.sort()
        # # simplified edit distance
        # cum = 0
        # for i in xrange(length/2):
        # if str1_lst[i]!=str2_lst[i]:
        #         cum += 1
        # return cum

        # bucket sort
        bucket = [0 for _ in xrange(256)]
        for elt in str1:
            bucket[ord(elt)] += 1
        for elt in str2:
            bucket[ord(elt)] -= 1
        return sum(filter(lambda x: x > 0, bucket))


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        cipher = f.readline().strip().split(' ')

        # solve
        s = "%s\n" % (Solution().solve(cipher))
        print s,
