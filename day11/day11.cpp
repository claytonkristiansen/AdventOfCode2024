#include <iostream>
#include <vector>
#include <cmath>
#include <future>
#include <unordered_map>
#include <string>
#include <stack>
#include <stdlib.h>

using std::cout;
using std::vector;
using std::unordered_map;
using std::pair;
using std::floor;
using std::log10;
using std::pow;
using std::stack;

#define NUM_BLINKS 75
#define memo_t unordered_map<uint64_t, pair<uint64_t, uint64_t>>

uint64_t Blink(unordered_map<uint64_t, uint64_t> stonesMap, int numBlinks)
{
    uint64_t numStones = 0;
    memo_t memoizationList;

    for (int i = 0; i < NUM_BLINKS; ++i)
    {
        unordered_map<uint64_t, uint64_t> newMap;

        auto it = stonesMap.begin();
        while (it != stonesMap.end())
        {
            if (it->first == 0)
            {
                auto itNew = newMap.find(1);
                if (itNew != newMap.end())
                {
                    itNew->second += it->second;
                }
                else
                {
                    newMap.insert({1, it->second});
                }
                it++;
                continue;
            }

            /* If entry exists (left hand side will have a non-zero value if an entry exists at all) */
            auto itMemo = memoizationList.find(it->first);
            if (itMemo != memoizationList.end())
            {
                auto itNew = newMap.find(itMemo->second.first);
                if (itNew != newMap.end())
                {
                    itNew->second += it->second;
                }
                else
                {
                    newMap.insert({itMemo->second.first, it->second});
                }
                itNew = newMap.find(itMemo->second.second);
                if (itNew != newMap.end())
                {
                    itNew->second += it->second;
                }
                else
                {
                    newMap.insert({itMemo->second.second, it->second});
                }
                it++;
                continue;
            }

            long numDigits = floor(log10(it->first)) + 1;
            if (numDigits % 2 == 0)
            {
                uint64_t topHalf = it->first / pow(10, (numDigits / 2));
                uint64_t bottomHalf = it->first - (topHalf * pow(10, (numDigits / 2)));

                memoizationList.insert({it->first, {topHalf, bottomHalf}});
                // cout << stone.second << "\n";

                auto itNew = newMap.find(topHalf);
                if (itNew != newMap.end())
                {
                    itNew->second += it->second;
                }
                else
                {
                    newMap.insert({topHalf, it->second});
                }
                itNew = newMap.find(bottomHalf);
                if (itNew != newMap.end())
                {
                    itNew->second += it->second;
                }
                else
                {
                    newMap.insert({bottomHalf, it->second});
                }
                it++;
                continue;
            }

            uint64_t newInt = it->first * 2024;

            auto itNew = newMap.find(newInt);
            if (itNew != newMap.end())
            {
                itNew->second += it->second;
            }
            else
            {
                newMap.insert({newInt, it->second});
            }
            it++;
        }
        stonesMap = newMap;
    }

    for (auto stone : stonesMap)
    {
        numStones += stone.second;
    }

    return numStones;
}

int ApplyBlinkRec(uint64_t stone, memo_t *memoizationList, int depth)
{
    if (depth >= NUM_BLINKS)
    {
        return 1;
    }

    if (stone == 0)
    {
        return ApplyBlinkRec(1, memoizationList, depth + 1);
    }

    /* If entry exists (left hand side will have a non-zero value if an entry exists at all) */
    auto it = memoizationList->find(stone);
    if (it != memoizationList->end())
    {
        return ApplyBlinkRec(it->second.first, memoizationList, depth + 1)
               + ApplyBlinkRec(it->second.second, memoizationList, depth + 1);
    }

    long numDigits = floor(log10(stone)) + 1;
    if (numDigits % 2 == 0)
    {
        uint64_t topHalf = stone / pow(10, (numDigits / 2));
        uint64_t bottomHalf = stone - (topHalf * pow(10, (numDigits / 2)));

        memoizationList->insert({stone, {topHalf, bottomHalf}});
        cout << stone << "\n";

        // auto topHalfFuture = std::async(std::launch::async, ApplyBlinkRec, topHalf, depth + 1);
        // auto bottomHalfFuture = std::async(std::launch::async, ApplyBlinkRec, bottomHalf, depth + 1);
        // return topHalfFuture.get() + bottomHalfFuture.get();

        return ApplyBlinkRec(topHalf, memoizationList, depth + 1)
               + ApplyBlinkRec(bottomHalf, memoizationList, depth + 1);
    }

    return ApplyBlinkRec(stone * 2024, memoizationList, depth + 1);
}

int main(int argc, char **argv)
{
    int numBlinks = NUM_BLINKS;
    if (argc > 1)
    {
        numBlinks = std::atoi(argv[1]);
    }
    vector<uint64_t> stonesVec = {6571, 0, 5851763, 526746, 23, 69822, 9, 989};
    unordered_map<uint64_t, uint64_t> stones = {{6571, 1},
                                                {0, 1},
                                                {5851763, 1},
                                                {526746, 1},
                                                {23, 1},
                                                {69822, 1},
                                                {9, 1},
                                                {989, 1}};
    // vector<uint64_t> stones = {125, 17};

    uint64_t numStones = Blink(stones, numBlinks);
    cout << "Num Stones: " << numStones << "\n";


    /* My failed attempt at brute forcing through multi-threading :) */
    // /* Memoization list for split operations below MEMO_SIZE */
    // vector<memo_t *> memoizationListList;

    // int totalStones = 0;

    // vector<std::future<int>> futures;

    // for (uint64_t stone : stones)
    // {
    //     memo_t *memoizationList = new memo_t;
    //     memoizationListList.push_back(memoizationList);
    //     futures.push_back(std::async(std::launch::async, ApplyBlinkRec, stone, memoizationList, 0));
    // }

    // cout << "Initial threads started\n";

    // for (int i = 0; i < stones.size(); ++i)
    // {
    //     totalStones += futures[i].get();
    // }

    // cout << totalStones << "\n";

    // /* Free all heap memory */
    // for (auto list : memoizationListList)
    // {
    //     delete list;
    // }

    // for (int i = 0; i < 75; ++i)
    // {
    //     ApplyBlink(stones);
    //     cout << stones.size() << "\n";
    // }

    return 0;
}
