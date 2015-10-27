__author__ = 'Danyang'
import logging
import sys


class Solution(object):
    @property
    def logger(self):
        lgr = logging.getLogger(__name__)
        lgr.setLevel(logging.CRITICAL)
        if not lgr.handlers:
            ch = logging.StreamHandler(sys.stdout)
            ch.setLevel(logging.DEBUG)
            ch.setFormatter(logging.Formatter('%(levelname)s - %(message)s'))
            lgr.addHandler(ch)
        return lgr

    def solve(self, cipher):
        """
        bfs

        attention to the usage of unvisited array
        :param cipher: the cipher
        """
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        M, N, matrix, K = cipher

        start = None
        end = None
        for i in xrange(M):
            for j in xrange(N):
                if matrix[i][j] == "M":
                    start = (i, j)
                elif matrix[i][j] == "*":
                    end = (i, j)

        pi = [[None for _ in xrange(N)] for _ in xrange(M)]
        visited = [[False for _ in xrange(N)] for _ in xrange(M)]

        visited[start[0]][start[1]] = True
        q = [start]
        ended = False
        while q and not ended:
            l = len(q)
            for i in xrange(l):
                cur = q[i]
                for dir in dirs:
                    r = cur[0] + dir[0]
                    c = cur[1] + dir[1]
                    if 0 <= r < M and 0 <= c < N and not visited[r][c]:
                        visited[r][c] = True
                        if matrix[r][c] in (".", "*"):
                            pi[r][c] = cur
                            q.append((r, c))
                        if matrix[r][c] == "*":
                            ended = True
            q = q[l:]

        if not ended:
            return "not found"

        path = [end]
        cur = end
        while cur != start:
            cur = pi[cur[0]][cur[1]]
            path.append(cur)

        path.reverse()
        self.logger.debug(str(path))
        cnt = 0
        visited = [[False for _ in xrange(N)] for _ in xrange(M)]
        for cur in path[:-1]:
            dir_cnt = 0
            visited[cur[0]][cur[1]] = True
            for dir in dirs:
                r = cur[0] + dir[0]
                c = cur[1] + dir[1]
                if 0 <= r < M and 0 <= c < N:
                    if matrix[r][c] in (".", "*") and not visited[r][c]:
                        dir_cnt += 1
            if dir_cnt > 1:
                cnt += 1
                self.logger.debug("Wand@" + str(cur))
            if cnt > K:
                return "Oops!"

        self.logger.debug("cnt: %d, K: %d" % (cnt, K))
        if cnt == K:  # exactly K times
            return "Impressed"
        else:
            return "Oops!"


if __name__ == "__main__":
    f = open("1.in", "r")
    # f = sys.stdin
    testcases = int(f.readline().strip())

    for t in xrange(testcases):
        # construct cipher
        M, N = map(int, f.readline().strip().split(' '))
        matrix = []
        for _ in xrange(M):
            matrix.append(list(f.readline().strip()))
        K = int(f.readline().strip())
        cipher = M, N, matrix, K

        # solve
        s = "%s\n" % (Solution().solve(cipher))
        print s,
