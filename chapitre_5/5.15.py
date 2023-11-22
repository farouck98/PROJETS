
lorem_ipsum = """Lorem Ipsum is simply dummy text of the printing and
typesetting industry. Lorem Ipsum has been the industry's standard dummy
text ever since the 1500s, when an unknown printer took a galley of type
and scrambled it to make a type specimen book. It has survived not only
five centuries, but also the leap into electronic typesetting, remaining
essentially unchanged. It was popularised in the 1960s with the release of
Letraset sheets containing Lorem Ipsum passages, and more recently with
desktop publishing software like Aldus PageMaker including versions of
Lorem Ipsum."""
lorem_ipsum = lorem_ipsum.lower()
chars_to_remove = ".,;:!?/'"

for char in chars_to_remove:
    lorem_ipsum = lorem_ipsum.replace(char," ")

new_dic = {}
list_word = lorem_ipsum.split()

for word in list_word:
    if word in new_dic:
        new_dic[word] = new_dic[word] + 1
    else:
        new_dic[word] = 1

print(new_dic)





