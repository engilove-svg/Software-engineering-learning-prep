// Find whether there are two numbers whose sum equals the target.
//  2 pointer approach
// given  a sorted array

#include <iostream>
using namespace std;

int main()
{
    int arr[] = {2, 2, 3, 4, 6, 8, 9};
    //   i                 j

    int target = 10;
    int i = 0, j = 6;
    //Two pointers require repeated checking → use a while loop.
while(i<j){
    if (arr[i] + arr[j] == target)
    {
        cout << arr[i] << "+" << arr[j] << "=" << target << endl;
        break;
    }
    else if (arr[i]+arr[j]>target){
         j--;
    }
    else{
        i++;
    }
}
    return 0;
}