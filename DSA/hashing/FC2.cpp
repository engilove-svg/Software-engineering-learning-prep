#include <iostream>
#include <unordered_map>
using namespace std;

int main()
{
    int arr[8] = {10, 20, 10, 30, 20, 40, 10, 50};
    unordered_map<int, int> temp;
    int target;
    cout << "Enter target: ";
    cin >> target;
    for (int i = 0; i < 8; i++)
    {
        temp[arr[i]]++;
        
    }
    cout << target << " appears " << temp[target] << endl; // temp[key]--value

    return 0;
}