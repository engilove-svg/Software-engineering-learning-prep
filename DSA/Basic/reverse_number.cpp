#include<iostream>
using namespace std;
int main() {
    int n;

    cout << "Enter a number: " << endl;
    cin >> n;
    int reverse=0;

    while (n>0) {
        int digit=n%10;//Remove the last digit
        reverse=reverse*10 + digit;//store the digits in reverse
        n=n/10;//remove the last one
    }

    cout << "Reverse of digits: " <<reverse << endl;

    return 0;
}