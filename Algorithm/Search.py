def searchLastSmallerThan(arr, target): ### find the last number smaller than target
    lp = 0
    rp = len(arr)-1
    while lp < rp:
        mid = (lp + rp) // 2 + 1 ### trick: ensure that mid > lp
        if arr[mid] < target: ### we can not exclude arr[mid]
            lp = mid ### the answer is on the right side of mid
        else:
            rp = mid - 1
    return rp if arr[rp] < target else -1

def searchFirstGreaterThan(arr, target): ### find the last number Greater than target
    lp = 0
    rp = len(arr)-1
    while lp < rp:
        mid = (lp + rp) // 2 ### trick: ensure that mid < rp
        if arr[mid] > target: ### we can not exclude arr[mid]
            rp = mid ### the answer is on the left side of mid
        else:
            lp = mid + 1
    return rp if arr[rp] < target else -1

def searchFirstGEThan(arr, target): ### find the first number greater than or equal target
    lp = 0
    rp = len(arr)-1
    while lp <= rp:
        mid = (lp + rp) // 2
        if arr[mid] > target: ### trick
            rp = mid - 1
        elif arr[mid] < target:
            lp = mid + 1
        else: ### 如果相等就不管了
            return mid
    ### return lp 因为lp可以被+到len(arr)
    return lp ### arr[:lp] <= target, if target > max(arr) return len(arr)

def searchLastLEThan(arr, target): ### find the last number less  than or equal target
    lp = 0
    rp = len(arr)-1
    while lp <= rp:
        mid = (lp + rp) // 2
        if arr[mid] > target:
            rp = mid - 1
        elif arr[mid] < target:
            lp = mid + 1
        else: ### 如果相等就不管了
            return mid
    ### return rp 因为rp可以被-到-1
    return rp ### arr[lp:] >= target, if target > max(arr) return len(arr)

import random
def QuickSelect(arr, k):  ### quick select k-th largest
    def partition(low, high):
        if low < high:
            r = random.randint(low, high) ### avoid worst case
            arr[high], arr[r] = arr[r], arr[high]
            pivot = arr[high]
            j = low
            for i in range(low, high):
                if arr[i] < pivot:
                    arr[j], arr[i] = arr[i], arr[j] ### easy to make a mistake (write j as i) here
                    j += 1
            arr[j], arr[high] = arr[high], arr[j] 
            return j
        else:
            return low

    ### rank:  len(arr)  ... 2, 1
    ### idx:   0, 1 ... len(arr) - 2, len(arr) - 1
    def select(low, high):
        while low <= high:
            p = partition(low, high)
            if p == len(arr) - k:
                return arr[p]
            elif p < len(arr) - k:
                low = p + 1
            else:
                high = p - 1

    return select(0, len(arr) - 1)