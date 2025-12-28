function merge(intervals: number[][]): number[][] {
    // NOTE:
    // - Sort `intervals` by start time --> the current interval can only overlap with the _last_ interval in `merged`.
    // - Tradeoffs between `merged.push(intervals[i])` and `merged.push([...intervals[i]])`

    // Sort by start time
    intervals.sort((a, b) => a[0] - b[0]);

    // Merge intervals
    const merged: number[][] = [intervals[0]];
    for (let i = 1; i < intervals.length; i++) {
        const [start, end] = intervals[i];
        const [prevStart, prevEnd] = merged[merged.length - 1];
        if (prevEnd < start) { // no overlap
            merged.push(intervals[i]);
            // ^ NOTE: `merged.push([start, end])` is safer but uses more space.
        } else { // overlapping
            if (end > prevEnd) {
                // Overwrite last merged interval's end
                merged[merged.length - 1][1] = end;
            }
        }
    }

    return merged
};
