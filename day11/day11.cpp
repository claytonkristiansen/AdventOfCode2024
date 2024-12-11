#include <iostream>
#include <vector>
#include <cmath>
#include <future>

using std::cout;
using std::vector;
using std::floor;
using std::log10;
using std::pow;

#define NUM_BLINKS 75

void ApplyBlink(vector<long long> &stones)
{
    vector<long long> newStones;
    for (long long stone : stones)
    {
        if (stone == 0)
        {
            newStones.push_back(1);
        }
        else
        {
            long numDigits = floor(log10(stone)) + 1;
            if (numDigits % 2 == 0)
            {
                long long topHalf = stone / pow(10, (numDigits / 2));
                long long bottomHalf = stone - (topHalf * pow(10, (numDigits / 2)));
                newStones.push_back(topHalf);
                newStones.push_back(bottomHalf);
            }
            else
            {
                newStones.push_back(stone * 2024);
            }
        }
    }

    stones = newStones;
}

long long ApplyBlinkRec(long long stone, int depth)
{
    if (depth >= NUM_BLINKS)
    {
        return 1;
    }

    if (stone == 0)
    {
        return ApplyBlinkRec(1, depth + 1);
    }

    long numDigits = floor(log10(stone)) + 1;
    if (numDigits % 2 == 0)
    {
        long long topHalf = stone / pow(10, (numDigits / 2));
        long long bottomHalf = stone - (topHalf * pow(10, (numDigits / 2)));

        // auto topHalfFuture = std::async(std::launch::async, ApplyBlinkRec, topHalf, depth + 1);
        // auto bottomHalfFuture = std::async(std::launch::async, ApplyBlinkRec, bottomHalf, depth + 1);
        // return topHalfFuture.get() + bottomHalfFuture.get();

        return ApplyBlinkRec(topHalf, depth + 1) + ApplyBlinkRec(bottomHalf, depth + 1);
    }

    return ApplyBlinkRec(stone * 2024, depth + 1);
}

int main(void)
{
    vector<long long> stones = {6571, 0, 5851763, 526746, 23, 69822, 9, 989};
    // vector<int> stones = {125, 17};

    long totalStones = 0;

    vector<std::future<long long>> futures;

    for (long long stone : stones)
    {
        futures.push_back(std::async(std::launch::async, ApplyBlinkRec, stone, 0));
    }

    cout << "Initial threads started\n";

    for (int i = 0; i < stones.size(); ++i)
    {
        totalStones += futures[i].get();
    }

    cout << totalStones << "\n";


    // for (int i = 0; i < 75; ++i)
    // {
    //     ApplyBlink(stones);
    //     cout << stones.size() << "\n";
    // }

    return 0;
}
