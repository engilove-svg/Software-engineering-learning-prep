#include <iostream>
#include <unordered_map>
using namespace std;

int main()
{
    int arr[7] = {3, 8, 4, 2, 7, 5, 1};
    int target = 9;
    unordered_map<int, int> container;
    for (int i = 0; i < 7; i++)
    {
        int sum = target - arr[i];
        if (container.find(sum) != container.end())
        {
            cout << "pair found: " << container[sum] << " " << i;
            break;
        }

        container[arr[i]] = i;
    }

    return 0;
}
