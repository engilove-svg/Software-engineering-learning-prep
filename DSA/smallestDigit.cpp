#include<iostream>
using namespace std;
int main(){
    int n,min_digit=9,digit;
    cout<<"Enter a number: "<<endl;
    cin>>n;
    while(n>0){
        digit=n%10;
        if(digit<min_digit){
            min_digit=digit;
        }
        n=n/10;
    }
    cout<<"Smallest digit is:"<<min_digit<<endl;
    return 0;
}