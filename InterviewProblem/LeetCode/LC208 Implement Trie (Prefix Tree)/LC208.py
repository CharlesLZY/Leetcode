'''
Leetcode 208. Implement Trie (Prefix Tree)

Description:
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
- boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
'''

class TrieNode:
    def __init__(self):
        self.children = [None] * 26 ### 26 letters
        self.end = False ### end of the word

class Trie:

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        cur.end = True

    def search(self, word):
        cur = self.root
        for c in word:
            idx = ord(c) - ord('a')
            if not cur.children[idx]:
                return False
            cur = cur.children[idx]
        return cur.end

    def startsWith(self, prefix):
        cur = self.root
        for c in prefix:
            idx = ord(c) - ord('a')
            # If current char is not curresent
            if not cur.children[idx]:
                return False
            cur = cur.children[idx]
        return True