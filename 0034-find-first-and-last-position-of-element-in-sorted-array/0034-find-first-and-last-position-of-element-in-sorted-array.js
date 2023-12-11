/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
    
    if (nums.length == 0){
        return [-1, -1]
    }
    
    let l = 0
    let r = nums.length
    
    let right = -1
    let left = -1
    
    
    while (l + 1 < r){
        
        mid = Math.floor((l + r) / 2)
        
        if (nums[mid] <= target){
            l = mid
        }
        else{
            r = mid
        } 
    }
    
    if (nums[l] == target){
        right = l
    }
    
    l = -1
    r = nums.length - 1
    
    while (l + 1 < r){
        mid = Math.floor((l + r) / 2)
        
        if (nums[mid] >= target){
            r = mid
        }
        else{
            l = mid
        }
    }
    
    if (nums[r] == target){
        left = r
    }
    
    return [left, right]
    
    
};