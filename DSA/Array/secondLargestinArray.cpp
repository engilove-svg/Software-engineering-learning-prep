#include <iostream>
using namespace std;

int main() {
    int arr[6] = {10, 25, 7, 40, 18, 30};
    int largest=arr[0];
    int secondlargest=arr[1];
    for(int i=1;i<6;i++){
        if(arr[i]>largest){
            secondlargest=largest;
            largest=arr[i];
        }
        else if (arr[i] > secondlargest){
            secondlargest=arr[i];
        }
    }
    cout << "Second largest: " << secondlargest;
    return 0;
}
/*For n elements:

Time: O(n) — one traversal
Space: O(1) — only a couple of variables*/