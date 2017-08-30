""" User Registration tests"""
import unittest

def createUser(email, username, password, cPassword):
        user_list = []
        users = {}

        for user in user_list:
            if email == user['email']:
                return " User exists. Please login"
            else:
                if password == cPassword:
                    users['username'] = username
                    users['email'] = email
                    users['password'] = password
                    user_list.append(users)
                else:
                    return "Password does not match"
        return "Login, Registration successful"

class UserTestCases(unittest.TestCase):
	"""
	Test contains tests for:
	password and cofirm password match
	User already exists
	Correct input given during registration and login 
	"""

	def test_mismatched_password(self):
		res = "junenthemba@gmail.com","njune","Qwerty1","Qwerty"
		self.assertEqual(createUser("junenthemba@gmail.com","njune","Qwerty1","Qwerty"),"Password does not match")


	def test_match_password(self):
		res="junenthemba@gmail.com","njune","Qwerty1","Qwerty1"
		self.assertEqual(createUser("junenthemba@gmail.com","njune","Qwerty1","Qwerty1"),"Login, Registration successful")

	def test_user_exists(self):
		res="junenthemba@gmail.com","njune","Qwerty1","Qwerty1"
		self.assertEqual(createUser("junenthemba@gmail.com","njune","Qwerty1","Qwerty1"), "User exists. Please login")

	def test_Successful_registration(self):
		res="liamTunoe@gmail.com","ltunoe","asdrt3","asdrt3"
		self.assertEqual(createUser("liamTunoe@gmail.com","ltunoe","asdrt3","asdrt3"),"Login, Registration successful")


if __name__ == '__main__':
	unittest.main()