#include <iostream>
#include <unordered_map>
using namespace std;

int main() {
    int arr[] = {4, 2, 7, 2, 4, 2, 9};
    unordered_map<int,int>temp;
    int count=0;
    for(int i=0;i<7;i++){
       temp[arr[i]]++;
       //
    }
    for(auto pair:temp){
        cout<<pair.first<<"->"<<pair.second<<endl;
    }
    //keys must be unique and values can repeat
    return 0;
}