function search(nums: number[], target: number): number {
    // NOTE: 
    // - O(log n) means binary search.
    // - The solution is built on top of the classic binary search solution with handling of "array rotation":
    //   If `nums` is "left rotated" (assuming the left half is the fully sorted half) and
    //   `target` was originally on the left half, `target` might end up being rotated to the right half
    //   --> We search the left half only when `nums[left] < target < nums[mid]`.

    let left = 0, right = nums.length - 1;
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (target === nums[mid]) {
            return mid;
        }

        // Two cases: the left half / the right half is fully sorted
        // Two subcases: target is on the fully-sorted half / the other half
        if (nums[left] <= nums[mid]) { // if the left half is fully sorted
        // NOTE: ^ Include `=` for the case where `mid` is `left`.
            if (nums[left] <= target && target < nums[mid]) {
                right = mid - 1;
            } else { // e.g. target < nums[left] --> `target` has been rotated to the right half
                left = mid + 1;
            }
        } else { // if the right half is fully sorted
            if (nums[mid] < target && target <= nums[right]) {
                left = mid + 1;
            } else { // e.g. nums[right] < target --> `target` is still on the left half
                right = mid - 1;
            }
        }
    }
    return -1; // not found
};
