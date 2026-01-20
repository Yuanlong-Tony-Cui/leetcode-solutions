function accountsMerge(accounts: string[][]): string[][] {

    // NOTE:
    // - Disjoint-set / union-find (a forest of parent pointer trees)
    //     - Each parent pointer tree has a representative (or root) node
    //     - The Find and Union operations

    const emailToRep = new Map<string, string>(); // maps an email to its representative (rep) / root
    // Emails of the same account should have a single rep.
    const emailToOwner = new Map<string, string>(); // maps an email to its owner's name

    /**
     * The Find operation. Gets the rep (or temp. rep) email of an email.
     */
    function find(email: string): string {
        const isRep = emailToRep.get(email) === email;
        if (!isRep) {
            // Make `email` point all the way to the real rep email
            // e.g. If email -> B, B -> C, C -> D, then email -> D.
            const tempRep = emailToRep.get(email);
            emailToRep.set(email, find(tempRep!));
        }
        return emailToRep.get(email)!;
    }

    /**
     * The Union operation. Merges two trees using `find()`.
     * @param email1
     * @param email2 - To be set as the source
     */
    function union(email1: string, email2: string) {
        const src1 = find(email1);
        const src2 = find(email2);
        if (src1 !== src2) {
            // Make src1 -> src2
            emailToRep.set(src1, src2);
        }
    }

    // Initialize
    for (const account of accounts) {
        const [name, ...emails] = account;
        for (const email of emails) {
            emailToRep.set(email, email); // set as the rep email of itself
            emailToOwner.set(email, name);
        }
    }

    // Union all emails at the account level
    for (const account of accounts) {
        const [name, repEmail, ...emails] = account;
        for (const email of emails) {
            union(email, repEmail);
        }
    }

    // Group emails by account
    const repToEmails = new Map<string, string[]>(); // maps the rep email to all emails of its owner
    for (const email of emailToRep.keys()) {
        const repEmail = find(email);
        if (!repToEmails.has(repEmail)) {
            repToEmails.set(repEmail, []);
        }
        repToEmails.get(repEmail)!.push(email);
    }

    // Build the result
    const result: string[][] = [];
    for (const emails of repToEmails.values()) {
        emails.sort();
        const name = emailToOwner.get(emails[0])!;
        result.push([name, ...emails]);
    }

    return result;
}
