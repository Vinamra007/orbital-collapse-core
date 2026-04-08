def authenticate(username, password):
    if username == "admin" and password == "1234":
        return "[AUTH] Auth OK"
    else:
        return "[AUTH] Auth Failed"