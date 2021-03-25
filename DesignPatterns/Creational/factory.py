class Dog:

	def __init__(self, name):
		self.name = name

	def speak(self):
		return "Woof!!"


class Cat:

	def __init__(self, name):
		self.name = name

	def speak(self):
		return "Meow!!"


def getPet(pet="dog"):
	'''
	The factory method
	'''

	pets = dict(dog=Dog('Kento'), cat=Cat('Goofy'))
	return pets.get(pet, None)


d, c = getPet('dog'), getPet('cat')
print(d.speak(), c.speak(), sep='\n')

