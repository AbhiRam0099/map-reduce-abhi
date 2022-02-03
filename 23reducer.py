s = open(r"C:\Users\S541999\Documents\44517\map-reduce-abhi\trendsort.txt","r")
out = r"C:\Users\S541999\Documents\44517\map-reduce-abhi\trendreducer.txt"



thisKey = ""
thisValue = 0
data_dict = {}

for line in s:
    line_data = line.split('\t')
    location,query = line_data[0], line_data[1].rstrip()
    if query in data_dict.keys():
        data_dict[query] +=1
    else:
        data_dict[query] = 1

with open(out, 'w') as f: 
    for key, value in data_dict.items():
        f.write('%s:%s\n' % (key, value))

s.close()
