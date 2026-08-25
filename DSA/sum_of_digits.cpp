#include<iostream>
using namespace std;
int main(){
  int n;
  cout<<"enter a number:"<<endl;
  cin>>n;
  int sum=0;
  while (n > 0){
    int digit=n % 10;//get the last digit
    sum=sum+digit;//store the last digit in sum
    n=n/10;//remove the last digit
  } 
  cout<<sum;
  return 0;
}


