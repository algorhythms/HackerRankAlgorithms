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

int solve(int n) {
	// TLE
	auto cnt = 0;
	auto m = 0;
	while(1) {
		if(cnt>=n)
			break;
		else {
			auto copy = m;
			while(copy!=0 && copy%5==0) {
				cnt++;
				copy /= 5;
			}
		}
		m += 5;
	}
	m -= 5;
	return m;
}

int main() {
    // freopen("out.txt","w",stdout);
    freopen("0.in","r", stdin);
    int N;
    cin>>N;
    for(auto i=0; i<N; i++) {
    	int n;
    	cin>>n;
    	cout<<solve(n)<<endl;
    }
    return 0;
}


