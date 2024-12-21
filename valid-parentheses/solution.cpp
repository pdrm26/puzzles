#include <string>
#include <stack>
#include <iostream>

class Solution
{
public:
    bool isValid(std::string s)
    {
        std::stack<char> stack;

        for (char character : s)
        {
            if (character == '(' || character == '{' || character == '[')
            {
                stack.push(character);
            }
            else
            {

                if (stack.empty())
                {
                    return false;
                }

                if ((character == ')' && stack.top() == '(') || (character == '}' && stack.top() == '{') || (character == ']' && stack.top() == '['))
                {
                    stack.pop();
                }
                else
                {
                    return false;
                }
            }
        }

        return stack.empty();
    }
};

void runTest(const std::string &test_case, bool expected)
{
    Solution solution;
    bool result = solution.isValid(test_case);

    std::cout << "Test case: \"" << test_case << "\"\n";
    std::cout << "Expected: " << (expected ? "true" : "false") << "\n";
    std::cout << "Got: " << (result ? "true" : "false") << "\n";
    std::cout << (result == expected ? "PASSED" : "FAILED") << "\n\n";
}

int main()
{
    // Test cases
    runTest("()", true);     // Simple valid case
    runTest("()[]{}", true); // Multiple valid pairs
    runTest("(]", false);    // Mismatched brackets
    runTest("([)]", false);  // Interleaved brackets
    runTest("{[]}", true);   // Nested brackets
    runTest("", true);       // Empty string
    runTest("((", false);    // Unclosed brackets
    runTest("))", false);    // Extra closing brackets
    runTest("([]){}", true); // Mixed nested and sequential

    return 0;
}