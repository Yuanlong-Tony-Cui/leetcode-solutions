/**
 Do not return anything, modify nums in-place instead.
 */
function sortColors(nums: number[]): void {
    // NOTE:
    // - This is a special sorting problem (Dutch national flag problem) with only three values involved.
    //   Note that to solve this problem, quick sort (O(nlogn)) is slower than the solution below.
    // - Key idea: 0s on the far left; 2s on the far right --> need to track the two indices.

    let low = 0; // next index to put 0; points to the index after the last 0
    let curr = 0; // next index to put 1; points to the curr index
    let high = nums.length - 1; // next index to put 2; points to the index before the first 2

    // Sort "unvisited" values
    while (curr <= high) {
        if (nums[curr] === 0) {
            // Swap the current 0 with an existing 1
            [nums[low], nums[curr]] = [nums[curr], nums[low]]; // NOTE: special use case of destructuring
            low += 1;
            curr += 1;
        } else if (nums[curr] === 1) {
            // (No swap needed)
            curr += 1;
        } else { // nums[curr] === 2
            // Swap the current 2 and an existing 1
            [nums[curr], nums[high]] = [nums[high], nums[curr]];
            high -= 1;
        }
    }
}
