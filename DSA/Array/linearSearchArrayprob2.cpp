#include <iostream>
using namespace std;
int main()
{
    int arr[5] = {10, 25, 7, 40, 18};
    int target = 40;
    int i = 0;
    bool found=false;
    for (i = 0; i < 5; i++)
    {
        if (arr[i] == target)
        {
            cout << "Target found at index: " << i;
            found=true;
            break;
        }
    }
    if (found==false){
        cout<<"Not found";
    }
    return 0;
}