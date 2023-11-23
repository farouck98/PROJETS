def is_user_banned(username: str, authorized_users: set) -> bool:
    return username in is_user_banned
"""
    Vérifie dans la base si  l'utilisateur  est autorisé à se connecter,
    
    Arg:
        username(string): le nom de l'utilisateur qui essaie de se connecter
        authorized_users (set): Ensemble des utilisateurs autorisés à se connecter
    return:
    bool : est-ce que l'utilisateur est autorisé à se connecter

"""