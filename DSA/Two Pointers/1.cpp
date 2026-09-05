//Remove duplicates from a sorted array

#include <iostream>
using namespace std;

int main() {
    int arr[] = {1, 1, 2, 2, 3, 4, 4};
    //           i  j
    int i=0;
    for(int j=1;j<7;j++){
        if(arr[i]!=arr[j]){
            i++;
            arr[i]=arr[j];
        }
    }
    for(int k=0;k<i+1;k++){
        cout<<arr[k]<<endl;

    }
    return 0;
}