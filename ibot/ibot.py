#!/usr/bin/python3
import os
basedir = os.path.abspath(os.path.dirname(__file__))+'/'
from InstagramAPI import InstagramAPI
from target import Target
from random import randrange
from time import sleep
from getpass import getpass


class Bot:
	
	my_name = ''
	passwd = ''

	def __init__(self):
		try: os.mkdir(basedir+'bot_data')
		except FileExistsError: pass

	def login(self):
		if not self.my_name: self.my_name = input('Введите логин: ')
		if not self.passwd: self.passwd = getpass('Введите пароль: ')
		self.api = InstagramAPI(self.my_name, self.passwd)
		if self.api.login() is True:
			self.getUserId = self.__getUserId
			self.makeTarget = self.__makeTarget
			return True
		else:
			self.my_name = ''
			self.passwd = ''
			del self.api
			return False

	def __getUserId(self, username):
		self.api.searchUsername(username)
		return self.api.LastJson['user']['pk']
	
	def __makeTarget(self, target_id=None):
		if not target_id: target_id = getUserId(input('Введите название группы: '))
		self.target = Target(target_id, self.api)
	
if __name__ == '__main__':
	b = Bot()
	b.login()
	b.makeTarget()
	b.target.followingProtocol()
