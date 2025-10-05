import heapq
from typing import List

class KthLargest:
    """
    This class finds the kth largest element in a stream of numbers.
    It uses a min-heap to efficiently keep track of the k largest elements seen so far.
    """
    def __init__(self, k: int, nums: List[int]):
        """
        Initializes the object with the integer k and the initial stream of numbers.
        
        Args:
            k (int): The 'k' for the kth largest element.
            nums (List[int]): The initial list of numbers.
        """
        self.k = k
        self.heap = []
        # Process the initial numbers to build the heap
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        """
        Adds a new number to the stream and returns the current kth largest element.
        
        Args:
            val (int): The new number to add.
            
        Returns:
            int: The current kth largest element after adding val.
        """
        # If the heap isn't full yet, just add the new element.
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        # If the new value is larger than the smallest element in our heap (the root),
        # replace the smallest element with the new one.
        elif val > self.heap[0]:
            # heapreplace is more efficient than a separate pop and push
            heapq.heapreplace(self.heap, val)
        
        # The root of our min-heap is always the kth largest element
        return self.heap[0]

# --- Example Usage ---
# Let's run through the example from the explanation.

# 1. Initialize: KthLargest(3, [4, 5, 8, 2])
kth_largest = KthLargest(3, [4, 5, 8, 2]) 
# After initialization, the heap contains the 3 largest elements from the list: [4, 5, 8].
# The root is 4, so the 3rd largest is 4.
print(f"Initial 3rd largest: {kth_largest.heap[0]}")  # Expected: 4

# 2. Add 3: add(3)
result = kth_largest.add(3)
# 3 is not > 4, so the heap is unchanged.
print(f"After adding 3, the 3rd largest is: {result}") # Expected: 4

# 3. Add 5: add(5)
result = kth_largest.add(5)
# 5 is > 4, so 4 is replaced with 5. The heap becomes [5, 5, 8]. The new root is 5.
print(f"After adding 5, the 3rd largest is: {result}") # Expected: 5

# 4. Add 10: add(10)
result = kth_largest.add(10)
# 10 is > 5, so 5 is replaced with 10. The heap becomes [5, 10, 8]. After sifting, it's [8, 10, 5].
print(f"After adding 10, the 3rd largest is: {result}") # Expected: 8

# 5. Add 9: add(9)
result = kth_largest.add(9)
# 9 is > 8, so 8 is replaced with 9. The heap becomes [9, 10, 5]. After sifting, it's [9, 10, 5].
print(f"After adding 9, the 3rd largest is: {result}") # Expected: 9


