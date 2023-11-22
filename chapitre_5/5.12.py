famous_citation = "I think therefore, I am."
famous_citation = famous_citation.lower()

new_dic = {}
for char in famous_citation:
    if char in new_dic:
        new_dic[char] += 1
    else:
        new_dic[char] = 1

for char in new_dic:
    print(f"there are {new_dic[char]} '{char}' in the text.")


#for i in set(famous_citation):
#    i.lower()
#    count = famous_citation.count(i)
#    if count >= 1:
#        print(f"there are {count} {i} in the text")
