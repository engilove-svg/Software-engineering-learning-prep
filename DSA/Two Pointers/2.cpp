//move zeroes
#include <iostream>
using namespace std;

int main() {
    int arr[] = {0, 1, 0, 3, 12};
    int i=0;
    for(int j=1;j<5;j++){
        if(arr[j]!=0){
            arr[i]=arr[j];
            i++;
        }
    }
    while(i<5){
        arr[i]=0;
        i++;
    }

    for(int k=0;k<5;k++){
        cout<<arr[k]<<endl;
    }
    return 0;
}