word_count = int(input())
synonym_list = {}

for num in range(word_count):
    word = str(input())
    synonym = str(input())

    if word not in synonym_list:
        synonym_list[word] = []

    synonym_list[word].append(synonym)

for key, value in synonym_list.items():
    print(f"{key} - {', '.join(value)}")