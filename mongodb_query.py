import auth



def user_exist(login, password):
    user = list(auth.mongo.db.users.find({"username":login.lower(), "password":password}).limit(1))
    if user:
        return True
    else:
        return False


def create_user(login, password):
    user = list(auth.mongo.db.users.find({"username":login.lower()}).limit(1))
    if user:
        return True
    else:
        auth.mongo.db.users.insert({"username":login.lower(),"password":password})
        return True

def showAllUsers():
    users = auth.mongo.db.users.find({})
    return users


def change_pass(username, old_password, new_password):
    if user_exist(username, old_password):
        auth.mongo.db.users.update({"username":username.lower()},{"username":username.lower(),"password":new_password})
        return True
    else:
        return False

def avatar_upload(username):

    mongo.db.users.update_one({'username': session['current_user']}, {"$set":{'avatar':base64.b64encode(f.read()).decode()}})
    
