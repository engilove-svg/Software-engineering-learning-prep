#include <iostream>
using namespace std;

int main() {
    int arr[7] = {2, 5, 2, 8, 2, 5, 9};
    int target=2;
    int count=0;
    for(int i=0;i<7;i++){
        if(arr[i]==target){
            count++;
        }   
    }
    cout<<target<<" appears "<<count<<" times ";
    return 0;
}