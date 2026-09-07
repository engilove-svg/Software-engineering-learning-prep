#include <iostream>
using namespace std;

int main() {
    int s[]={0,1,0,3,12};
    int left=0;
    int right=4;
    while(left<right){
        if(s[left]!=0){
            left++;
        }
        else{
            int temp=s[left];
            s[left]=s[right];
            s[right]=temp;

            right--;
        }
    }
    for(int k=0;k<5;k++){
        cout<<s[k]<<" "<<endl;
    }
    return 0;
}