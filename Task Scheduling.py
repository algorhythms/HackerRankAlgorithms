"""
You have a long list of tasks that you need to do today. To accomplish task i, you need Mi minutes and the deadline for
this task is Di. You need not complete a task at a stretch. You can complete a part of it, switch to another task, and
then switch back.

You've realized that it might not be possible to complete all the tasks by their deadline. So you decide to do them in
such a manner that the maximum amount by which a task's completion time overshoots its deadline is minimized.

Input:
The first line contains the number of tasks T. Each of the next T lines contains two integers Di and Mi.
"""
__author__ = 'Danyang'


class Solution(object):
    def solve(self, cipher):
        """
        Small test cases pass. Sort by deadline and complete them one by one

        for complete solution: https://github.com/ningke/tasksched

        main solution function
        :param cipher: the cipher
        """
        tasks = cipher
        tasks.sort(key=lambda t: t[0])

        overshot = -1
        timer = 0
        for task in tasks:
            timer += task[1]
            overshot = max(overshot, timer - task[0])

        return overshot


if __name__ == "__main__":
    import sys

    f = open("1.in", "r")
    # f = sys.stdin
    testcases = int(f.readline().strip())
    cipher = []
    for t in xrange(testcases):
        # construct cipher
        cipher.append(map(lambda x: int(x), f.readline().strip().split(' ')))

        # solve
        s = "%s\n" % (Solution().solve(cipher))
        print s,
