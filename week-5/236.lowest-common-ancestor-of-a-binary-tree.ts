/**
 * Definition for a binary tree node.
 */
class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
    }
}
 
function lowestCommonAncestor(root: TreeNode | null, p: TreeNode | null, q: TreeNode | null): TreeNode | null {
    // NOTE:
    // - We search for p or q in:
    //     - current node
    //     - left subtree
    //     - right subtree
    //   and based on these results, we update `lca` accordingly.
    // - This solution is easier to understand than the one that recursively calls lowestCommonAncestor()
    
    let lca: TreeNode | null = null;

    /**
     * Searches for p or q in a tree and updates `lca` if it can be determined.
     * @param node - The root node of the tree to search in
     */
    function nodeFoundInTree(node: TreeNode | null): boolean {
        // Base case: not found after reaching leaf nodes
        if (node === null) {
            return false;
        }

        const foundInLeft = nodeFoundInTree(node.left);
        const foundInRight = nodeFoundInTree(node.right);

        // NOTE: LCA can be updated in two broad cases as follows
        const foundAtCurr = (node === p || node === q);
        if ((foundInLeft && foundInRight) ||
            (foundAtCurr && (foundInLeft || foundInRight))
        ) {
            lca = node;
        }

        return foundInLeft || foundInRight || foundAtCurr;
    }

    nodeFoundInTree(root);
    return lca;
};
