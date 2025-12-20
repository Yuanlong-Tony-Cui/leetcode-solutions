function coinChange(coins: number[], amount: number): number {
    // NOTE:
    // - Dynamic programming (complex solutions are built on top of simpler solutions)
    // - We build each solution using the _smallest_ coins first and progressively add larger coins.
    //   e.g. coins = [1,2,5], amount = 11:
    //       - Using only "1": 11 = 11 * "1" --> 11 coins
    //       - Using only "1" and "2": 11 = 5 * "2" + 1 * "1" --> 6 coins
    //       - Using "1", "2" and "5": 11 = 2 * "5" + 1 * "1" --> 3 coins

    // dp[amount] = dp[amount - coin] + 1, for each coin value included
    const dp = Array(amount + 1).fill(Infinity) // index range: [0, amount]
    dp[0] = 0 // no coins needed to make up 0

    // Build dp
    for (const coin of coins) { // focus on a single coin value at a time
        // Update index within range [coin, amount]
        for (let i = coin; i < amount + 1; i++) {
            dp[i] = Math.min(dp[i], dp[i - coin] + 1)
        }
    }

    return dp[amount] === Infinity ? -1 : dp[amount];
};
