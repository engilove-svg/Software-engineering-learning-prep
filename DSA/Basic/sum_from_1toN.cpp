#include<iostream>
using namespace std;
int main(){
    int n;
    int i=0;
    int sum=0;
    cout<<"Enter n:"<<endl;
    cin>>n;
    while(n>i){
        i++;
        sum=sum+i;
    }
    cout<<"sum is:"<<sum<<endl;
    return 0;
}