from shoppinglist import Shoppinglist
class ShoppingItem(Shoppinglist):

	def __init__(self):
		self.shoppinglist = Shoppinglist()
		self.shoppingItem_list=[]
	"""
	returns a shopping list with a certain name
	"""
	def list_name(self,user,shopping):
		user_shopping_list = shoppinglist.listOwner()
		for shopping_list in user_shopping_list:
			if shopping == shopping_list['name']:
				self.shoppingItem_list=shopping
				return self.shoppingItem_list 


	def createItem(self,user,shopping,name,description,quantity,bought):

		shopping_item_dict={}

		for s_Item in self.shoppingItem_list:
			if name == s_Item['name']:
				return "Item already exist.Try a new name"
			else:
				shopping_item_dict['user'] = user
				shopping_item_dict['shopping'] = shopping
				shopping_item_dict['name'] = name
				shopping_item_dict['description'] = description
				shopping_item_dict['quantity'] = quantity
				shopping_item_dict['bought'] = bought
				self.shoppingItem_list.append(shopping_item_dict)
				return "Shopping item created"

	def editItem(user,shopping,name,description,quantity,bought):

		shopping_item_dict={}

		for s_Item in self.shoppingItem_list:
			if name == s_Item['name']:
				return "Item already exist.Try a new name"
			else:
				shopping_item_dict['user'] = user
				shopping_item_dict['shopping'] = shopping
				shopping_item_dict['name'] = name
				shopping_item_dict['description'] = description
				shopping_item_dict['quantity'] = quantity
				shopping_item_dict['bought'] = bought
				self.shoppingItem_list.append(shopping_item_dict)
				return "shopping item edited"

	def deleteItem(user,shopping,name):
		
		for s_Item in range(len(self,shoppingItem_list)):
			if name == self.shoppingItem_list[s_Item]['name']:
				del self.shoppingItem_list[s_Item]
				return "shopping Item deleted"
			else:
				return "shopping Item does not exist"