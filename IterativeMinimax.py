#include<bits/stdc++.h>
using namespace std;

int left(int i){
	return (i*2)+1;
}
int right(int i){
	return (i*2)+2;
}

int main()
{
    vector<int> leafs{3,5,2,9,12,5,23,23};
    int n = leafs.size();
    vector<int> tree;

    int height = 1,OH=1;
    bool max = true;

    for(int i=0;i<(2*n-1)-n;i++){
    	if(max){
    		tree.push_back(-10000);
    		height--;
    	}else if(!max){
    		tree.push_back(10000);
    		height--;
    	}

    	if(height == 0){
    		height = OH*2;
    		OH = height;
    		max = !max;
    	}
    }
    for(auto elm : leafs){
    	tree.push_back(elm);
    }

	int beg = (tree.size()-n)/2, end = tree.size()-n;
	for(int i=beg;i<end and i!=0;i++){
		if(tree[i]<0){
			if(tree[left(i)] > tree[right(i)]){
				tree[i] = tree[left(i)];
			}else tree[i] = tree[right(i)];
		}else{
			if(tree[left(i)] < tree[right(i)]){
				tree[i] = tree[left(i)];
			}else tree[i] = tree[right(i)];
		}
		if(i == end-1){
			end = beg;
			i = (beg/2)-1;
			beg = i;
		}
	}
	tree[left(0)] > tree[right(0)] ? tree[0] = tree[left(0)] : tree[0] = tree[right(0)];

    cout<<"Your Optimal Value is: "<<tree[0];
    return 0;
}
