/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function isValidBST(root: TreeNode | null): boolean {
    
    // NOTE:
    // - An incorrect solution would simply see if `left.val < val < right.val` to validate, which will fail for [5, 4, 6, null, null, 3, 7]. This is because although 3 < 6 < 7, the node at "3" should be within (5, 6).
    // - We instead validate each node by seeing if its value falls in a (low, high) range.

    function validateNode(node: TreeNode | null, min: number, max: number): boolean {
        if (node === null) {
            return true;
        }
        return (
            min < node.val && node.val < max && // within range (min, max)
            validateNode(node.left, min, node.val) && // updates max
            validateNode(node.right, node.val, max) // updates min
        ); // short-circuit evaluation
    }

    return validateNode(root, Number.NEGATIVE_INFINITY, Number.POSITIVE_INFINITY);
};
