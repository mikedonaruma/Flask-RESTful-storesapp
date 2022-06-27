from models.user import UserModel
# this function will allow us to compare strings without worrying about char encoding, it is built into flask
import hmac

def authenticate(username, password):
    # .get is a way of accessing a dictionary. we give it a key and it will return the value
    # we set the default value to None (which we wouldnt have been able to do it we used the ['username'] notation to access the dict)
    print("the username/password received is {}/{}".format(username,password))
    user = UserModel.find_by_username(username)
    # if the user is not None (implied) and the passwords match, return user
    if user and hmac.compare_digest(user.password, password):
        return user

# take in the payload (the contents of the jwt token)
# excract the userid from the payload
def identity(payload):
    user_id = payload['identity']
    # once we have the userid from the payload, we can return the user from the user dictionary
    return UserModel.find_by_id(user_id)
