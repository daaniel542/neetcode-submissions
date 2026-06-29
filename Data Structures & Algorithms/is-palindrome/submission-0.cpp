class Solution {
public:
    bool isPalindrome(string s) {
        int i = 0;
        int j = s.length() - 1;

        while (i < j) {
            // Skip non-alphanumeric characters from the left
            while (i < j && !std::isalnum(s[i])) {
                i++;
            }
            // Skip non-alphanumeric characters from the right
            while (i < j && !std::isalnum(s[j])) {
                j--;
            }
            
            // Compare the valid characters
            if (std::toupper(s[i]) != std::toupper(s[j])) {
                return false;
            }
           
            // Move pointers inward for the next check
            i++;
            j--;
        }
        return true;
    }
};