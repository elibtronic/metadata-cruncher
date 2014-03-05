
#
# Creates parsedate stuff from Else supplied data
#
#
from sys import argv
import csv

infile_name = "in.csv"
outfile_name = "out.csv"
mlist = dict()

if __name__ == '__main__' and len(argv) == 3:
		infile_name = argv[1]
		outfile_name = argv[2]

with open(infile_name,'r') as csvfile:
	mdr = csv.reader(csvfile)
	mdr.next()
	for row in mdr:
		issn = row[0]
		if mlist.has_key(issn):
			mlist[issn].append(row)
			print "old"
		else:
			mlist[issn] = row
			print "new"
		
for k in mlist.keys():
	ei = mlist[k]
	if len(ei) == 7:
		final_ent = ei[0] + ",$obj->parsedDate(\">=\","+"YEAR"+","+ei[1]+","+ei[2]+")"

	print final_ent
