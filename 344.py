import math


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        def find_index(arr, cond):
            return next((i for i, x in enumerate(arr) if cond(x)), None)

        triplets = [float("inf"), float("inf"), float("inf")]
        for n in nums:
            beat_idx = find_index(triplets, lambda x: n < x)
            print(beat_idx, triplets)
            if beat_idx != None:
                print(f"inserting at pos {beat_idx}: {n}")
                triplets[beat_idx] = n

        if all([t != float("inf") for t in triplets]):
            return True
        return False
