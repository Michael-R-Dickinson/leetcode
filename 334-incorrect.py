import math
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        def find_index(arr, cond):
            return next((i for i, x in enumerate(arr) if cond(x)), None)

        triplets = [nums[0]]
        for n in nums:
            beat_idx = find_index(triplets, lambda x: n > x)
            print(beat_idx, triplets)
            if (beat_idx != None):
                print (f'inserting at pos {beat_idx}: {n}')
                triplets.insert(beat_idx, n)
                if (len(triplets) >= 3):
                    return True

        return False
