// Another two sum
#include <iostream>
#include <unordered_map>
using namespace std;

int main()
{
    int arr[7] = {4, 6, 1, 9, 3, 7, 2};
    int target = 10;
    unordered_map<int,int>temp;
    for(int i=0;i<7;i++){
        int complement=target-arr[i];
        if(temp.find(complement)!=temp.end()){
            cout<<"Pair found: "<<complement<<"+"<<arr[i]<<"="<<target<<endl;
            break;
        }
        temp[arr[i]]=i;
    }

    return 0;
}