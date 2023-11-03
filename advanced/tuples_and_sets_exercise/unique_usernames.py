username_num = int(input())
unique_usernames = set()
for username in range(username_num):
    unique_usernames.add(input())


print("\n".join(unique_usernames))