'''
This is to read from Excel to JSON which can be used for frontend vis
'''
import pandas as pd
import sys
import json

# N = len(sys.argv)

# if N < 2:
#     print "Need a file name"
#     quit()

# fname = str(sys.argv[1])
casename = "newyork"
networktype = "distribution"
feedername = "ders_IEEE123"
fname = "./../data/cases/" + casename + "/excel/" + networktype + "/input/" + feedername + "_data.xlsx"


try:
    xl = pd.ExcelFile(fname)
except:
    print "No excel file"
    quit()

# Get bus info
try:
    df = xl.parse("buses",header=None)
except:
    print "No bus info"
    quit()

nbuses = int(df.iat[0,1])
busname = []
for i in range(nbuses):
    val = str(df.iat[3+i,0])
    busname.append(val)


# Get lines info
try:
    df = xl.parse("lines",header=None)
except:
    print "No lines info"
    quit()
nlines = int(df.iat[0,1])
linename = []
linefrom = []
lineto = []
linecap = []
linebmat = []
for i in range(nlines):
    val = str(df.iat[3+i,0])
    linename.append(val)
    val = str(df.iat[3+i,1])
    linefrom.append(val)
    val = str(df.iat[3+i,2])
    lineto.append(val)
    val = float(df.iat[3+i,3])
    linecap.append(val)
    val = float(df.iat[3+i,4])
    linebmat.append(val)

# Get price info
try:
    df = xl.parse("price",header=None)
except:
    print "No price info"
    quit()
nperiods = int(df.iat[0,1])
price = []
for i in range(nperiods):
    val = float(df.iat[3+i,1])
    price.append(val)

# Get generator info
try:
    df = xl.parse("generators",header=None)
except:
    print "No generator info"
    quit()
ngens = int(df.iat[0,1])
genname = []
gencost = []
gencap = []
genloc = []
for i in range(ngens):
    val = str(df.iat[3+i,0])
    genname.append(val)
    val = float(df.iat[3+i,1])
    gencost.append(val)
    val = float(df.iat[3+i,2])
    gencap.append(val)
    val = str(df.iat[3+i,3])
    genloc.append(val)


# Get storage info
try:
    df = xl.parse("storages",header=None)
except:
    print "No storage info"
    quit()
nstrgs = int(df.iat[0,1])
strgname = []
strgminchrg = []
strgmaxchrg = []
strgintchrg = []
strgchrgrt = []
strgdischrgrt = []
strgchrgeff = []
strgdischrgeff = []
strgloc = []
for i in range(nstrgs):
    val = str(df.iat[3+i,0])
    strgname.append(val)
    val = float(df.iat[3+i,1])
    strgminchrg.append(val)
    val = float(df.iat[3+i,2])
    strgmaxchrg.append(val)
    val = float(df.iat[3+i,3])
    strgintchrg.append(val)
    val = float(df.iat[3+i,4])
    strgchrgrt.append(val)
    val = float(df.iat[3+i,5])
    strgdischrgrt.append(val)
    val = float(df.iat[3+i,6])
    strgchrgeff.append(val)
    val = float(df.iat[3+i,7])
    strgdischrgeff.append(val)
    val = str(df.iat[3+i,8])
    strgloc.append(val)


# Get renewables info
try:
    df = xl.parse("renewables",header=None)
except:
    print "No renewables info"
    quit()
nrens = int(df.iat[0,1])
renname = []
renloc = []
renavlbl = []
renspcost = []
j = 2 
for i in range(nrens):
    val = str(df.iat[j,1])
    renname.append(val)
    j = j+1
    val = str(df.iat[j,1])
    renloc.append(val)
    j = j+2
    val1 = []
    val2 = []
    for t in range(nperiods):
        val = float(df.iat[j,1])
        val1.append(val)
        val = float(df.iat[j,2])
        val2.append(val)
        j = j+1
    renavlbl.append(val1)
    renspcost.append(val2)
    j = j+1

# Get loads  info
try:
    df = xl.parse("loads",header=None)
except:
    print "No loads info"
    quit()
nloads = int(df.iat[0,1])
loadname = []
loadloc = []
loadval = []
loaddrlb = []
loaddrub = []
loadshrtcost = []
loadsurpcost = []
j = 2
for i in range(nloads):
        val = str(df.iat[j,1])
        loadname.append(val)
        j = j+1
        val = str(df.iat[j,1])
        loadloc.append(val)
        j = j+2
        val1 = []
        val2 = []
        val3 = []
        val4 = []
        val5 = []
        for t in range(nperiods):
                val = float(df.iat[j,1])
                val1.append(val)
                val = float(df.iat[j,2])
                val2.append(val)
                val = float(df.iat[j,3])
                val3.append(val)
                val = float(df.iat[j,4])
                val4.append(val)
                val = float(df.iat[j,5])
                val5.append(val)
                j = j+1
        loadval.append(val1)
        loaddrlb.append(val2)
        loaddrub.append(val3)
        loadshrtcost.append(val4)
        loadsurpcost.append(val5)
        j = j+1

'''
making vis_usage data
'''
vis_data = {}
vis_data['nodes'] = []
vis_data['links'] = []
vis_data['price'] = price
name2nodeMap = {}

# make bus
for i in range(nbuses):
    newNode = {
        'name': busname[i],
        'object': 'node',
        'lat': None,
        'lng': None,
        'elements': []
    }
    vis_data['nodes'].append(newNode)
    name2nodeMap[busname[i]] = newNode

#make lines
for i in range(nlines):
    newLine = {
        'name': linename[i],
        'object': 'line',
        'from': linefrom[i],
        'to': lineto[i],
        'cap': linecap[i],
        'bmat': linecap[i]
    }
    vis_data['links'].append(newLine)

#make generators
for i in range(ngens):
    newGenerator = {
        'name': genname[i],
        'object': 'generator',
        'cost': gencost[i],
        'capacity': gencap[i],
        'parent': genloc[i],
    }
    name2nodeMap[genloc[i]]['elements'].append(newGenerator)

#make storages
for i in range(nstrgs):
    newStorage = {
        'name': strgname[i],
        'object': 'storage',
        'min charge': strgminchrg[i],
        'max charge': strgmaxchrg[i],
        'initial charge': strgintchrg[i],
        'charge rate': strgchrgrt[i],
        'discharge rate': strgdischrgrt[i],
        'charge eff': strgchrgeff[i],
        'discharge eff': strgdischrgeff[i],
        'parent': strgloc[i],
    }
    name2nodeMap[strgloc[i]]['elements'].append(newStorage)


#make renewables
for i in range(nrens):
    newSolar = {
        'name': renname[i],
        'object': 'solar',
        'parent': renloc[i],
        'available': renavlbl[i],
        'spillage cost': renspcost[i]
    }
    name2nodeMap[renloc[i]]['elements'].append(newSolar)

#make loads
for i in range(nloads):
    newLoad = {
        'name': loadname[i],
        'object': 'load',
        'parent': loadloc[i],
        'load value': loadval[i],
        'dem Resp LB': loaddrlb[i],
        'dem Resp UB': loaddrub[i],
        'shortage cost': loadshrtcost[i],
        'surplus cost': loadsurpcost[i],
    }
    name2nodeMap[loadloc[i]]['elements'].append(newLoad)

'''
try to attach the location data
'''
try:
    loc_fname = "./../data/cases/" + casename + "/jsondata/" + networktype + "/input/" + feedername + "_loc.json"
    with open(loc_fname, 'r') as infile:
        location_data = json.load(infile)

    node_locations = location_data['nodes']
    for node in node_locations:
        currNode = name2nodeMap[node['name']]
        currNode['lat'] = node['lat']
        currNode['lng'] = node['lng']
except IOError:
    print "Error: Cannot find location data"

'''
end of try
'''

with open('./../data/cases/cleandata2.json', 'w') as outfile:
    json.dump(vis_data, outfile, indent=4)
'''
end of vis_data
'''
