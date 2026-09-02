//Find the first number that appears twice while traversing from left to right.
#include <iostream>
#include<unordered_map>
using namespace std;

int main() {
    unordered_map<int,int>temp;
    int arr[] = {5, 3, 8, 3, 9, 5};
    for(int i=0;i<6;i++){
        if(temp.find(arr[i])!=temp.end()){
        cout<<"First repeated element is:"<<arr[i]<<endl;
        break;
        }
       temp[arr[i]]=i;
    }
    return 0;
}