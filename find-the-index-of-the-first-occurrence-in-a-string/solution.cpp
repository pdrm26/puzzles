#include <string>
#include <iostream>

class Solution
{
public:
    int strStr(std::string haystack, std::string needle)
    {
        std::int8_t index = 0;

        while (index < haystack.size())
        {
            std::string haystack_substr = haystack.substr(index, needle.size());

            if (needle == haystack_substr)
            {
                return index;
            }

            index++;
        }

        return -1;
    }
};

int main()
{
    std::string haystack = "leetcodeleeto";
    std::string needle = "leeto";
    Solution solution;
    int index = solution.strStr(haystack, needle);

    if (index != -1)
    {
        return index;
    }

    return -1;
};