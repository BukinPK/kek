#!/usr/bin/python3

import curses, signal, sys, re, time
import vk_api
from datetime import timedelta
from random import randint
from getpass import getpass
login = input('Введите ваш логин: ')
password = getpass('Введите ваш пароль: ')
groupId = input('Введите идентификатор группы: ')
vk = vk_api.VkApi(login = login, password = password)
vk.auth()

stdscr = curses.initscr()
curses.noecho()
stdscr.refresh()

myCountry = vk.method('database.getCountries', {'code':'MD'})['items'][0]['id']
myCity = vk.method('database.getCities', {'country_id':myCountry})['items'][0]['id']

count = 1000
offset = 0
gsParams = {'group_id':groupId,
        'count':count,
        'offset':offset,
        'fields':'sex, country, city, bdate'
        }

def sign(signum, frame):
    curses.endwin()
    print('Bay')
    sys.exit(0)
signal.signal(signal.SIGINT, sign)

try:
    with open('likedIds', 'r') as f:
        likedIds = f.read().splitlines()
except: likedIds = []
while True:
    gsParams['offset'] = offset
    gSearch = vk.method('groups.getMembers', gsParams)
    if  gSearch['items'] == []: break
    for user in gSearch['items']:
        try: 
            age = int(user.get('bdate', 0).split('.')[2])
        except (AttributeError, IndexError): 
            f_noAge = 1 if 'f_noAge' not in locals() else f_noAge + 1
            continue
        if user['sex'] != 1: 
            f_sex = 1 if 'f_sex' not in locals() else f_sex + 1
            continue
        elif user.get('city',{}).get('id', 0) != myCity: 
            f_city = 1 if 'f_city' not in locals() else f_city + 1
            continue
        elif not 1999 > age > 1989: 
            f_age = 1 if 'f_age' not in locals() else f_age + 1
            continue
        elif likedIds.count(str(user['id'])) != 0: 
            f_listed = 1 if 'f_listed' not in locals() else f_listed + 1
            continue

        photo = vk.method('photos.get', 
                {'owner_id':user['id'], 
                    'album_id':'profile', 
                    'rev':1, 
                    'extended':1, 
                    'count':1})
        try:
            if photo['items'][0]['likes']['user_likes'] == 0:
                delay = randint(1,5)
                for de in range(delay, -1, -1):
                    stdscr.addstr(1, 20, 'watch photo delay: %s/%s  ' % (de, delay))
                    stdscr.refresh()
                    time.sleep(1)
                vk.method('likes.add', 
                        {'type':'photo', 
                            'item_id':photo['items'][0]['id'], 
                            'owner_id':user['id']})
                likes = 1 if 'likes' not in locals() else likes + 1
                with open('likedIds', 'a') as f:
                    f.write(str(user['id'])+'\n')
                stdscr.addstr(0, 0, 'no age: %d'    % f_noAge)
                stdscr.addstr(1, 0, 'man: %d'       % f_sex)
                stdscr.addstr(2, 0, 'city: %d'      % f_city)
                stdscr.addstr(3, 0, 'age: %d'       % f_age)
                stdscr.addstr(4, 0, 'listed: %d'    % f_listed)
                stdscr.addstr(5, 0, 'likes: %d'     % likes)
                stdscr.addstr(6, 0, 'last: https://vk.com/id%s  ' % user['id'])
                stdscr.refresh()
                delay = randint(60,180)
                for de in range(delay, -1, -1):
                    stdscr.addstr(0, 20, 'after like delay: %d/%d  ' % (de, delay))
                    stdscr.refresh()
                    time.sleep(1)
                if 'pause' not in locals():
                    pause = 1 
                    pauseTime = randint(8, 15)
                else:
                    pause += 1
                    if pause > pauseTime:
                        delay = randint(20*60, 40*60)
                        for de in range(delay, -1, -1):
                            stdscr.addstr(2, 20, 'pause after %d likes: %s / %s  ' % (pause, ':'.join(re.split(':', str(timedelta(0, de)))[1:]), ':'.join(re.split(':', str(timedelta(0, delay)))[1:])))
                            stdscr.refresh()
                            time.sleep(1)
                        del(pause)
        except IndexError:
            stdscr.addstr(10, 2, 'index error on https://vk.com/id%s' % user['id'])
            with open('likedIds', 'a') as f:
                f.write(str(user['id'])+'\n')
        except:
            curses.endwin()
            raise
    offset += count
