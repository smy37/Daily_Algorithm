class Node:
    def __init__(self, char, string=None):
        self.char = char
        self.string = string
        self.children = {}

class Trie:
    def __init__(self):
        self.root = Node(None)
        self.answer = ""

    def build(self, word):
        cur = self.root

        for s in word:
            if s not in cur.children:
                cur.children[s] = Node(s)
            cur = cur.children[s]

        cur.string = word

    def find_max(self, cur_node: Node):
        for next_node in cur_node.children:
            if cur_node.children[next_node].string is not None:
                if len(cur_node.children[next_node].string) > len(self.answer):
                    self.answer = cur_node.children[next_node].string
                self.find_max(cur_node.children[next_node])


class Solution:
    def longestWord(self, wordList: list[str]) -> str:
        wordList.sort()

        trie = Trie()
        for word in wordList:
            trie.build(word)

        trie.find_max(trie.root)

        return trie.answer
        
