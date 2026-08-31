// Find the number with highest frequency

#include <iostream>
#include <unordered_map>
using namespace std;

int main()
{
    int arr[8] = {4, 7, 2, 7, 9, 2, 7, 5};

    unordered_map<int, int> temp;

    // Step 1: Count frequency
    for (int i = 0; i < 8; i++)
    {
        temp[arr[i]]++;
    }

    // Step 2: Find highest frequency
    int maxFrequency = 0;
    int maxNumber = 0;

    for (auto pair : temp)
    {
        if (pair.second > maxFrequency)
        {
            maxFrequency = pair.second;
            maxNumber = pair.first;
        }
    }

    cout << "Number with highest frequency: " << maxNumber << endl;
    cout << "Frequency: " << maxFrequency << endl;

    return 0;
}