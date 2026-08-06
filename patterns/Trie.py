class TrieNode:
    def __init__(self):
        self.children = {}          # Map: character -> TrieNode
        self.is_end_of_word = False  # Flag to mark the end of a complete word


class Trie:
    def __init__(self):
        self.root = TrieNode()      # Empty root node

    # 1. Insert a word into the Trie
    def insert(self, word):
        current = self.root
        
        for i in range(len(word)):
            char = word[i]
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
            
        current.is_end_of_word = True

    # 2. Search for a full word
    def search(self, word):
        current = self.root
        
        for i in range(len(word)):
            char = word[i]
            if char not in current.children:
                return False
            current = current.children[char]
            
        return current.is_end_of_word

    # 3. Search for a prefix
    def starts_with(self, prefix):
        current = self.root
        
        for i in range(len(prefix)):
            char = prefix[i]
            if char not in current.children:
                return False
            current = current.children[char]
            
        return True


# ==========================================
# 🧪 Execution Example with Prints
# ==========================================

trie = Trie()

# 1. Insert Words
words_to_insert = ["cat", "car", "apple", "app"]
print("--- 1. Inserting Words ---")
for i in range(len(words_to_insert)):
    word = words_to_insert[i]
    trie.insert(word)
    print(f"Inserted: '{word}'")

# 2. Search Full Words
print("\n--- 2. Searching Full Words ---")
print("Search 'cat':", trie.search("cat"))      # Output: True
print("Search 'car':", trie.search("car"))      # Output: True
print("Search 'ca':", trie.search("ca"))        # Output: False (Prefix only, not a word)
print("Search 'dog':", trie.search("dog"))      # Output: False

# 3. Search Prefixes
print("\n--- 3. Checking Prefixes ---")
print("StartsWith 'ca':", trie.starts_with("ca"))    # Output: True
print("StartsWith 'app':", trie.starts_with("app"))  # Output: True
print("StartsWith 'do':", trie.starts_with("do"))    # Output: False    