// Find the first element that appears more than once.

#include <iostream>
#include <unordered_map>
using namespace std;

int main()
{
    int arr[7] = {4, 7, 2, 7, 9, 2, 5};
    unordered_map<int, int> temp;
    for (int i = 0; i < 7; i++)
    {
        temp[arr[i]]++; // frequency count
        if (temp[arr[i]] == 2)
        {
            cout << (arr[i]);
            break;
        }
    }

    return 0;
}