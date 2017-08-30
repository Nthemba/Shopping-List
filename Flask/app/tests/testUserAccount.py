""" User Registration tests"""
import unittest
       
def createUser(email, username, password, cPassword):
	user_list =[{
		'email':'junenthemba@gmail.com','username': 'njune', 'password':'Qwerty1'
	}]
        users = {}

        for user in user_list:
            if email == user['email']:
                return " User exists. Please login"
            else:
                if password == cPassword:
                	users['email'] = email
                	users['username'] = username
                	users['password'] = password
                	user_list.append(users)
                else:
                    return "Password does not match"
        return "Login, Registration successful"

def signin(username, password):
	user_list =[{
		'email':'junenthemba@gmail.com', 'username': 'njune', 'password':'Qwerty1'
		}]
        for user in user_list:
            if username == user['username']:
                if password == user['password']:
                    return "Welcome, Create a new shopping list"
                else:
                    return "Wrong credentials.Please try again"
        return "Please Create account to login"

class UserTestCases(unittest.TestCase):
	"""
	Test contains tests for:
	password and cofirm password match
	User already exists
	Correct input given during registration and login 
	# # """
	
	def test_mismatched_password(self):
		self.assertEqual(createUser("liamTunoe@gmail.com","liam","Qwerty1","Qwe"),"Password does not match")

	def test_match_password(self):
		self.assertEqual(createUser("robertson@gmail.com","roba","asdfg","asdfg"),"Login, Registration successful")

	def test_user_exists(self):
	 	self.assertEqual(createUser("junenthemba@gmail.com","njune","Qwerty1","Qwerty1"), "User exists. Please login")

	def test_Successful_registration(self):
		self.assertEqual(createUser("norlan@gmail.com","nolan","asdrt3","asdrt3"),"Login, Registration successful")



# TestCases for login

	def test_account_doesnot_exists(self):
		self.user_list =[{
		'username': 'njune', 'email':'junenthemba@gmail.com', 'password':'Qwerty1'
		}]
		self.assertEqual(signin("Cmilka","zypks2"),"Please Create account to login")

	def test_user_exists(self):
		self.user_list =[{
		'username': 'njune', 'email':'junenthemba@gmail.com', 'password':'Qwerty1'
		}]
		self.assertEqual(signin("njune","Qwerty1"),"Welcome, Create a new shopping list")

	def test_wrong_password(self):
		self.user_list =[{
		'username': 'njune', 'email':'junenthemba@gmail.com', 'password':'Qwerty1'
		}]
		self.assertEqual(signin("njune","Qwerty2"),"Wrong credentials.Please try again")



if __name__ == '__main__':
	unittest.main()