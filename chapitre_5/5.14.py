famous_citation = "I think therefore, I am."
famous_citation = famous_citation.lower()
l = []

for i in set(famous_citation):
    if famous_citation.count(i) == 1:
        l.append(i)
print(l)
