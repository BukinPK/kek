from hashlib import sha256
from datetime import datetime

class Block:
	def __init__(this, index, prevHash, timestamp, data, Ahash):
		this.index = index
		this.prevHash = prevHash
		this.timestamp = timestamp
		this.data = data
		this.hash = Ahash

genesisBlock = Block(0,'0',1513511456,'This is the Genesis Block!', 
	'f81a91cde7f2c7a08a7ca06c8282612073b837718b578bb2000fd0dd67e6469d')
blockchain = [genesisBlock]
def getPrevBlock(): return blockchain[len(blockchain) - 1]

def calcHash(index, prevHash, timestamp, data): 
	return sha256(str(index).encode() + prevHash.encode() + str(timestamp).encode() + data.encode()).hexdigest()
def calcHashBlock(block):
	return calcHash(block.index, block.prevHash, block.timestamp, block.data)

def genNextBlock(blockData): 
	prevBlock = getPrevBlock()
	nextIndex = prevBlock.index + 1
	nextTimestamp = int(datetime.today().timestamp())
	nextHash = calcHash(nextIndex, prevBlock.hash, nextTimestamp, blockData)
	return Block(nextIndex, prevBlock.hash, nextTimestamp, blockData, nextHash)


def chekVakidBlock(prevBlock, newBlock):
	if prevBlock.index + 1 != newBlock.index:
		print('Неверный индекс')
		return False
	elif prevBlock.hash != newBlock.prevHash:
		print('Неверный хеш предыдущего блока')
		return False
	elif calcHashBlock(newBlock) != newBlock.hash:
		print('Неверный хеш: ' + calcHashBlock(newBlock) +' (актуальный) != (номинальный) '+ newBlock.hash)
		return False
	return True

def addBlock(newBlock):
	if checkVakidBlock(getPrevBlock(), newBlock):
		blockchain.append(newBlock)
