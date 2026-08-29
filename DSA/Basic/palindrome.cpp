#include<iostream>
using namespace std;
int main(){
    int n;int reverse=0;
    cout<<"Enter a number:"<<endl;
    cin>>n;
    int original=n;
    while(n>0){
        int digit=n%10;
        reverse=reverse*10+digit;
        n=n/10;
    }
    if(reverse==original){
        cout<<"Number is palindrome"<<endl;
    }
    else{
        cout<<"Not palindrome";
    }
    return 0;
}