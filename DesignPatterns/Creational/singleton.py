class Borg:
	_shared_state = dict()
	def __init__(self):
		self.__dict__ = self._shared_state
		# make it an attribute dictionary


class Singleton(Borg):
	'''Inherits from Borg class'''
	
	def __init__(self, **kwargs):
		Borg.__init__(self)
		self._shared_state.update(kwargs)

	def __str__(self):
		return str(self._shared_state)


x = Singleton(HTTP="Hyper Text Transfer Protocol")
y = Singleton(SNMP="Simple Network Management Protocol")
print(x)

