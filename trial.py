from dataclasses import dataclass 


class data:
	def __init__(self,name):
		self.data = []
		self.name_class = name
	def __call__(self,dict_of_class):
		dict_class_keys = []
		for dict_class in dict_of_class.keys():
			dict_class_keys.append(dict_class)
		return dict_class_keys

if __name__ == "__main__":
	Name_Hash  = data("name_hash")
	print(Name_Hash({"hello":"Vanakkam"}))
