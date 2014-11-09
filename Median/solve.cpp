/**
 * Some errors
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
long long N;
// by default cpp is max-heap, while python is min-heap
vector<long long> left_heap; // max-heap
vector<long long> right_heap; // min-heap

void balance(vector<long long>& left, vector<long long>& right) {
	if(left.size()>right.size()+1) {
//		cout<<"balance left"<<endl;
		long long head = left.front();

		pop_heap(left.begin(), left.end()); // swap to last
		left.pop_back();

		right.push_back(-head);
		push_heap(right.begin(), right.end());
	}
	else if(right.size()>left.size()+1) {
//		cout<<"balance right"<<endl;
		long long head = right.front();

		pop_heap(right.begin(), right.end());
		right.pop_back();

		left.push_back(-head);
		push_heap(left.begin(), left.end());
	}
	// balance(left, right);
}

double get_median(vector<long long> left, vector<long long> right) {
	if(left.size()==right.size())
		return 0.5*(left.front()-right.front());
	else if(left.size()>right.size()) {
		return left.front();
	}
	else {
		return -right.front();
	}
}

string solve(char op, long long val) {
	if(op=='r') {
		try {
			if(left_heap.size()>0 && val<=left_heap.front()) {
				auto i = 0;
				while(i<left_heap.size() && left_heap[i]!=val) i++;
				if(i==left_heap.size())
					throw 1;
				left_heap.erase(left_heap.begin()+i);
				make_heap(left_heap.begin(), left_heap.end());
			}
			else {
				auto i = 0;
				while(i<right_heap.size() && right_heap[i]!=-val) i++;
				if(i==right_heap.size())
					throw 2;
				right_heap.erase(right_heap.begin()+i);
				make_heap(right_heap.begin(), right_heap.end());
			}

			if(left_heap.size()<=0 && right_heap.size()<=0) {
				return "Wrong!";
			}
		}
		catch(int e) {
			return "Wrong!";
		}
	}
	else {
		if(left_heap.size()>0 && val>=left_heap.front()) {
			left_heap.push_back(val);
			push_heap(left_heap.begin(), left_heap.end());
		}
		else {
			right_heap.push_back(-val);
			push_heap(right_heap.begin(), right_heap.end());
		}
	}
	balance(left_heap, right_heap);

//	cout<<"left: ";
//	for(auto e: left_heap)
//		cout<<-e<<" ";
//	cout<<endl;
//	cout<<"right: ";
//	for(auto e: right_heap)
//		cout<<e<<" ";
//	cout<<endl;

	auto result = get_median(left_heap, right_heap);
	stringstream ss;
	ss<<result;

	return ss.str();
}

int main() {
    // freopen("out.txt","w",stdout);
    freopen("0.in","r", stdin);
    cin>>N;
    char op;
    long long val;
    for(auto i=0; i<N; i++) {
    	cin>>op;
    	cin>>val;
    	cout<<solve(op, val)<<endl;
    	// TODO, some errors
    }
    return 0;
}



