user_logins = { "Bob": "p@ssw0rd",
 "Charlie": "qwertyuiop123",
 "Michael": "superP@ssword123",
}

username = input("Enter your username : ").lower()
password = input("Enter your Password : ")

if username in user_logins and password == user_logins[username]:
    print(f"Welcome {username} ")
else:
    print("You are not welcome")

"""user_logins = {
 "alice": "12345678",
 "bob": "farouck",
 "charlie": "qwertyuiop123",
 "michael": "superP@ssword123",
}
username = input("Enter an username : ").strip().lower()
password = input("Enter a passwowd : ").strip()
if username in user_logins.keys() and password == user_logins.get(username):
    print("Access granted")
else:
    print("Could not login")"""
