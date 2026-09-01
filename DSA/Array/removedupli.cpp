//given a sorted array,remove duplicates in-place.
#include <iostream>
using namespace std;

int main() {
    //two pointer pattern
   //intended pattern is sorted array + remove duplicates --> two pointers
    int arr[] = {1, 1, 2, 2, 3, 4, 4, 5};
    int i=0;   //i     j
    for(int j=1;j<8;j++){
        if(arr[j]!=arr[i]){
            i++;
            arr[i]=arr[j];
        }
    }
    for(int k=0;k<=i;k++){
        cout<<arr[k];
    }

    return 0;
}