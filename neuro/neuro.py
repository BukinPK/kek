import string, os
from img import load_image, save_image

class Neuron:
	weight = 0
	def __init__(self, name, model=[255 for x in range(30*30)], count=0):
		self.name = name
		self.model = model
		self.count = count
	def __repr__(self):
		return 'Нейрон:%s Уверенность:%i Модель:%i' % (self.name, self.weight, self.count)
	def add(self, input):
		temp = []
		for num, pixel in enumerate(self.model):
			temp.append(int((pixel * self.count + input[num]) / (self.count + 1)))
		self.model = temp
		self.count += 1
	def save(self, path='pic/model/'):
		for model in os.listdir(path):
			if self.name.lower() == model[0]: os.remove(path+model)
		save_image(self.model, path+self.name.lower()+str(self.count)+'.png')
	def load(self, path='pic/model/'):
		for pic in os.listdir(path):
			if pic[0] == self.name.lower():
				self.model = load_image(path+pic)
				self.count = int(pic[1:].split('.png')[0])
				break
			

class Web:
	__view = []
	match = None
	_input = [0 for x in range(30*30)]
	def __init__(self, elements=string.ascii_uppercase):
		for item in elements:
			self.__view.append(Neuron(item))
	def __repr__(self):
		return repr(self.__view)
	def __getitem__(self, key):
		return self.__view[key]
	def insert(self, pic):
		self._input = load_image(pic)
	def check(self):
		for neuron in self:
			neuron.weight = 0
			for pixel in range(900):
				if self._input[pixel] < 250 and abs(neuron.model[pixel] - self._input[pixel]) < 100:
					neuron.weight += 1	
		max = self[0]
		for neuron in self:
			if neuron.weight > max.weight: max = neuron
		self.match = max
		return max
	def result(self):
		for neuron in self: print(neuron)
	def learn(self, path='pic/input/'):
		for pic in os.listdir(path):
			for neuron in self:
				if neuron.name == pic[0].upper():
					neuron.add(load_image(path+pic))
	def save(self, path='pic/model/'):
		for neuron in self:
			if neuron.count > 0:
				neuron.save(path)
	def load(self, path='pic/model/'):
		for neuron in self:
			neuron.load(path)

if __name__ == '__main__':
	from sys import argv
	w = Web()
	w.learn()
	w.insert(argv[1])
	w.check()
	w.save()
	w.result()
