function productExceptSelf(nums: number[]): number[] {

    // NOTE:
    // - Forward pass (prefix product) + backward pass (products[i] * suffix product) --> still O(n)
    // - Initialize variables to _identity elements_ so that they automatically change to the other operand itself
    //   and we wouldn't need to handle those special cases using if-else.
    //     - e.g. For multiplication (*), 1 is the identity element since 1 * M = M, 1 * N = N, etc.

    const n = nums.length;
    const products = Array(n).fill(1); // initialized to 1 (identity element for multiplication)

    // Forward pass
    let prefixProduct = nums[0];
    for (let i = 1; i < n; i++) {
        products[i] = prefixProduct;
        prefixProduct *= nums[i]; // update
    }

    // Backward pass
    let suffixProduct = nums[n - 1];
    for (let i = n - 2; i >= 0; i--) {
        products[i] *= suffixProduct;
        suffixProduct *= nums[i]; // update
    }

    return products;
};
