def aggressiveCows(stalls, k):    
    def check(stalls, k, mid):
        cow = 1
        prev = stalls[0]
        
        for i in range(1, len(stalls)):
            if stalls[i] - prev >= mid:
                cow += 1
                prev = stalls[i]
            if cow == k:
                return True
        return False
            
        
        
    stalls.sort()
    low = 1
    high = stalls[-1] - stalls[0]
    result = 0
    while low <= high:
        mid = (low + high) // 2
        if check(stalls, k, mid):
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    return result

stalls = [1, 2, 4, 8, 9]
k = 3
print(aggressiveCows(stalls, k))