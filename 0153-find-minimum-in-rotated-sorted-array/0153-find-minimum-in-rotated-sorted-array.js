/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    
    let l = -1
    let r = nums.length - 1
    
    while (l + 1 < r){
        mid = Math.floor( (l + r) / 2)
        
        if (nums[mid] >= nums[0]){
            l = mid
        }
        else{
            r = mid
        }
    }
    
    return Math.min(nums[r], nums[0])
    
};