#include <iostream>
#include <unordered_map>
using namespace std;

int main()
{
    int arr[] = {1, 2, 3, 2, 4, 1, 5};
    unordered_map<int, int> temp;
    for (int i = 0; i < 7; i++)
    {
        temp[arr[i]]++; // frequrency count
    }
    for (int i = 0; i < 7; i++)
    {
        if (temp[arr[i]] == 1)
        {
            cout << "First unique number: " << arr[i];
            break;
        }
    }

    return 0;
}