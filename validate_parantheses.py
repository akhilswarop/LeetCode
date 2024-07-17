def longestConsecutive(nums):
    maxCount = 0
    tempCount = 0
    res = list(set(nums))
    for i in range(0,len(res)-1):
        if i == (len(res) - 1):
            return max(tempCount,maxCount)
        elif res[i+1] - res[i] == 1:
            tempCount += 1
            continue
        maxCount = max(tempCount,maxCount)
        tempCount = 0
    return maxCount
longestConsecutive([0,3,2,5,4,6,1,1])