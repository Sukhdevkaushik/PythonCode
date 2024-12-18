def MaxArea(height):
    left = 0
    right = len(height) - 1
    maxarea = 0
    while(left < right):
         
        width = right - left
        _height = min(height[right], height[left])
        current_area =  _height * width
        maxarea = max(maxarea, current_area)

        if height[left] > height[right]:
            right -= 1
        else:
            left += 1
    return maxarea

    

height = [1,8,6,2,5,4,8,3,7]
print(MaxArea(height))