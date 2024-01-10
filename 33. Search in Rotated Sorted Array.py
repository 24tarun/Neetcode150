class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1

        while left<=right:
            mid = (left + right) //2
            if nums[mid]==target:
                return mid

            elif nums[left]<=nums[mid]:
                #if yes we are in the left part
                if target < nums[left] or target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                #we are in the right part
                if target < nums[mid] or target > nums[right]:
                    right=mid-1
                else:
                    left = mid +1 

        return -1
