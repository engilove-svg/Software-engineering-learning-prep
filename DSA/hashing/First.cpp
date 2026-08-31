// Find first unique element

#include <iostream>
#include <unordered_map>
using namespace std;

int main()
{
    int arr[10] = {3, 5, 3, 8, 2, 3, 7, 5, 9, 3};
    unordered_map<int, int> temp;
    for (int i = 0; i < 10; i++)
    {
        temp[arr[i]]++;
    }

    for (int i = 0; i < 10; i++)
    {
        if (temp[arr[i]] == 1)
        {
            cout << arr[i];
            break;
        }
    }

    return 0;
}