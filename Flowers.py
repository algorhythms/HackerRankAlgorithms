"""
You and your K-1 friends want to buy N flowers. Flower number i has cost ci. Unfortunately the seller does not want just
 one customer to buy a lot of flowers, so he tries to change the price of flowers for customers who have already bought
 some flowers. More precisely, if a customer has already bought x flowers, he should pay (x+1)*ci dollars to buy flower
 number i.
You and your K-1 friends want to buy all N flowers in such a way that you spend the least amount of money. You can buy
the flowers in any order.

Input:

The first line of input contains two integers N and K (K <= N). The next line contains N space separated positive
integers c1,c2,...,cN.

Output:

Print the minimum amount of money you (and your friends) have to pay in order to buy all N flowers.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        Array math

        Sort the costs
        Group the costs
        :param cipher: the cipher
        """
        N, K, C = cipher

        C.sort(reverse=True)

        group_cnt = N / K + 1  # 1 is the last remaining group
        total_cost = 0
        for i in xrange(group_cnt):
            unit_cost = i + 1
            total_cost += unit_cost * sum(C[i * K:(i + 1) * K])
        return total_cost


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    N, K = map(int, f.readline().strip().split(' '))
    C = map(int, f.readline().strip().split(' '))
    cipher = N, K, C
    # solve
    s = "%s\n" % (Solution().solve(cipher))
    print s,
