class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m_map = Counter(nums)
        
        return heapq.nlargest(k, m_map, key=m_map.get)
        