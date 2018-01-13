import string, os
from PIL import Image

class Neuron:
	weight = 0
	#ВАЖНО!!! Убрать ссылки с массивов
	def __init__(self, name, input=[0 for x in range(30*30)], model=[255 for x in range(30*30)], count=0):
		self.name = name
		self.input = input
		self.model = model
		self.count = count
	def __repr__(self):
		return 'Нейрон:%s Уверенность:%i Модель:%i' % (self.name, self.weight, self.count)
	@property
	def add(self):
		for num, pixel in enumerate(self.model):
			self.model[num] = int((pixel * self.count + self.input[num]) / (self.count + 1))
		self.count += 1

class Web:
	__view = []
	match = None
	def __init__(self, elements=string.ascii_uppercase):
		for item in elements:
			self.__view.append(Neuron(item))
	def __repr__(self):
		return repr(self.__view)
	def __getitem__(self, key):
		return self.__view[key]

	def insert(self, pic):
		for neuron in self: neuron.input = pic

	def check(self):
		for neuron in self:
			for pixel in range(900):
				if neuron.input[pixel] < 250 and abs(neuron.model[pixel] - neuron.input[pixel]) < 100:
					neuron.weight += 1	
		max = self[0]
		for neuron in self:
			if neuron.weight > max.weight: max = neuron
		self.match = max
		return max

	def result(self):
		for neuron in self:
			print(neuron)

	def learn(self):
		path='pic/input/'
		for pic in os.listdir(path):
			for neuron in self:
				if neuron.name == pic[0].upper():
					neuron.input = load_image(path+pic)
					neuron.add

#def make_web(elements=string.ascii_uppercase):
#	web = []
#	for item in elements:
#		web.append(Neuron(item))
#	return web

def pic_bolder(pic):
	min = pic[0]
	for pixel in pic:
		if pixel < min: min = pixel
	for num,pixel in enumerate(pic):
		if pixel < 255: pic[num] = pic[num]-min
	return pic

#def check(web):
#	for neuron in web:
#		for pixel in range(900):
#			if neuron.input[pixel] < 250 and abs(neuron.model[pixel] - neuron.input[pixel]) < 100:
#				neuron.weight += 1	
#	max = web[0]
#	for neuron in web:
#		if neuron.weight > max.weight: max = neuron
#	return max

#def learn(web):
#	pass
def load_model(path):
	pass

def load_image(path):
	pic = Image.open(path) #Загрузка
	return pic_bolder([int(y) for y in pic.tobytes()]) #Преобразование картинки в массив

def save(pic, path):
	pic = Image.frombytes('L', (30,30),bytes(pic)) #Преобразование массива в картинку
	pic.save(path) #Сохранение

#def test(web):
#        path='pic/input/'
#        for pic in os.listdir(path):
#                for neuron in web:
#                        if neuron.name == pic[0].upper():
#                                neuron.input = load_image(path+pic)
#                                neuron.add
#

#save(pic, 'pic/out.png')

