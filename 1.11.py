
line = '2017-12-22 22:10:28 INFO  : Request Id is - ITSUSRALSP01260_rp'


import re

print(re.split(r'[" "\s]\s*', line))
