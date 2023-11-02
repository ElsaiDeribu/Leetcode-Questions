/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
        
        
//         def dfs(node):
//             if not node:
//                 return 0, 0, 0
            
//             left = dfs(node.left)
//             right = dfs(node.right)
            
//             resl, suml, cntl = left
//             resr, sumr, cntr = right
            
//             res = resl + resr
//             sumt = suml + sumr + node.val
//             cntt = cntl + cntr + 1
            
//             mean = sumt // cntt 
            
//             if mean == node.val:
//                 res += 1
                
//             return res, sumt, cntt
        
        
//         return dfs(root)[0]



var averageOfSubtree = function(root) {
    
    function dfs(node){
        if (node == null){
            return [0, 0, 0]
        }
        let left = dfs(node.left)
        let right = dfs(node.right)
        
        
        let [resl, suml, cntl] = left
        let [resr, sumr, cntr] = right
        
        
        let res = resl + resr;
        let sumt = suml + sumr + node.val;
        let cntt = cntl + cntr + 1;
        
        let mean = Math.floor(sumt / cntt)
        
        if (mean === node.val){
            res += 1
        }
        
        return [res, sumt, cntt]
        
    }
    
    return dfs(root)[0]

    
};