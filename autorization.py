import json


def user_exist(login, password):
    store = open("secretdata.txt", "r")
    secretdata = json.load(store)
    store.close()
    try:
        if secretdata[login] == password:
            return True
    except KeyError:
        return False


def create_user(login, password):
    store = open("secretdata.txt", "r")
    secretdata = json.load(store)
    store.close()
    try:
        if secretdata[login]:
            return False
    except KeyError:
        secretdata[login] = password
        store = open("secretdata.txt", "w")
        json.dump(secretdata, store)
        store.close()
        return True

def showAllUsers():
    store = open("secretdata.txt", "r")
    secretdata = json.load(store)
    store.close()
    output = ''
    for user, password in secretdata:
        output += user + ' ' + password + "<br>"
    return output
