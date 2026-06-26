class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // Map stores: <number_value, array_index>
        unordered_map<int, int> indices; 
        
        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            
            // 1. Check if the complement (diff) already exists in our map
            if (indices.find(diff) != indices.end()) {
                // We found a match! Return the index of the diff, and current index 'i'
                return {indices[diff], i};
            }
            
            // 2. If not found, add the current number and its index to the map
            indices[nums[i]] = i;
        }
        
        // Fallback return (the problem guarantees exactly one solution will exist)
        return {};
    }
};