
""" user.py """
"""
Functions for user to register and login
"""

class User(object):

    def __init__(self):

        self.user_list = []

    def createUser(self, email, username, password, cPassword):
        
        users = {}

        for user in self.user_list:
            if email == user['email']:
                return " User exists. Please login"
            else:
                if password == cPassword:
                    users['email'] = email
                    users['username'] = username
                    users['password'] = password
                    self.user_list.append(users)
                else:
                    return "Password does not match"
        return "Login, Registration successful"

    def signin(self, username, password):
        for user in self.user_list:
            if username == user['username']:
                if password == user['password']:
                    return "Welcome, Create a new shopping list"
                else:
                    return "Wrong credentials.Please try again"
        return "Please Create account to login"
