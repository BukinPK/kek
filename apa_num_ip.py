#!/bin/python
import re
import sys
import gzip
logFile = sys.argv[1]
try: level = int(sys.argv[2])
except IndexError: level = 1

def logMaker(logFile, level=1):
    if re.match(r'.+.gz$', logFile):
        openFile = gzip.open(logFile, 'rt')
    else: openFile = open(logFile, 'r')
    with openFile as f:
        log={}
        for line in f:
            try:
                ip = re.split(' ',line)[0]
                timeUnit=':'.join(re.split(r':', str(re.split(' ', line)[3]))[0:level])[1:]
                bandwidth=int(re.split(' ', re.split(r'(?<![\\])"', line)[2])[2])
            except IndexError as ie:
                print(ie, ': ', line, sep='')
            if timeUnit in log: 
                if ip in log[timeUnit]:
                    log[timeUnit][ip][0] += 1
                    log[timeUnit][ip][1] += bandwidth
                else:
                    log[timeUnit][ip] = [1, bandwidth]
            else:
                log[timeUnit] = {}.fromkeys([ip], [1, bandwidth])
        return log

log = logMaker(logFile, level)
timeUnits = list(log.keys())
timeUnits.sort()
for timeUnit in timeUnits:
    requests=0
    bandwidth=0
    for ip in log[timeUnit]:
        requests += log[timeUnit][ip][0]
        bandwidth += log[timeUnit][ip][1]
    print('{0} IP: {1:<6.3f} requests: {2:<7.3f} bandwidth: {3} MiB'.format(timeUnit, len(log[timeUnit])/1000, requests/1000, int(bandwidth/1024/1024)))
