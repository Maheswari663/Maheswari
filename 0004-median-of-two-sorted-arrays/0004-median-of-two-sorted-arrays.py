class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2): nums1, nums2 = nums2, nums1
        m, n, low, high = len(nums1), len(nums2), 0, len(nums1)
        half = (m + n + 1) // 2
        while low <= high:
            i = (low + high) // 2
            j = half - i
            maxL1 = nums1[i-1] if i > 0 else float('-inf')
            minR1 = nums1[i] if i < m else float('inf')
            maxL2 = nums2[j-1] if j > 0 else float('-inf')
            minR2 = nums2[j] if j < n else float('inf')
            if maxL1 <= minR2 and maxL2 <= minR1:
                if (m + n) % 2 == 1: return float(max(maxL1, maxL2))
                return (max(maxL1, maxL2) + min(minR1, minR2)) / 2.0
            elif maxL1 > minR2: high = i - 1
            else: low = i + 1