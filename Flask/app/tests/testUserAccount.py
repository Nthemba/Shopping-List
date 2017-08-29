""" User Registration tests"""
import unittest




class UserTestCases(unittest.TestCase):
	"""
	Test contains tests for:
	password and cofirm password match
	Correct input given during registration and login 
	"""

	def test_mismatched_password(self):
		msg = self.user.createUser(
			"junenthemba@gmail.com","njune","Qwerty1","Qwerty")
		self.assertEqual(msg,"PasswordMismatch")

	def test_match_password(self):
		msg = self.user.createUser(
			"junenthemba@gmail.com","njune","Qwerty1","Qwerty1")
		self.assertEqual(msg,"Welcome")

	def test_user_exists(self):
		self.user.createUser(
			"junenthemba@gmail.com","njune","Qwerty1","Qwerty1")
		msg= self.user.createUser(
			"junenthemba@gmail.com","njune","Qwerty1","Qwerty1")
		self.asserEqual(msg, "User already exists")

	def test_Successful_registration(self):
		msg =self.user.createUser(
			"liamTunoe@gmail.com","ltunoe","asdrt3","asdrt3")
		self.asserEqual(msg,"Login, Registration successful")

	def test_correct_input(self):
		msg = self.user.createUser(
			"liamTunoe@gmail.com","ltunoe","asdrt3","asdrt3")
		self.asserEqual(msg,"Login, Registration successful")



	""" 
	Test Cases for User Login 
	"""


	def test_account_doesnot_exists(self):
		self .user.users=[
			{'username': 'njune', 'email':'junenthemba@gmail.com', 'password':'Qwerty1'}]
		msg= self.user.signin("Cmilka","zypks2")
		self.asserEqual(msg,"Please Create account to login")

	def test_user_exists(self):
		self .user.users=[
			{'username': 'njune', 'email':'junenthemba@gmail.com', 'password':'Qwerty1'}]
		msg= self.user.signin("njune","Qwerty1")
		self.asserEqual(msg,"Welcome, Create a new shopping list")
	

	def test_wrong_username(self):
		self.user.users =[{
		'username': 'njune', 'email':'junenthemba@gmail.com', 'password':'Qwerty1'
		}]
		msg=self.user.signin("njunr","Qwerty1")
		self.asserEqual(msg,"Wrong Username given.Please try again")

	def test_wrong_password(self):
		self.user.users =[{
		'username': 'njune', 'email':'junenthemba@gmail.com', 'password':'Qwerty1'
		}]
		msg=self.user.signin("njune","Qwerty2")
		self.asserEqual(msg,"Wrong passsword given.Please try again")


if __name__ == '__main__':
	unittest.main()