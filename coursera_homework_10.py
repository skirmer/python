
name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
    
fh = open(name)
hours = dict()

for line in fh:
	line=line.rstrip()
	if not line.startswith('From '):
		continue
	k=line.split(":")
	time=k[0]
	mailtime=time[-2:]
	if mailtime not in hours:
		hours[mailtime]=1
	else:
		hours[mailtime]=hours.get(mailtime,0)+1
        
timelist=list()
for key, val in hours.items():
    timelist.append((key, val))
timelist.sort()
for val,key in timelist:
	print val,key
