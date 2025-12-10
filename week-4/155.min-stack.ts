class MinStack {

    // NOTE:
    // - To be able to retrieve the min value _in constant time_,
    //   we will need to store the min value for _every index_ on the stack.

    stack: number[];
    mins: number[]; // stores min values
    // NOTE: `stack` and `min` will always have the same length

    constructor() {
        this.stack = []
        this.mins = []
    }

    push(val: number): void {
        this.stack.push(val);
        // Check if new value becomes the new min value
        if (this.mins.length === 0) {
            this.mins.push(val)
        } else {
            this.mins.push(Math.min(val, this.mins.at(-1)))
        }
    }

    pop(): void {
        this.stack.pop()
        this.mins.pop()
    }

    top(): number {
        return this.stack.at(-1)
    }

    getMin(): number {
        return this.mins.at(-1)
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */