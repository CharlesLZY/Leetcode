
def searchFirstGreaterThan(arr, idx): ### find first number greater than idx
    lp = 0
    rp = len(arr)-1
    while lp <= rp:
        mid = (lp + rp) // 2
        if arr[mid] > idx: ### trick
            rp = mid - 1
        elif arr[mid] < idx:
            lp = mid + 1
        else:
            return mid
    ### return lp 因为lp可以被+到len(arr)
    return lp ### arr[:lp] <= idx, if idx > max(arr) return len(arr)

def searchFirstLessThan(arr, idx): ### find first number less than idx
    lp = 0
    rp = len(arr)-1
    while lp <= rp:
        mid = (lp + rp) // 2
        if arr[mid] > idx:
            rp = mid - 1
        elif arr[mid] < idx:
            lp = mid + 1
        else:
            return mid
    ### return rp 因为rp可以被-到len(arr)
    return rp ### arr[lp:] >= idx, if idx > max(arr) return len(arr)

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