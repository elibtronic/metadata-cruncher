
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
		else:
			mlist[issn] = row
		
for k in mlist.keys():
	year = ""
	ei = mlist[k]
	#Standard one line entitlement statement
	if len(ei) == 7:

		#Displayed as a 4 digit number
		if len(ei[3]) == 4:
			year = ei[3]

		#Displayed as 
		year_parts = str.rsplit(ei[3],"-")
		if len(year_parts) == 2:
			if year_parts[1] > 0 and year_parts[1] <= 14:
				year = "20"+year_parts[1]
			else:
				year = "19"+year_parts[1]
			
		
	final_ent = ei[0] + ",$obj->parsedDate(\">=\","+year+","+ei[1]+","+ei[2]+")"
	#print final_ent
