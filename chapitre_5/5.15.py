chars_to_remove = ".,;:!?/'"
lorem_ipsum ="""Lorem Ipsum is simply dummy text of the printing and
typesetting industry. Lorem Ipsum has been the industry's standard dummy
text ever since the 1500s, when an unknown printer took a galley of type
and scrambled it to make a type specimen book. It has survived not only
five centuries, but also the leap into electronic typesetting, remaining
essentially unchanged. It was popularised in the 1960s with the release of
Letraset sheets containing Lorem Ipsum passages, and more recently with
desktop publishing software like Aldus PageMaker including versions of
Lorem Ipsum."""

#On met d'abord le texte en minuscule
lorem_ipsum = lorem_ipsum.lower()

#ensuite on remplace les caractères à effacer par espace("")
for char in chars_to_remove:
    lorem_ipsum = lorem_ipsum.replace(char, "")

#On crée un nouveau dictionaire pour compter les mots et les y mettre
lorem_ipsum = lorem_ipsum.split()
new_dic = {}

#On compte le nombre de mots dans le texte:
for word in lorem_ipsum:
    if word in new_dic:
        new_dic[word] = new_dic[word] + 1
    else:
        new_dic[word] = 1

print(new_dic)



