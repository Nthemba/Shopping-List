""" Test Shopping Item"""

import unittest

def createItem(user,shopping,name,description,quantity,bought):
 	shoppingItem_list=[
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

	shopping_item_dict={}

	for s_Item in shoppingItem_list:
		if name == s_Item['name']:
			return "Item already exist.Try a new name"
		else:
			shopping_item_dict['user'] = user
			shopping_item_dict['shopping'] = shopping
			shopping_item_dict['name'] = name
			shopping_item_dict['description'] = description
			shopping_item_dict['quantity'] = quantity
			shopping_item_dict['bought'] = bought
			shoppingItem_list.append(shopping_item_dict)
			return "Shopping item created"

def editItem(user,shopping,name,description,quantity,bought):
	shoppingItem_list=[
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
	shopping_item_dict={}

	for s_Item in shoppingItem_list:
		if name == s_Item['name']:
			return "Item already exist.Try a new name"
		else:
			shopping_item_dict['user'] = user
			shopping_item_dict['shopping'] = shopping
			shopping_item_dict['name'] = name
			shopping_item_dict['description'] = description
			shopping_item_dict['quantity'] = quantity
			shopping_item_dict['bought'] = bought
			shoppingItem_list.append(shopping_item_dict)
			return "shopping item edited"

def deleteItem(user,shopping,name):
	shoppingItem_list=[
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

	for s_Item in range(len(shoppingItem_list)):
		if name == shoppingItem_list[s_Item]['name']:
			del shoppingItem_list[s_Item]
			return "shopping Item deleted"
		else:
			return "shopping Item does not exist"

class Test_Shoppingitem(unittest.TestCase):

	def shoppingitem_exists(self):
		self.assertEqual(createItem(
			"njune", "Monthly Shopping","Milk","1l","1","false"), "The shopping Item name already exists.Please try a new name")


	def test_successful_creation(self):
		self.assertEqual(createItem(
			"njune", "Monthly Shopping","Milk","1l","1","false"), "Shopping item created")


	def test_shoppingitem_edit(self):
		self.assertEqual(editItem(
			"njune", "Monthly Shopping","Soap","1kg","2","false"), "shopping item edited")

	def test_delete_shoppingitem(self):
		self.assertEqual(deleteItem(
			"njune", "Monthly Shopping","Tissue"), "shopping Item deleted")

if __name__ == '__main__':
	unittest.main()