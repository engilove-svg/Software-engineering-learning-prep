#include <iostream>
#include <unordered_map>
using namespace std;

int main()
{
    int arr[] = {4, 7, 2, 7, 9, 4, 7, 2};
    unordered_map<int, int> temp;
    for (int i = 0; i < 8; i++)
    {
        temp[arr[i]]++;
    }
    int mostFrequent = arr[0];
    int maxFrequency = temp[arr[0]];
    for (int i = 0; i < 8; i++)
    {
        if (maxFrequency < temp[arr[i]])
        {
            maxFrequency = temp[arr[i]];
            mostFrequent = arr[i];
        }
    }
    cout << "Most frequent: " << mostFrequent << endl;
    cout << "Frequency: " << maxFrequency << endl;
    return 0;
}