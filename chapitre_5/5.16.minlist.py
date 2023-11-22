l = [5, 1, 3, -2, 8]

list_trie = []

for i in l.copy():
    list_trie.append(min(l))
    l.remove(min(l))
print(list_trie)