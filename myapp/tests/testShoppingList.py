""" Test Shopping List"""

import unittest
 
def createList(user,name,due_date):
 	shopping_list=[{
				'user':'njune', 'name': 'Christmas' ,'due_date':'22/12/2017'
			},
			{
			'	user':'njune', 'name': 'Anne Baby Shower', 'due_date':'4/9/2017'
			},
			{
			'	user':'njune', 'name': 'Monthly Shopping', 'due_date':'28/9/2017'
			}
	]

	shopping_list_dict={}

	for s_list in shopping_list:
		if name == s_list['name']:
			return "Shopping list already exist.Try a new name"
		else:
			shopping_list_dict['user'] = user
			shopping_list_dict['name'] = name
			shopping_list_dict['due_date'] = due_date
			shopping_list.append(shopping_list_dict)
			return "Shopping list created. Add Items to it"

def editList(user,new_name,new_due_date):
	shopping_list=[{
				'user':'njune', 'name': 'Christmas' ,'due_date':'22/12/2017'
			},
			{
			'	user':'njune', 'name': 'Anne Baby Shower', 'due_date':'4/9/2017'
			},
			{
			'	user':'njune', 'name': 'Monthly Shopping', 'due_date':'28/9/2017'
			}
	]

	shopping_list_dict={}
	for s_list in shopping_list:
		if new_name == s_list['name']:
			return "Shopping list already exist.Try a new name"
		else:
			shopping_list_dict['user'] = user
			shopping_list_dict['name'] = new_name
			shopping_list_dict['due_date'] = new_due_date
			shopping_list.append(shopping_list_dict)
			return "Shopping list edited"

def deleteList(user,l_name):
	shopping_list=[{
				'user':'njune', 'name': 'Christmas' ,'due_date':'22/12/2017'
			},
			{
			'	user':'njune', 'name': 'Anne Baby Shower', 'due_date':'4/9/2017'
			},
			{
			'	user':'njune', 'name': 'Monthly Shopping', 'due_date':'28/9/2017'
			}
	]

	for s_list in range(len(shopping_list)):
		if l_name == shopping_list[s_list]['name']:
			del shopping_list[s_list]
			return "shoppinglist deleted"
		else:
			return "shopping List does not exist"


class Test_Shoppinglist(unittest.TestCase):

	def shoppinglist_exists(self):
		self.assertEqual(createList(
			"njune", "Anne Baby Shower","4/9/2017"), "Shopping list already exist.Try a new name")


	def test_successful_creation(self):
		self.assertEqual(createList(
			"njune", "Monthly Shopping","28/9/2017"), "Shopping list created. Add Items to it")


	def test_shoppinglist_edit(self):
		self.assertEqual(editList(
			"njune", "Christmas_party","23/12/2017"), "Shopping list edited")

	def test_delete_shoppinglist(self):
		self.assertEqual(deleteList(
			"njune", "Christmas"), "shoppinglist deleted")

if __name__ == '__main__':
	unittest.main()