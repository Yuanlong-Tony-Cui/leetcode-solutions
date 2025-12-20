// NOTE:
// - Create a custom TrieNode type that has
//   - (1) `nextChars` --> what chars come next (maps a char to a TrieNode)
//   - (2) `isEnd` --> if this char ends a word
// - We recursively check the next char by going into nested dictionaries.

// Given the word set ["apple", "app", "bat", "bath", "bad"],
// the corresponding Trie would look like this:
//
// (root)
// ├──> a
// │    └─> p
// │        └─> p (is_end = True)
// │             └─> l
// │                 └─> e (is_end = True)
// └──>b
//     ├─> a
//     │   ├─> d (is_end = True)
//     │   └─> t
//     │       └─> h (is_end = True)

class TrieNode {
    nextChars: Record<string, TrieNode> = {}; // maps each of its next chars to a TrieNode
    // NOTE: We put next chars as Record keys for faster lookup & switches.
    isEnd: boolean = false; // indicates if this char marks the end of a word seen
}

class Trie {

    // Fields
    root: TrieNode;

    // Methods
    constructor() {
        this.root = new TrieNode()
    }

    insert(word: string): void {
        let curr = this.root;
        for (const char of word) {
            // Create new if DNE
            if (!curr.nextChars[char]) {
                curr.nextChars[char] = new TrieNode();
            }
            curr = curr.nextChars[char] // proceed
        }
        curr.isEnd = true;
    }

    search(word: string): boolean {
        let curr = this.root;
        for (const char of word) {
            if (!curr.nextChars[char]) {
                return false
            }
            curr = curr.nextChars[char] // proceed
        }
        return curr.isEnd;
        // NOTE: If "apple" is stored but not "app", search("app") should return false.
    }

    startsWith(prefix: string): boolean {
        let curr = this.root;
        for (const char of prefix) {
            if (!curr.nextChars[char]) {
                return false
            }
            curr = curr.nextChars[char] // proceed
        }
        return true;
    }
}

/**
 * Your Trie object will be instantiated and called as such:
 * var obj = new Trie()
 * obj.insert(word)
 * var param_2 = obj.search(word)
 * var param_3 = obj.startsWith(prefix)
 */
