famous_citation = "I think therefore, I am."
for i in set(famous_citation):
    if famous_citation.count(i) == 1:
        print(f"There is {famous_citation.count(i)} {i} in the text")