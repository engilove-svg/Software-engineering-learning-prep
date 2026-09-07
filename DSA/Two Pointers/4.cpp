#include <iostream>
using namespace std;

int main() {
    int arr[]={1, 2, 3, 4, 6, 8, 11};
    int target=10;
    int i=0;
    for(int j=1;j<7;j++){
        if(arr[i]+arr[j]==target){
            cout<<"Target found: "<<arr[i]<<"+"<<arr[j]<<endl;
            break;
        }
        i++;
    }
    return 0;
}