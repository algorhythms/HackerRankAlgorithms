"""
You are given an array a of size N. The elements of the array are a[0], a[1], ... a[N-1], where each a[i] is either 0 or
 1. You can perform one transformation on the array: choose any two integers L and R, and flip all the elements between
 (and including) the Lth and Rth bits. In other words L and R represent the left-most and the right-most index
 demarcating the boundaries of the segment whose bits you will decided to flip. ('Flipping' a bit means, that a 0 is
 transformed to a 1 and a 1 is transformed to a 0.)

What is the maximum number of '1'-bits (indicated by S) which you can obtain in the final bit-string?
"""
__author__ = 'Danyang'


def bitFlip(cipher):
    """
    main solution function


    :type cipher: list
    :param cipher: the cipher
    """
    if len(cipher) <= 2:
        return len(cipher)

    cipher = [val if val == 1 else -1 for val in cipher]

    # diff = [cipher[i+1]-cipher[i] for i in xrange(len(cipher)-1)]
    maxl = 0
    maxr = -1
    min_sum = 1 << 31

    ssum = 0
    l = 0
    r = -1

    for ind, val in enumerate(cipher):
        ssum += val
        if ssum > 0:
            l = ind + 1
            r = ind
            ssum = 0

        if ssum < 0:
            r = ind

        if min_sum > ssum:
            min_sum = ssum
            maxr, maxl = r, l

    cipher = [val if val == 1 else 0 for val in cipher]
    for i in xrange(maxl, maxr + 1):
        cipher[i] ^= 1

    return sum(cipher)


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    N = int(f.readline().strip())

    cipher = []
    for t in xrange(N):
        # construct cipher
        i = int(f.readline().strip())
        cipher.append(i)
        # solve
    s = "%s\n" % (bitFlip(cipher))
    print s,
