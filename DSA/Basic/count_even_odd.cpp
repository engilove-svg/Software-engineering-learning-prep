#include <iostream>
using namespace std;
int main()
{
    int n, countOfEven = 0, countOfOdd = 0, digit;
    cout << "Enter a number" << endl;
    cin >> n;
    while (n > 0)
    {
        digit = n % 10;
        if (digit % 2 == 0)
        {
            countOfEven++;
        }
        else
        {
            countOfOdd++;
        }
        n = n / 10;
    }
    cout << " Count of even digits are: " << countOfEven << endl;
    cout << " Count of odd digits are: " << countOfOdd << endl;

    return 0;
}