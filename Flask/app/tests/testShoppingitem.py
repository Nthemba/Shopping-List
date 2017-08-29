""" Test Shopping Item"""

import unittest



class Test_Shoppingitem(unittest.TestCase):

	def shoppingitem_exists(self):
		self.shoppingitem.shoppingItem_list =[
			{
				'user':'njune', 'shopping': 'Monthly Shopping','name': 'Tissue' ,'description':'10 pc', 'quantity':'2', 'bought':'true'
			},
			{
				'user':'njune', 'shopping': 'Monthly Shopping','name': 'Soap' ,'description':'500g pc', 'quantity':'3', 'bought':'false'
			},
			{
				'user':'njune', 'shopping': 'Monthly Shopping','name': 'Milk' ,'description':'500ml pc', 'quantity':'5', 'bought':'false'
			}
		]

		msg = self.shoppingitem.createItem(
			"njune", "Monthly Shopping","Milk","1l","1","false")
		self.assertEqual(msg, "The shopping Item name already exists.Please try a new name")


	def test_successful_creation(self):
		self.shoppingitem.shoppingItem_list =[
			{
				'user':'njune', 'shopping': 'Monthly Shopping','name': 'Tissue' ,'description':'10 pc', 'quantity':'2', 'bought':'true'
			},
			{
				'user':'njune', 'shopping': 'Monthly Shopping','name': 'Soap' ,'description':'500g pc', 'quantity':'3', 'bought':'false'
			}
		]
		msg = self.shoppingitem.createItem(
			"njune", "Monthly Shopping","Milk","1l","1","false")
		self.assertEqual(msg, " shopping item created")


	def test_shoppingitem_edit(self):
		self.shoppingitem.shoppingItem_list =[
			{
				'user':'njune', 'shopping': 'Monthly Shopping','name': 'Tissue' ,'description':'10 pc', 'quantity':'2', 'bought':'true'
			},
			{
				'user':'njune', 'shopping': 'Monthly Shopping','name': 'Soap' ,'description':'500g pc', 'quantity':'3', 'bought':'false'
			}
		]

		msg= self.shoppingitem.editItem(
			"njune", "Monthly Shopping","Soap","1kg","2","false")
		self.assertEqual(msg, " shopping item edited")

	def test_delete_shoppingitem(self):
		self.shoppingitem.shoppingItem_list=[
			{
				'user':'njune', 'shopping': 'Monthly Shopping','name': 'Tissue' ,'description':'10 pc', 'quantity':'2', 'bought':'true'
			},
			{
				'user':'njune', 'shopping': 'Monthly Shopping','name': 'Soap' ,'description':'500g pc', 'quantity':'3', 'bought':'false'
			},
			{
				'user':'njune', 'shopping': 'Monthly Shopping','name': 'Milk' ,'description':'500ml pc', 'quantity':'5', 'bought':'false'
			}
		]
		msg = self.shoppingitem.deleteItem(
			"njune", "Monthly Shopping","Tissue", "10 pc","2","true")
		self.assertEqual(msg, " shopping Item deleted")

if __name__ == '__main__':
	unittest.main()