from random import randint as rand
from sys import argv

def repeat_count(try_count, maximum=1, debug=False):
	global_storage = {}
	storage = 0
	last_try = None
	while try_count > 0:	
		try_count -= 1
		this_try = rand(0,maximum)

		if this_try is not last_try and last_try is not None or try_count == 0:
			if this_try == last_try:
				storage += 1
			if debug: print(str(last_try)*storage)
			if try_count == 0 and this_try != last_try:
				if debug: print(this_try)
				try: global_storage[1] += 1
				except KeyError: global_storage[1] = 1
			try: global_storage[storage] += 1
			except KeyError: global_storage[storage] = 1
			storage = 1
		else: storage += 1
		last_try = this_try

	return global_storage

storage = repeat_count(*map(int,argv[1:]))
for key in sorted(storage.keys()):
	print('%-3i подряд выпало %i раз' % (key, storage[key]))
