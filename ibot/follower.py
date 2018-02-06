from random import randrange
from time import sleep
import json

class Follower:
	
	like_wait = 5

	def __init__(self, follower_id, api):
		self.id = follower_id
		self.api = api

	def getInfo(self):
		self.api.getUsernameInfo(self.id)
		self.info = self.api.LastJson['user']
		self.username = self.info['username']
	def getFeed(self):
		self.api.getUserFeed(self.id)
		self.feed = self.api.LastJson
		
	
	def print_info(self):
		if 'info' not in dir(self):
			self.getInfo()
		print(json.dumps(self.info, indent=2))
	def print_feed(self):
		if 'feed' not in dir(self):
			self.getFeed()
		print(json.dumps(self.feed, indent=2))
		

	def checkInfo(self):
		if 'info' not in dir(self):
			self.getInfo()
		if self.info['media_count'] <= 1:
			self.is_media_homeless = True
		else: self.is_media_homeless = False
		if self.info['follower_count'] > \
    		self.info['following_count'] * 3:
        		self.is_attention_whore = True
		else: self.is_attention_whore = False
		if self.info['follower_count'] * 3 < \
    		self.info['following_count']:
        		self.is_shit_eater = True
		else: self.is_shit_eater = False
		self.is_business = self.info['is_business']
		self.is_private = self.info['is_private']
		self.media_count = self.info['media_count']
		self.follower_count = self.info['follower_count']
		self.following_count = self.info['following_count']
		if self.follower_count > 5000 \
			or self.following_count > 5000:
				self.activity_overload = True
		else: self.activity_overload = False

		if self.is_media_homeless is True or \
			self.is_attention_whore is True or \
			self.is_shit_eater is True or \
			self.activity_overload is True or \
			self.is_business is True:
				with open('bot_data/bad_user', 'a') as f:
					f.write(str(self.id)+'\n')
				return False
		else: return True
		

	def checkFriendship(self):
		self.api.userFriendship(self.id)
		user_info = self.api.LastJson
		if user_info['followed_by'] is True or \
    		user_info['following'] is True or \
    		user_info['outgoing_request'] is True:
				self.is_friend = True
				return True
		else: 
			self.is_friend = False
			return False

	def follow(self):
		self.api.follow(self.id)
		with open('bot_data/user_fol', 'a') as f:
			f.write(str(self.id)+'\n')

	def randomPicLike(self):
		if 'feed' not in dir(self):
			self.getFeed()
		while True:
			like_count = randrange(1,4)
			pic_count = self.feed['num_results']
			if like_count <= pic_count:
				self.liked_pics = []
				break
		for like in range(like_count):
			media_number = randrange(0, pic_count)
			media_choice = self.feed['items'][media_number]
			if media_choice['has_liked'] is True:
				continue
			else: 
				picture_id = media_choice['pk']
				self.api.like(picture_id)
				with open('bot_data/pic_like', 'a') as f:
					f.write(str(picture_id)+'\n')
				sleep(randrange(2, self.like_wait))
				self.liked_pics.append(media_number+1)

	def action(self):
		if self.checkFriendship() is True:
			print('is friend [%s]:' % self.username)
			return False
		if self.checkInfo() is False:
			print('bad info [%s]:' % self.username, end=' ')
			if self.is_attention_whore:
				print('whore', end=' ') 
			if self.is_media_homeless:
				print('homless', end=' ') 
			if self.is_business:
				print('business', end=' ') 
			if self.is_shit_eater:
				print('shit_eater', end=' ') 
			if self.activity_overload:
				print('activity_overload', end=' ') 
			print()
			return False
		if self.is_private is False:
			self.randomPicLike()
			print('pic liked:', self.liked_pics, end=' ')
		else:
			print('no pic liked, is private', end=' ')
			sleep(randrange(2, self.like_wait))
		self.follow()
		print('following [%s]' % self.username)
		self.is_friend = True
		return True
