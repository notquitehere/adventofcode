#include <iostream>
#include <vector>
#include <fstream>
#include <utility>

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

vector<string> recursive(vector<string> ip, string ltgt, int iter) {
    vector<string> output;
    char filter;
    int zeros = 0;
    int ones = 0;

    if ( ip.size() == 1 ) {
        return ip;
    } else {
        for (int i = 0; i < ip.size(); i++) {
            if (ip[i][iter] == '0') {
                zeros += 1;
            } else {
                ones += 1;
            }
        }

        if (ltgt == "greater") {
            filter = zeros > ones ? '0' : '1';
        } else if (ltgt == "smaller") {
            filter = zeros <= ones ? '0' : '1';
        }

        for ( int i = 0; i < ip.size(); i++ ) {
            if (ip[i][iter] == filter) {
                output.push_back(ip[i]);
            }
        }

        return recursive(output, ltgt, iter+1);
    }
} 

int part2(bool test=false) {
    // test solution gamma = 10111
    // test solution epsilon = 01010
    // final solution = 230
    vector<string> ip = parseInput(test);
    sort(ip.begin(), ip.end());
    
    string gamma = recursive(ip, "greater", 0)[0];
    string epsilon = recursive(ip, "smaller", 0)[0];

    return stoi(gamma, nullptr, 2) * stoi(epsilon, nullptr, 2);
}

int main() {
    cout << "Part 1 solution: " << part1(false) << "\n"; 
    cout << "Part 2 solution: " << part2(false) << "\n";
}