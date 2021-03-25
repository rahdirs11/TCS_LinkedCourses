class Component(object):
	def __init__(self, *args, **kwargs):
		pass

	def componentFunction(self):
		pass


class Child(Component):
	def __init__(self, *args, **kwargs):
		Component.__init__(self, *args, **kwargs)
		self.name = args[0]

	def componentFunction(self):
		print(f'{self.name}')


class Composite():
	def __init__(self, *args, **kwargs):
		Component.__init__(self, *args, **kwargs)
		self.children = list()

	def appendChild(self, child):
		self.children.append(child)

	def removeChild(self, child):
		if child in self.children:
			self.children.remove(child)

	def componentFunction(self):
		for i in self.children:
			i.componentFunction()

sub1 = Composite('submenu1')
sub1 = Child("sub_submenu 11")
sub12 = Child("sub_submenu 12")

sub1.appendChild(sub11)
sub1.appendChild(sub12)

top = Composite("topmenu")
sub2 = Child("submenu2")
top.appendChild(sub1)
top.appendChild(sub2)

top.componentFunction()