#include<iostream>
using namespace std;
int main(){
    int n;
    cout<<"Enter a number: "<<endl;
    cin>>n;
    int max_digit=0;
    int digit;
    while(n>0){
        digit=n%10;//extract the last digit
        if (digit>max_digit){//check if the last digit is greater than max
            max_digit=digit;//if yes,store in max
        }
        n = n / 10;//remove the last digit from n
    }
    cout<<"Largest is: "<<max_digit<<endl;
    return 0;
}
/*
🧠 The DSA pattern you just learned

This is called a "keep track of the best value so far" pattern:

if (current > best)
    best = current;

You'll see this pattern again and again in DSA—for maximum, minimum, best score, longest value, etc.*/