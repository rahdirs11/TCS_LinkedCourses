class Subject(object):
	def __init__(self):
		self._observers = []

	def attach(self, observer):
		if observer not in self._observers:
			self._observers.append(observer)

	def detach(self, observer):
		if observer in self._observers:
			self._observers.remove(observer)

	def notify(self, modifier=None):
		for observer in self._observers:
			if modifier != observer:
				observer.update(self)


class Core(Subject):
	def __init__(self, name=""):
		Subject.__init__(self)
		self._name, self._temp = name, 0

	@property
	def temp(self):
		return self._temp

	@temp.setter
	def temp(self, temp):
		self._temp = temp


class TempViewer:
	def update(self, subject):
		print(f'Temperature Viewer: {subject._name} has temperature: {subject._temp}')


c1, c2 = Core('Core1'), Core('Core2')
v1, v2 = TempViewer(), TempViewer()

c1.attach(v1)
c2.attach(v2)

c1.temp, c2.temp = 80, 90 