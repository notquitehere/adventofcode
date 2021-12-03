#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

vector<string> parseInput(bool test=false) {
    fstream ipFile;
    string val;
    vector<string> ip;

    test ? ipFile.open("day3-test.txt") : ipFile.open("day3-ip.txt");

    while (ipFile >> val) {
        ip.push_back(val);
    }

    return ip;
}

int part1(bool test=false) {
    // test op 198
    vector<string> ip = parseInput(test);
    string gamma, epsilon;

    for (int i = 0; i < ip[0].size(); i++) {
        int zeros = 0;
        int ones = 0;

        for (int j = 0; j < ip.size(); j++) {
            if (ip[j][i] == '0') {
                zeros += 1;
            } else {
                ones += 1;
            }
        }

        gamma += zeros > ones ? "0" : "1";
        epsilon += zeros < ones ? "0" : "1";
    }

    return stoi(gamma, nullptr, 2) * stoi(epsilon, nullptr, 2);
}

int main() {
    cout << "Part 1 solution: " << part1(false) << "\n"; 
}