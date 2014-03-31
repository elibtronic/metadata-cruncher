#
# Feed in a CSV or OpenURLs will spit out a CSV file of all the 
#   url parameters alphabetically listed
#
# 2 Caveats 
#   If a data element had a , it was changed to \,
#   If a data element had a " it was changed to qqq
#
import urllib
import urlparse
infile = open("data_in.csv","r")
outfile = open("data_out.csv","w")
masterDict = {}
runningList = []


#Build Dictionary of available categories
for line in infile:
    line = line.rstrip('\n')
    qsp1 = urlparse.parse_qs(line)
    oneLine = {}
    for q in qsp1.keys():
        masterDict[q] = q


infile.close()
mListSorted = sorted(masterDict,key=masterDict.get)


outString = "line"
for m in mListSorted:
    outString += "," + m

print outString
outfile.write(outString+"\n")

infile = open("data_in.csv","r")
for line in infile:
    line = line.rstrip('\n')
    fline = line
    qsp2 = urlparse.parse_qs(line)
    for m in mListSorted:
        if m in qsp2:
            fline += ',"' + "".join(qsp2[m]).replace(",","\\,").replace('"','qqqq')+'"'
        else:
            fline += ',"NA"'
    #print fline + "\n"
    outfile.write(fline + "\n")
    outfile.flush()




print "fin"
