#include <iostream>
#include <fstream>
#include <vector>
#include <utility>

using namespace std;

vector<pair<string, int> > parseInput(bool test=false) {
    vector<pair<string, int> > ip;
    fstream ipFile;
    string direction;
    int value;

    if (test) {
        ipFile.open("day2-test.txt");
    } else {
        ipFile.open("day2-ip.txt");
    }

    while ( ipFile >> direction >> value ) {
        ip.push_back(make_pair(direction, value));
    }

    return ip;
}

int part1(bool test = false) {
    // test output is 150
    int depth = 0;
    int distance = 0;

    vector<pair<string, int> > ip = parseInput(test);

    for (int i = 0; i < ip.size(); i++) {
        switch (ip[i].first[0]) {
            case 'f':
                distance += ip[i].second;
                break;
            case 'u':
                depth -= ip[i].second;
                break;
            case 'd':
                depth += ip[i].second;
                break;
            default:
                break;
        }
    }

    return depth * distance;
}

int part2(bool test = false) {
    // test result: 900
    int aim = 0;
    int distance = 0;
    int depth = 0;

    vector<pair<string, int> > ip = parseInput(test);

        for (int i = 0; i < ip.size(); i++) {
        switch (ip[i].first[0]) {
            case 'f':
                distance += ip[i].second;
                depth += aim * ip[i].second;
                break;
            case 'u':
                aim -= ip[i].second;
                break;
            case 'd':
                aim += ip[i].second;
                break;
            default:
                break;
        }
    }

    return depth * distance;
}

int main() {
    cout << "part 1: " << part1(false) << "\n";
    cout << "part 2: " << part2(false) << "\n";
}