import sys, getopt
argv = sys.argv[1:]
inputfile = ''
outputfile = ''
try:
	opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
except getopt.GetoptError:
	print 'stl2pcl.py -i <inputfile> -o <outputfile>'
	sys.exit(2)
for opt, arg in opts:
	if opt == '-h':
		print 'stl2pcl.py -i <inputfile> -o <outputfile>'
		sys.exit()
	elif opt in ("-i", "--ifile"):
		inputfile = arg
	elif opt in ("-o", "--ofile"):
		outputfile = arg
out = open(outputfile,'w')

j = 0
with open(inputfile) as file:
	lines = file.readline()
	while lines:
		lines = file.readline()
		line = lines.split(' ')
		if len(line) > 6 and line[4] == 'vertex':
			for i in range(3):
				vertex = float(line[5+i].split('\n')[0])/1000
				#print 'writing to file'
				out.write(str(vertex))
				out.write(' ')
			out.write('\n')

out.close()