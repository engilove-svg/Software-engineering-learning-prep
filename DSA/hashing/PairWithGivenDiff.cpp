// Find two numbers whose difference is 4

#include <iostream>
#include <unordered_map>
using namespace std;

int main()
{
    int arr[7] = {5, 1, 9, 3, 7, 12, 4};
    int target = 4;

    unordered_map<int, int> temp;

    for (int i = 0; i < 7; i++)
    {
        int complement = arr[i] - target;

        if (temp.find(complement) != temp.end())
        {
            cout << "Pair Found: ";
            cout << arr[i] << " - " << complement
                 << " = " << target << endl;
            break;
        }

        if (temp.find(arr[i] + target) != temp.end())
        {
            cout << "Pair Found: ";
            cout << arr[i] + target << " - " << arr[i]
                 << " = " << target << endl;
            break;
        }

        temp[arr[i]] = i;
    }

    return 0;
}