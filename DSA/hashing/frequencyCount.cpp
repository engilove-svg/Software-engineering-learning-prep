#include <iostream>
#include<unordered_map>
using namespace std;

int main() {
    int arr[7] = {2, 5, 2, 8, 2, 5, 9};
    unordered_map<int,int> temp;
    for(int i=0;i<7;i++){
       temp[arr[i]]++;//frequency count
    }
    for(auto pair:temp){
        cout<<pair.first<<":"<<pair.second<<endl;
    }
    return 0;
}