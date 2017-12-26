from hashlib import sha256
from datetime import datetime
import json

class Block:
	def __init__(this, index, prevHash, timestamp, level, nonce, data, Ahash):
		this.index = index
		this.prevHash = prevHash
		this.timestamp = timestamp
		this.level = level
		this.nonce = nonce
		this.data = data #Добавить вознаграждение
		this.hash = Ahash
	def parse(self):
		return [self.index, self.prevHash, self.timestamp, self.level, self.nonce, self.data, self.hash]

genesisBlock = Block(0,'0',1513693852,1,0,'This is the Genesis Block!', 
	'9529788d61b65be3d1796a04a348a46f5b30e6bc28fc293b29f7277ab48a7be0')
blockchain = [genesisBlock]
def getLastBlock(): return blockchain[len(blockchain) - 1]

def calcHash(index, prevHash, timestamp, level, nonce, data): return sha256(str(index).encode() + prevHash.encode() + str(timestamp).encode() + str(level).encode() + str(nonce).encode() + data.encode()).hexdigest()
def calcHashBlock(block):
	return calcHash(block.index, block.prevHash, block.timestamp, block.level, block.nonce, block.data)

def genNextBlock(blockData): 
	prevBlock = getLastBlock()
	nextIndex = prevBlock.index + 1
	nextTimestamp = int(datetime.today().timestamp())
	nextLevel = 3
	nextNonce = 0
	nextHash = calcHash(nextIndex, prevBlock.hash, nextTimestamp, nextLevel, nextNonce, blockData)
	return Block(nextIndex, prevBlock.hash, nextTimestamp, nextLevel, nextNonce, blockData, nextHash)

def findNonce(newBlock):
	while True:
		if newBlock.hash[:newBlock.level] != newBlock.level * '0':
			newBlock.nonce += 1
			newBlock.hash = calcHashBlock(newBlock)
		else: 
			print('Времени потрачено: %i секунд' % (int(datetime.today().timestamp()) - newBlock.timestamp))
			return newBlock

def checkValidBlock(prevBlock, newBlock):
	if prevBlock.index + 1 != newBlock.index:
		print('Неверный индекс')
		return False
	elif prevBlock.hash != newBlock.prevHash:
		print('Неверный хеш предыдущего блока')
		return False
	elif calcHashBlock(newBlock) != newBlock.hash:
		print('Неверный хеш: ' + calcHashBlock(newBlock) +' (актуальный) != (номинальный) '+ newBlock.hash)
		return False
	elif newBlock.hash[:newBlock.level] != newBlock.level * '0':
		print('Неверный Nonce %s' % newBlock.hash)
		return False
	return True

def addBlock(newBlock):
	if checkValidBlock(getLastBlock(), newBlock):
		blockchain.append(newBlock)

#Сделать проверку цепочки (длинная в приоритете, дубликаты отбрасываются)
def checkValidChain(newBlockchain):
	goodPart = []
	for block in newBlockchain[::-1]:
		if block.index > getLastBlock().index or block.prevHash != blockchain[block.index-1].hash and block.index != 0:
			if checkValidBlock(newBlockchain[(newBlockchain.index(block))-1], block):
				goodPart.append(block)
				continue
			return False
		elif goodPart: return list(reversed(goodPart))
		else: return False

def replaceChain(newBlockchain):
	if len(newBlockchain)-1 > getLastBlock().index:
		goodPart = checkValidChain(newBlockchain)
		if goodPart:		
			for index in range(getLastBlock().index - goodPart[0].index):
				del blockchain[-1]
			blockchain.extend(goodPart)
			print('Цепочка успешно импортирована')
		else: print('Цепочка не валидна')
		#Рассказать всем	
	else: print("Цепочка коротче, либо равна актуальной на %s блоков" % (getLastBlock().index - (len(newBlockchain)-1)))

def chainExport(saved_chain='saved_chain.json'):
	with open(saved_chain, 'w') as fd:
		parsedBlockchain = []
		for block in blockchain:
			parsedBlockchain.append(block.parse())
		fd.write(json.dumps(parsedBlockchain))

def chainImport(saved_chain='saved_chain.json'):
	with open(saved_chain, 'r') as fd:
		parsedBlockchain = json.loads(fd.read())
	newBlockchain = []
	for block in parsedBlockchain:
		newBlockchain.append(Block(*block))
	return newBlockchain
