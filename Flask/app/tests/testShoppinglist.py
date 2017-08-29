""" Test Shopping List"""

import unittest



class Test_Shoppinglist(unittest.TestCase):

	def shoppinglist_exists(self):
		self.shoppinglist.shopping_list =[
			{
				'user':'njune', 'name': 'Christmas' ,'due_date':'22/12/2017'
			},
			{
			'	user':'njune', 'name': 'Anne Baby Shower', 'due_date':'4/9/2017'
			}
		]

		msg = self.shoppinglist.createList(
			"njune", "Anne Baby Shower","4/9/2017")
		self.assertEqual(msg, "The shopping list name already exists.Please try a new name")


	def test_successful_creation(self):
		self.shoppinglist.shopping_list =[
			{
				'user':'njune', 'name': 'Christmas','due_date':'22/12/2017'
			}
		]
		msg = self.shoppinglist.createList(
			"njune", "Monthly Shopping","28/9/2017")
		self.assertEqual(msg, " shopping list created")


	def test_shoppinglist_edit(self):
		self.shoppinglist.shopping_list =[
			{
				'user':'njune', 'name': 'Christmas' ,'due_date':'22/12/2017'
			},
			{
			'	user':'njune', 'name': 'Anne Baby Shower', 'due_date':'4/9/2017'
			}
		]

		msg= self.shoppinglist.editList(
			"njune", "Christmas","23/12/2017")
		self.assertEqual(msg, " shopping list edited")

	def test_delete_shoppinglist(self):
		self.shoppinglist.shopping_list=[
			{
				'user':'njune', 'name': 'Christmas' ,'due_date':'22/12/2017'
			},
			{
			'	user':'njune', 'name': 'Anne Baby Shower', 'due_date':'4/9/2017'
			},
			{
			'	user':'njune', 'name': 'Monthly Shopping', 'due_date':'28/9/2017'
			}
		]
		msg = self.shoppinglist.deleteList(
			"njune", "Christmas","23/12/2017")
		self.assertEqual(msg, " shoppinglist deleted")

if __name__ == '__main__':
	unittest.main()