import csv
import argparse

corpus_headers = ['term', ' frequency', ' tfidf', ' ratio of texts occuring in', ' part of speech']
entity_headers = ['Term', ' Entity', ' Frequnecy', ' POS', ' ']

data = {}
finalData = []
def readAllData(filelist,index): # index = 3 for entity and 2 for corpus
    global data
    category = "subject"
    for filename in filelist:
        with open(filename) as fp:
            reader = csv.reader(fp)
            reader.next()
            for row in reader:
                row = row[:index]
                newrow = []
                newrow.append(row[0])
                newrow.append(row[0].replace(" ","_"))
                newrow[1] = newrow[1].replace(".","")
                newrow.extend(row[1:])
                if index == 3:
                    category = row[1]
                if newrow[0] not in data:
                    data[newrow[0]] = {"identi": newrow[1],"cat": category, "freq": int(row[-1])}
                else:
                    data[newrow[0]]["freq"] += int(row[-1])

def prepareData(threshhold):
    global finalData
    for k,v in data.iteritems():
        if v["freq"] > threshhold:
            print v["freq"]
            finalData.append([k,v["identi"],v["cat"]])

def writeCodebook(filename):
    global finalData
    with open(filename, "wb+") as fp:
        writer = csv.writer(fp)
        writer.writerows(finalData)

def makeCorpusCodebook(filelist,threshhold):
    readAllData(filelist,2)
    prepareData(threshhold)
    writeCodebook("CorpusCodebook.csv")
    print "Corpus Codebook Generated."

def makeEntityCodebook(filelist,threshhold):
    readAllData(filelist,3)
    prepareData(threshhold)
    writeCodebook("EntityCodebook.csv")
    print "Entity Codebook Generated."
       
        

def main(args):
    headers = []
    threshhold = 100
    if args.c != "e" and args.c != "c":
        print "No data type mentioned c or e"
        exit(-1)
    if args.t == None:
        args.t = 100
        print "no threshhold. Continuing with 100"
    if args.f == None:
        print "No Files"
        exit(-1)
    threshhold = int(args.t)
    print threshhold
    filelist = args.f.split(",")
    if args.c == "e":
        headers = entity_headers
        makeEntityCodebook(filelist, threshhold)
    elif args.c == "c":
        headers = corpus_headers
        makeCorpusCodebook(filelist, threshhold)
    print "Done" 


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c") #type Entity,Corpus
    parser.add_argument("-t") #threshhold
    parser.add_argument("-f") #files
    args = parser.parse_args()
    main(args)
    
    
