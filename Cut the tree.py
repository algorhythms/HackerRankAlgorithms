# -*- coding: utf-8 -*-
"""
Atul is into graph theory, and he is learning about trees nowadays. He observed that the removal of an edge from a given
tree T will result in formation of two separate trees T1 and T2.

Each vertex of the tree T is assigned a positive integer. Your task is to remove an edge, such that, the *Tree_diff* of
the resultant trees is minimized. *Tree_diff* is defined as

 F(T) = Sum of numbers written on each vertex of a Tree T
 Tree_diff(T) = abs(F(T1) - F(T2))
Input Format
The first line will contain an integer N, i.e., the number of vertices in the tree.
The next line will contain N integers separated by a single space, i.e., the values assigned to each of the vertices.
The next (N-1) lines contain pair of integers separated by a single space and denote the edges of the tree.
In the above input, the vertices are numbered from 1 to N.

Output Format
A single line containing the minimum value of *Tree_diff*.

Constraints
3 ≤ N ≤ 105
1 ≤ number written on each vertex ≤ 1001

Sample Input

6
100 200 100 500 100 600
1 2
2 3
2 5
4 5
5 6
Sample Output

400
"""
__author__ = 'Danyang'


class TreeNode(object):
    def __init__(self, item):
        self.item = item
        self.tree_sum = None
        self.left = None
        self.right = None

    def __repr__(self):
        return repr(self.item)


class Solution_error(object):
    def solve(self, cipher):
        """
        it should be graph theory rather than tree

        bought test case #5
        :param cipher: the cipher
        """
        root = self.construct_tree(cipher)
        total = self.get_tree_sum(root)
        mini = [1 << 32]  # primitive is pass by value thus put it into array
        self.dfs(root, total, mini)
        return mini[0]

    def dfs(self, root, total, mini):
        """
        pre-order
        """
        if not root:
            return

        mini[0] = min(mini[0], abs(total - root.tree_sum - root.tree_sum))
        self.dfs(root.left, total, mini)
        self.dfs(root.right, total, mini)


    def construct_tree(self, cipher):
        """
        Hard part, the connection not necessarily from parent to child
        errors may occur here due to the edge
        """
        N, nodes, rls = cipher
        lst = [TreeNode(val) for val in nodes]
        # rls.sort(key=lambda x: x[1])  # secondary
        # rls.sort(key=lambda x: x[0])
        rls = map(lambda x: [x[0] - 1, x[1] - 1], rls)
        linked_set = {0}
        for r in rls:
            if r[0] in linked_set:
                parent = r[0]
                child = r[1]
            else:
                parent = r[1]
                child = r[0]

            linked_set.add(child)
            if not lst[parent].left:
                lst[parent].left = lst[child]
            else:
                lst[parent].right = lst[child]

        return lst[0]

    def get_tree_sum(self, root):
        """

        :type root: TreeNode
        """
        if not root.tree_sum:
            left_sum = self.get_tree_sum(root.left) if root.left else 0
            right_sum = self.get_tree_sum(root.right) if root.right else 0
            root.tree_sum = left_sum + right_sum + root.item

        return root.tree_sum


#
# class GraphNode(object):
#     def __init__(self, data):
#         self.neighbors = []
#         self.data = -1

class Solution(object):
    def __init__(self):
        self.order = 0

    def __inc_order(self):
        self.order += 1
        return self.order

    def solve(self, cipher):
        """
        https://github.com/pankajmore/DPP/blob/master/hackerrank/w2/cut-the-tree.cpp

        graph
        dfs
        use order count to present preserve the tree structure information
        combination of graph and tree
        :param cipher: the cipher
        """
        N, data, rls = cipher

        # pure index representation without GraphNode strut
        visited = [-1 for _ in xrange(N)]  # visited order
        E = [(0, 0) for _ in xrange(N - 1)]
        G = [[] for _ in xrange(N)]
        v_sum = [-1 for _ in xrange(N)]  # in tree order
        _sum = sum(data)

        # construct graph
        for ind, r in enumerate(rls):
            u = r[0] - 1
            v = r[1] - 1

            G[u].append(v)
            G[v].append(u)

            E[ind] = (u, v)

        # dfs
        # def dfs(s):
        #     visited[s] = self.__inc_order()
        #     v_sum[s] = data[s]
        #     for n in G[s]:
        #         if visited[n]==-1: # otherwise, already visited, which means parent.
        #
        #             v_sum[s] += dfs(n)
        #     return v_sum[s]

        # lazy recursive dp
        # problem:  RuntimeError: maximum recursion depth exceeded
        def get_sum(s):
            if v_sum[s] == -1:
                visited[s] = self.__inc_order()
                v_sum[s] = data[s]
                for n in G[s]:  # dfs
                    if visited[n] == -1:
                        v_sum[s] += get_sum(n)
            return v_sum[s]

        get_sum(0)

        mini = 1 << 32
        for e in E:
            u, v = e
            if visited[u] > visited[v]:  # if smaller, the node is in the middle of subtree
                mini = min(mini, abs(_sum - get_sum(u) - get_sum(u)))
            else:
                mini = min(mini, abs(_sum - get_sum(v) - get_sum(v)))
        return mini


if __name__ == "__main__":
    import sys

    sys.setrecursionlimit(100000)  # otherwise not enough, stack problem with python
    # print sys.getrecursionlimit()
    f = open("1.in", "r")
    # f = sys.stdin
    N = int(f.readline().strip())
    nodes = map(int, f.readline().strip().split(' '))
    rls = []
    for t in xrange(N - 1):
        # construct rls
        rls.append(map(int, f.readline().strip().split(' ')))
    cipher = N, nodes, rls
    s = "%s\n" % (Solution().solve(cipher))
    print s,
