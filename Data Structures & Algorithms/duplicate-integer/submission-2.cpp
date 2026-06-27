class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> output;
        for (int key : nums) {
            if (output.count(key)) {
                return true;
            }
            output.insert(key);
        }
        return false;
    }
};