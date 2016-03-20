import os

fd = open("val.txt","w+")

for f in os.listdir('./val'):
	if(f[0:3]=='cat'):
		#write f along with label 0
		s ='/'+f+' 0\n'
		fd.write(s)
	else:
		#write f along with label 1	
		s='/'+f+' 1\n'
		fd.write(s)
