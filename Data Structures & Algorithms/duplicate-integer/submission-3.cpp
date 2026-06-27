class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> output;
        for (int key : nums) {
            // Try to insert it. If it fails (returns false), we found a duplicate!
            if (output.insert(key).second == false) {
                return true;
            }
        }
        return false;
    }
};