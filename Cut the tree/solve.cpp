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
#define SHOW_A(x) {cout << #x << ": " << x << endl;}
using namespace std;
int order = 0;
int N;
vector<int> data;
// vector<pair<int, int> > rls;
vector<int> visited;
vector<pair<int, int> > E;
vector<int> v_sum;
vector<vector< int> > G;


int get_sum(int i) {
    // SHOW_A(i);
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
    for(auto d: data)
        total += d;
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



