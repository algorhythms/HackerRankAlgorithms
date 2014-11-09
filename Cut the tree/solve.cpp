/*
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
3 <= N <= 105
1 <= number written on each vertex <= 1001

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
 */

#include <algorithm>
#include <list>
#include <stack>
#include <map>
#include <string>
#include <cstdio>
#include <iostream>
#include <ostream>
#include <utility>
#include <cstring>
#include <istream>
#include <queue>
#include <set>
#include <vector>
#include <cmath>
#include <deque>
#include <limits>
#include <sstream>
#include <iterator>
using namespace std;
// #define miN(a,b) ( (a) < (b) ? (a) : (b))
int order = 0;
int N;
vector<int> data;
// vector<pair<int, int> > rls;
vector<int> visited;
vector<pair<int, int> > E;
vector<int> v_sum;
vector<vector< int> > G;


int get_sum(int i) {
    if(v_sum[i]==0) {
        visited[i] = order++;
        v_sum[i] = data[i];
        for(auto n: G[i]) {
            if(visited[n]==0)
                v_sum[i] += get_sum(n);
        }
    }
    return v_sum[i];
}
int solve() {
    int total = 0;
    for(int i=0; i<data.size(); i++)
        total += data[i];
    get_sum(0);

    int mini = 1<<31-1;
    for(auto e: E) { // auto is C11
        int u = e.first;
        int v = e.second;
        if(visited[u]>visited[v]) {
            mini = min(mini, abs(total-2*get_sum(u)) );
        }
        else {
            mini = min(mini, abs(total-2*get_sum(v)));
        }
    }

    return mini;
}
int main() {
    // freopen("out.txt","w",stdout);
    freopen("1.in","r", stdin);
    cin>>N;
    visited.resize(N);
    E.resize(N-1);
    G.resize(N);
    v_sum.resize(N);
    data.resize(N);

    for(int i=0; i<N; i++) {
        cin>>data[i];
    }

    int u, v;
    for(int i=0; i<N-1; i++) {
        cin>>u>>v;
        u--;
        v--;
        E[i] = make_pair(u, v);
        G[u].push_back(v);
        G[v].push_back(u);
    }

    int result = solve();
    cout<<result<<endl;
    return 0;
}



