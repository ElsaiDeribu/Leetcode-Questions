/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    
    let l = 0
    let r = nums.length - 1
    
    
    while (l < r){
        mid = Math.floor((l + r) / 2)
        
        if (nums[mid] > nums[r]){
            l = mid + 1
        }else{
            r = mid
        }
    }
    
    let binarySearch = (l, r) => {
        
        while (l + 1 < r){
            mid = Math.floor((l + r) / 2)
            
            if (nums[mid] <= target){
                l = mid
            }else{
                r = mid
            }
        }
        return l 
    } 
     
    let leftRes = binarySearch(0, r)
    let rightRes = binarySearch(r, nums.length)
    
    if (nums[leftRes] === target){
        return leftRes
    }
    
    if (nums[rightRes] === target){
        return rightRes
    }
    
    return -1
    
};