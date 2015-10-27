"""
https://www.hackerrank.com/challenges/encryption
One classic method for composing secret messages is called a square code.  The spaces are removed from the english text
and the characters are written into a square (or rectangle). The width and height of the rectangle have the constraint,

floor(sqrt( len(word) )) <= width, height <= ceil(sqrt( len(word) ))

Among the possible squares, choose the one with the minimum area.

In case of a rectangle, the number of rows will always be smaller than the number of columns. For example, the sentence
"if man was meant to stay on the ground god would have given us roots" is 54 characters long, so it is written in the
form of a rectangle with 7 rows and 8 columns. Many more rectangles can accomodate these characters; choose the one with
minimum area such that: length * width >= len(word)

                ifmanwas
                meanttos
                tayonthe
                groundgo
                dwouldha
                vegivenu
                sroots

The coded message is obtained by reading the characters in a column, inserting a space, and then moving on to the next
column towards the right. For example, the message above is coded as:

imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau

You will be given a message in English with no spaces between the words.The maximum message length can be 81 characters.
Print the encoded message.

Here are some more examples:

Sample Input:

haveaniceday

Sample Output:

hae and via ecy
"""
from math import sqrt, floor, ceil

__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        l = len(cipher)
        r = range(int(floor(sqrt(l))), int(ceil(sqrt(l))) + 1)

        min_pair = (r[-1], r[-1])
        for h in r:
            for w in r:
                if h * w >= l and h * w < min_pair[0] * min_pair[1]:
                    min_pair = (h, w)
        h, w = min_pair
        rect = [[None for _ in xrange(w)] for _ in xrange(h)]
        for i in xrange(l):
            rect[i / w][i % w] = cipher[i]

        result = []
        for j in xrange(w):
            sb = []
            for i in xrange(h):
                if rect[i][j] == None: break
                sb.append(rect[i][j])
            result.append("".join(sb))

        return " ".join(result)


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    cipher = f.readline().strip()

    # solve
    s = "%s\n" % (Solution().solve(cipher))
    print s,
