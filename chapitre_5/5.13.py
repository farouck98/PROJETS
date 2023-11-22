user_logins = {
 "alice": "12345678",
 "bob": "farouck",
 "charlie": "qwertyuiop123",
 "michael": "superP@ssword123",
}
username = input("Enter an username : ").strip().lower()
password = input("Enter a passwowd : ").strip()
if username in user_logins.keys() and password == user_logins[username]:
    print("Access granted")
else:
    print("Could not login")
