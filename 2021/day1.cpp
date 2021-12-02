#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

vector<int> parseinput(bool test=false) {
    ifstream ipFile;
    vector<int> ip;
    int cur;

    if (test) {
        ipFile.open("day1-test.txt");
    } else {
        ipFile.open("day1-ip.txt");
    }

    while (ipFile >> cur) {
        ip.push_back(cur);
    }

    return ip;
}

int part1(bool test=false) {
    // test output should be 7
    int tot = 0;

    vector<int> ip = parseinput(test);

    for (int i = 1; i < ip.size() ; i++) {
        if (ip[i] > ip[i-1]) {
            tot++;
        }
    }

    return tot;
}

int part2(bool test=false) {
    // test output should be 5
    int tot = 0;

    vector<int> ip = parseinput(test);

    for (int i = 1; i < ip.size()-2; i++) {
        int a = ip[i-1] + ip[i] + ip[i+1];
        int b = ip[i] + ip[i+1] + ip[i+2];

        if (b > a) {
            tot++;
        }
    }

    return tot;
}


int main() {
    cout << "the solution to part 1 is: " << part1(false) << "\n";
    cout << "the solution to part 2 is: " << part2(false) << "\n";
    return 0;
}