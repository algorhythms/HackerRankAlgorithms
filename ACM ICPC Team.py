"""
You are given a list of N people who are attending ACM-ICPC World Finals. Each of them are either well versed in a topic
or they are not. Find out the maximum number of topics a 2-person team can know. And also find out how many teams can
know that maximum number of topics.

Input Format

The first line contains two integers N and M separated by a single space, where N represents the number of people, and M
 represents the number of topics. N lines follow.
Each line contains a binary string of length M. In this string, 1 indicates that the ith person knows a particular
topic, and 0 indicates that the ith person does not know the topic. Here, 1 <= i <= 2, and it denotes one of the persons
in the team
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        bit manipulation
        brute force O(N^2*M)
        :param cipher: the cipher
        """
        N, M, ppl = cipher
        team_cnt = 0
        max_topic = 0
        for i in xrange(N):
            for j in xrange(i + 1, N):
                cnt = self.common_topics(M, ppl[i], ppl[j])
                if cnt == max_topic:
                    team_cnt += 1
                elif cnt > max_topic:
                    team_cnt = 1
                    max_topic = cnt
        return "%d\n%d" % (max_topic, team_cnt)

    def common_topics(self, M, a, b):
        topic = a | b
        topic_cnt = bin(topic).count("1")  # otherwise TLE
        # topic_cnt = 0
        # for i in xrange(M):
        # if topic&0x1==0x1:
        #         topic_cnt += 1
        #     topic >>= 1
        return topic_cnt


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    N, M = map(lambda x: int(x), f.readline().strip().split(" "))
    ppl = []
    for i in xrange(N):
        ppl.append(int(f.readline().strip(), 2))

    cipher = [N, M, ppl]
    s = "%s\n" % (Solution().solve(cipher))
    print s,
