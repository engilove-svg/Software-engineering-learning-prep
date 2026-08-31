// Two sum problem

#include <iostream>
#include <unordered_map>
using namespace std;

int main()
{
    unordered_map<int, int> temp;
    int arr[6] = {2, 7, 11, 15, 3, 6};
    int target = 9;
    for(int i=0;i<6;i++){
        int complement=target-arr[i];
        if (temp.find(complement)!=temp.end()){//Have i seen? or does the complement already exist in the map?
            cout<<"Pair found:"<<complement<<"+"<<arr[i]<<"="<<target<<endl;
            break;
        }
        temp[arr[i]]=i;
    }

    return 0;
}