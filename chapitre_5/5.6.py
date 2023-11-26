allowed_users = ["Alice", "Bob", "Charlie", "Michael"]
allowed_users_lower = []
username = input("Enter your username : ").lower()

for i in allowed_users:
    allowed_users_lower.append(i.lower())
if username in allowed_users_lower:
    print("You are allowed")
else:
    print("You are not allowed : ")



