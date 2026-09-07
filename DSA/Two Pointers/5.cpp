#include <iostream>
using namespace std;

int main() {
    int arr[]={1,2,3,4,6,8,11};
    int target=10;
    int left=0;
    int right=6;
    int sum=0;
    bool found=false;
    while(left < right){
        sum=arr[left]+arr[right];    
        if(sum==target){
            found=true;
            break;
        }
        else if(sum<target){
            left++;
        }
        else{
            right--;
        }
    }
    if(found){
        cout<<"Sum is : "<<arr[left]<<"+"<<arr[right]<<"="<<target<<endl;
    }else{
        cout<<"Not found";
    }

    return 0;
}