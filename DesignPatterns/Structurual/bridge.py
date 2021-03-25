class DrawingAPIOne(object):
	def drawCircle(self, x, y, radius):
		print('API 1 drawing a circle at ({}, {} with radius {}!)'.format(x, y, radius))


class DrawingAPITwo(object):
	def drawCircle(self, x, y, radius):
		print('API 2 drawing a circle at ({}, {} with radius {}!)'.format(x, y, radius))


class Circle(object):
	def __init__(self, x, y, radius, drawingAPI):
		self._x, self._y = x, y
		self._radius, self._drawingAPI = radius, drawingAPI

	def draw(self):
		self._drawingAPI.drawCircle(self._x, self._y, self._radius)

	def scale(self, percent):
		self._radius *= percent


	circle1 = Circle(1, 2, 3, DrawingAPIOne())
	circle1.draw()

	circle2 = Circle(2, 3, 4, DrawingAPITwo())
	circle2.draw()