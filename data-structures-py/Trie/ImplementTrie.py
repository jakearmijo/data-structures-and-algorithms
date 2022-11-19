# 208. Implement Trie (Prefix Tree)

# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

# Implement the Trie class:

# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

# Example 1:
# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]

# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
 

# Constraints:
# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 104 calls in total will be made to insert, search, and startsWith.


class TrieNode:
  def __init__(self) -> None:
    self.children = {}
    self.endOfWord = False

class Trie:
  def __init__(self) -> None:
    self.root = TrieNode()
  
  def insert(self, word: str) -> None:
    cur = self.root

    for c in word:
      if c not in cur.children:
        cur.children[c] = cur
      cur = cur.children[c]
    print('insert -> ', cur.endOfWord)
    cur.endOfWord = True

  def search(self, word: str) -> bool:
    cur = self.root

    for c in word:
      if c not in cur.children:
        return False
      cur = cur.children[c]
    print('search -> ', cur.endOfWord)
    return cur.endOfWord

  def startsWith(self, prefix: str) -> bool:
    cur = self.root

    for c in prefix:
      if c not in cur.children:
        print('startsWith -> False')
        return False
      cur = cur.children[c]

    print('startsWith -> True')
    return True




trie = Trie()
trie.insert("apple")
trie.search("apple")
trie.search("app")
trie.startsWith("app")
trie.insert("app")
trie.search("app")
