'''
### Prefix Sum 前缀和
sum(nums[i:j]) = sum(nums[:j]) - sum(nums[:i]) = prefix[j] - prefix[i]

### 差分数组
差分数组的主要适用场景是频繁对原始数组的某个区间的元素进行加减。
diff[0] = nums[0]
diff[i] = nums[i] - nums[i-1] 
The original array nums can be retrieved from difference array.

If we want to add x to nums[i:j], we only need to update diff[i] += x and diff[j+1] -= x
diff[i] += x equals to adding x for nums[i:]
diff[j+1] -= x equals to substracting x for nums[j:]
'''


