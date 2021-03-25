class Korean:
	def __init__(self):
		self.name = 'Korean'

	def speakKorean(self):
		return "An-neyong?"

class British:
	def __init__(self):
		self.name = "British"

	def speakEnglish(self):
		return "Hello"


class Adapter:
	def __init__(self, object, **adaptedMethod):
		self.object = object
		self.__dict__.update(adaptedMethod)

	def __getattr__(self, attr):
		return getattr(self, object, attr)


k = Korean()
b = British()

objects = []
objects.append(Adapter(k, speak=k.speakKorean))
objects.append(Adapter(b, speak.b.speakEnglish))

for obj in objects:
	print(f'{obj.name()} says {obj.speak()}')
