"""
You are given two positive integers a and b in binary representation. You should find the following sum modulo 10^9+7:

\sum_i=0^314159{a xor (b shl i)}
where operation xor means exclusive OR operation, operation shl means binary shift to the left.

Please note, that we consider ideal model of binary integers. That is there is infinite number of bits in each number,
and there are no disappearings (or cyclic shifts) of bits.

Input Format

The first line contains number a (1<=a<2^{10^5}) in binary representation. The second line contains number
b (1<=b<2^{10^5}) in the same format. All the numbers do not contain leading zeros.
"""
__author__ = 'Danyang'
MOD = 10 ** 9 + 7
BIT_CNT = 10 ** 5
SHIFT_CNT = 314159
# BIT_CNT = 4  # test
# SHIFT_CNT = 4  # test
N = BIT_CNT + SHIFT_CNT


class Solution(object):
    def solve(self, cipher):
        """
        algorithm: dp, bit sum
        sum of the number of 1's
        sum of the number of 0's
        treat a as mask
        scrutinize b
        :param cipher: the cipher
        """
        a, b = cipher
        len_a = len(a)
        len_b = len(b)

        # bit array
        a_array = [0 for _ in xrange(N)]
        b_array = [0 for _ in xrange(N)]

        # str to reversed bit array
        for ind, val in enumerate(a):
            a_array[len_a - 1 - ind] = int(val)
        for ind, val in enumerate(b):
            b_array[len_b - 1 - ind] = int(val)

        # dp for sum of bits
        dp = [[0, 0] for _ in xrange(N + 1)]
        for i in xrange(1, N + 1):
            dp[i][0] = dp[i - 1][0] + 1 if b_array[i - 1] == 0 else dp[i - 1][0]
            dp[i][1] = dp[i - 1][1] + 1 if b_array[i - 1] == 1 else dp[i - 1][1]

        result = 0
        sig = 1
        for i in xrange(N):  # total N bit
            if i < SHIFT_CNT:
                cnt_zero = dp[i + 1][0] + SHIFT_CNT - i  # trailing zeros
                cnt_one = dp[i + 1][1]  # no trailing ones
            else:
                cnt_zero = dp[len_b][0] - dp[i - SHIFT_CNT][0] + SHIFT_CNT  # reach-ability
                cnt_one = dp[len_b][1] - dp[i - SHIFT_CNT][1]  # reach-ability



            # xor
            cur_bit_sum = (a_array[
                               i] ^ 0) * cnt_zero  # rather than cur_bit_sum  = a_array[i]^0 * cnt_zero  # operator precedence
            cur_bit_sum += (a_array[i] ^ 1) * cnt_one

            result = (result + sig * cur_bit_sum) % MOD
            # sig *= 2  # TLE
            sig = (sig * 2) % MOD

        return result


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    a = f.readline().strip()
    b = f.readline().strip()
    cipher = (a, b)
    # solve
    s = "%s\n" % (Solution().solve(cipher))
    print s,
