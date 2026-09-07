#include <iostream>
using namespace std;

int main() {
    string s = "hello";
    bool count=true;
    int i = 0;
    for(int j=s.length()-1;j>i;j--){
        if(s[i]!=s[j]){
            count=false;
            break;
        }
        i++;
    }
    if(count){
        cout<<"Palindrome"<<endl;
    }
    else{
        cout<<"Not palindrome"<<endl;
    }
    return 0;
}