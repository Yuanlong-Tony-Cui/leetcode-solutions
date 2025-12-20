function canFinish(numCourses: number, prerequisites: number[][]): boolean {
    // NOTE:
    // - It's intuitive to build `nextCourses` and `numPrereqs` in order to take courses in sequence.
    // - Q: How do we know if we have finish all the courses? A: We track num of courses taken and compare it with `numCourses`.
    //   Note that if num of prereqs of a course never reduces to 0, this course will _never_ be taken.

    // Build graph
    const numPrereqs: number[] = Array(numCourses).fill(0); // by default, no prereqs for any course
    const nextCourses: Record<number, number[]> = {};
    for (const [course, prereq] of prerequisites) {
        if (!nextCourses[prereq]) {
            nextCourses[prereq] = [];
        }
        nextCourses[prereq].push(course);
        numPrereqs[course] += 1;
    }

    // Find courses that have no prereqs
    const coursesToTake: number[] = [];
    for (let i = 0; i < numCourses; i++) {
        if (numPrereqs[i] === 0) {
            coursesToTake.push(i);
        }
    }
    // Take courses
    let numTaken = 0;
    while (coursesToTake.length > 0) {
        const course = coursesToTake.shift();
        numTaken += 1;
        // Update for each of its next courses
        for (const nextCourse of nextCourses[course] ?? []) {
            numPrereqs[nextCourse] -= 1;
            if (numPrereqs[nextCourse] === 0) {
                coursesToTake.push(nextCourse);
            }
        }
    }

    return numTaken === numCourses ? true : false;
};
