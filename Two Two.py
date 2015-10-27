"""
Prof. Twotwo as the name suggests is very fond powers of 2. Moreover he also has special affinity to number 800. He is
known for carrying quirky experiments on powers of 2.

One day he played a game is his class. He brought some number plates on each of which a digit from 0 to 9 is written. He
made students stand in a row and gave a number plate to each of the student. Now turn by turn, he called for some
students who are standing continuously in the row say from index i to index j (i<=j) and asked them to find their
strength.

The strength of the group of students from i to j is defined as:

strength(i , j)
{
    if a[i] = 0
        return 0; //If first child has value 0 in the group, strength of group is zero
    value = 0;
    for k from i to j
        value = value*10 + a[k]
    return value;
}
Prof called for all possible combinations of i and j and noted down the strength of each group. Now being interested in
powers of 2, he wants to find out how many strengths are powers of two. Now its your responsibility to get the answer
for prof.

Input Format
First line contains number of test cases T
Next T line contains the numbers of number plates the students were having when standing in the row in the form of a
string A.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve_TLE(self, cipher):
        """
        main solution function
        :param cipher: the cipher
        """
        # a = map(lambda x: int(x), list(cipher[0]))
        a = cipher[0]
        counter = 0
        for i in xrange(len(a)):
            if a[i] == "0":
                continue
            for j in xrange(i, len(a)):
                # strength = self.strength(a, i, j)
                strength = a[i:j + 1]
                strength = int(strength)
                if strength & (strength - 1) == 0:
                    counter += 1
        return counter

    def solve(self, cipher):
        """
        main solution function
        :param cipher: the cipher
        """

    def strength(self, a, i, j):
        # not used
        if a[i] == 0:
            return 0
        value = 0
        for k in xrange(i, j + 1):
            value = value * 10 + a[k]
        return value


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
