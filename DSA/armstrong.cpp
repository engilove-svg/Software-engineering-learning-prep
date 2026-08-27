/*An Armstrong number is a number where the sum of each digit raised to the power of the number of digits equals the original number.*/

#include <iostream>
#include <cmath>
using namespace std;
int main()
{
    int n;
    cout << "Enter a number: " << endl;
    cin >> n;
    int count = 0, digit, power;
    int sum = 0;
    int original = n;
    int temp = n;

    while (n > 0)
    {
        digit = n % 10;
        count++;
        n = n / 10;
    }

    while (temp > 0)
    {
        digit = temp % 10;
        power = round(pow(digit, count));
        cout << "digit = " << digit << endl;
        cout << "power = " << power << endl;
        sum = sum + power;
        temp = temp / 10;
    }

    if (sum == original)
    {
        cout << "Count: " << count << endl;
        cout << "Sum: " << sum << endl;
        cout << "Original: " << original << endl;
        cout << "It is an armstrong number.";
    }
    else
    {
        cout << "Not armstrong.";
    }
    return 0;
}