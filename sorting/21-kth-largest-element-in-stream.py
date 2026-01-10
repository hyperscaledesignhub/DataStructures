import heapq
from typing import List
def kth_largest_element_stream(num:list[int],k:int):
    heap_arr = []
    def add_to_heap(val:int):
        """Helper method to add element to heap"""
        heapq.heappush(heap_arr,val)
        if len(heap_arr) > k:
            heapq.heappop(heap_arr)
    def add(val:int):
        add_to_heap(val)
        
    for element in num:
        add(element)
    return heap_arr[0]

print("=== Testing KthLargest (Min Heap) ===")
k = 3
nums = [4, 5, 8, 2]
kth_largest = kth_largest_element_stream(nums,3)
print(f"{k}th Largest element in {nums}is:{kth_largest}")