#include <iostream>
#include <unordered_map>
using namespace std;

int main()
{
    unordered_map<int, int> students;
    // unordered_map<key_type, value_type> name;
    students[101] = 85;
    students[102] = 92;
    students[103] = 78;

    cout << students[102];

    return 0;
}