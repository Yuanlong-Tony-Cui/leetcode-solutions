class TimeMap {

    // NOTE:
    // - The set() calls use **increasing** timestamps --> It automatically gives us a sorted array in ascending order --> suitable for **binary search** for a timestamp
    // - Get familiar with JS Map

    store: Map<string, {
        timestamp: number,
        value: string,
    }[]>;
    // store = {
    //     key1: [
    //         {
    //             timestamp: timestamp1
    //             value: value1
    //         },
    //         {
    //             timestamp: timestamp2
    //             value: value2
    //         }
    //     ]
    // }

    constructor() {
        this.store = new Map();
    }

    set(key: string, value: string, timestamp: number): void {
        if (!this.store.has(key)) {
            this.store.set(key, []);
        }
        this.store.get(key)!.push({
            timestamp,
            value
        });
    }

    get(key: string, timestamp: number): string {
        const records = this.store.get(key);
        if (!records) {
            return ""; // key not found
        }
        let left = 0, right = records.length - 1;
        let res = ""; // value not found by default
        while (left <= right) {
            const mid = Math.floor((left + right) / 2)
            const record = records[mid];
            if (record.timestamp === timestamp) {
                return record.value;
            } else if (record.timestamp < timestamp) {
                res = record.value; // NOTE: stores the value associated with the "smaller and closest" timestamp
                left = mid + 1; // --> `res` always gets larger
            } else { // timestamp < record.timestamp
                right = mid - 1;
            }
        }
        return res;
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * var obj = new TimeMap()
 * obj.set(key,value,timestamp)
 * var param_2 = obj.get(key,timestamp)
 */