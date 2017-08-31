class Shoppinglist(object):

	def __init__(self):
		self.shopping_list = []
		self.user_shopping_list=[]
	"""
	list of shopping lists owned by a specific user
	"""
	def listOwner(self,user):
		for user_list in self.shopping_list:
			if user == user_list['user']:
				self.user_shopping_list.append(user_list)				
				return user_shopping_list

	"""
	Create Shopping list function
	"""
	def createList(self,user,name,due_date):

		shopping_list_dict={}

		user_lists= self.listOwner(user)
		for s_list in user_lists:
			if name == s_list['name']:
				return "Shopping list already exist.Try a new name"
			else:
				shopping_list_dict['user'] = user
				shopping_list_dict['name'] = name
				shopping_list_dict['due_date'] = due_date
				user_lists.append(shopping_list_dict)
				return "Shopping list created. Add Items to it"

	"""
	edit shopping list Function
	"""		

	def editList(self,user,new_name,new_due_date):

		user_lists= self.listOwner(user)

		for s_list in user_lists:
			if new_name == s_list['name']:
				return "Shopping list already exist.Try a new name"
			else:
				shopping_list_dict['user'] = user
				shopping_list_dict['name'] = new_name
				shopping_list_dict['due_date'] = new_due_date
				user_lists.append(shopping_list_dict)
				return "Shopping list edited"

	"""
	Delete Shopping LIst
	"""

	def deleteList(user,l_name):

		user_lists= self.listOwner(user)

		for s_list in range(len(user_lists)):
			if l_name == self.user_lists[s_list]['name']:
				del self.user_lists[s_list]
			return "shoppinglist deleted"
		else:
			return "shopping List does not exist"
