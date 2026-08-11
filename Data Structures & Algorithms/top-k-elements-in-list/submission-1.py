
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counts = {}
        # create empty frequency list for length + 1 size
        freq = [[] for i in range (len(nums) + 1)]

        # loop through nums
        for n in nums:
        # at every count index, update the number of duplicates, if none then set it to 0
            counts[n] = 1 + counts.get(n,0)
        
        # count is now populated, now we accessing the count hash map and populating the hashmap based on the freq and its corresponding number
        for number, count in counts.items():
            freq[count].append(number)

        result = []
        
        # looping backwards from freq - 1 to 0, because of the 0 indexing 
        for i in range(len(freq) -1, 0, -1):
            for n in freq[i]:
                result.append(n)
                if len(result) == k:
                    return result

    # The top k frequent numbers will be at the highest indices of our array because we set the index as our count, and the value inside is a list of the corresponding numbers.

# To get the answer, we need:

    # A hash map (to store the frequencies of the numbers from nums).

    # A frequency list (an array of empty buckets that we populate based on the hash map).

# Finally, loop backwards through the frequency list to grab the highest index-values (descending order) until we hit k numbers.

