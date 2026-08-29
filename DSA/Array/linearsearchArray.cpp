#include<iostream>
using namespace std;
int main(){
    int arr[5] = {10, 25, 7, 40, 18};
    int target=25;
    bool found=false;
    for (int i=0;i<5;i++){
        if (arr[i]==target){
             found=true;
             break;
        }
    }
    if (found){
        cout<<"Found";
    }
    else{
        cout<<"Not found";
    }
    return 0;
}
/*🧠 Complexity

For an array of n elements:

Time: O(n)
Space: O(1)

Why O(n)?

Because in the worst case, we may have to check every element.
*/