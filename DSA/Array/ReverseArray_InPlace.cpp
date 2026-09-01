#include <iostream>
using namespace std;

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6};
    int temp;
    int i=0,j=5;
    while(i<j){
        temp=arr[i];
        arr[i]=arr[j];
        arr[j]=temp;
        i++;
        j--;
    }
    for(int k=0;k<6;k++){
        cout<<arr[k]<<" ";
    }
 
    return 0;
}