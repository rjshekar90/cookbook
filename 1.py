

line = '2017-12-22 22:10:28 INFO  : Request Id is - ITSUSRALSP01260_rp'

timestamp, timestamp1, loglevel,_, _,*log = line.split(" ", 5)

print(timestamp+" "+timestamp1)
print(loglevel)
print(log)