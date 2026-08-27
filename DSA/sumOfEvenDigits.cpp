#include<iostream>
using namespace std;
int main(){
    int n;
    cout<<"Enter a number: "<<endl;
    cin>>n;
    int sum=0;
    while(n>0){
        int digit=n%10;
        if (digit%2==0){
            sum+=digit; //accumulator pattern 
        }
        n=n/10;
    }
    cout<<"Sum of even digits is:"<<sum<<endl;
    return 0;
}
/*⭐ What you now know

You've combined three DSA concepts:

1. Extract a digit

digit = n % 10;

2. Check a condition

digit % 2 == 0

3. Maintain an answer

sum += digit;

That third one is especially important. You'll see this accumulator pattern constantly in DSA.*/