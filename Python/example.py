import pickle

class Animal:
	def __init__(self, name, species):
		self.name = name
		self.species = species

	def __repr__(self):
		return f'{self.name} is a {self.species}'

	def make_sound(self, sound):
		print(f'this animal says {sound}')

class Cat(Animal):
	def __init__(self, nzme, breed, toy):
		super().__init__(name, species = 'Cat')
		self.breed = breed
		self.toy = toy

	def play(self):
		print(f'{self.name} plays with {self.toy}')


blue = Cat('Blue', 'Scottish Fold', 'String')

#with open('pets.pickle', 'wb') as file:  #Pickling - makes file binary
#	pickle.dump(blue, file)


with open('pets.pickle' 'rb') as file:
	print(pickle.load(file))
	print(pickle.load(file).play())

	#Returns 
	#Blue is a cat
	#Blue plays with String
	#None

