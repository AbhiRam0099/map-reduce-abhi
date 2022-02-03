f = open("trends.txt","r")  # open file, read-only
o = open("terndsmapperout.txt", "w") # open file, write
for line in f:  
    rowList = line.strip().split(",") 
    print (rowList )
    print (len(rowList ))
    if len(rowList) == 5:
        location,year,category,rank,query = rowList  #assign names
        print ("{0}\t{1}".format(location, query))
        o.write("{0}\t{1}\n".format(location, query))
f.close()
o.close()