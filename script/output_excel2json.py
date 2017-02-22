'''
This is to read from output Excel to JSON
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
fname = "./../data/cases/" + casename + "/excel/" + networktype + "/output/" + feedername + "_output.xlsx"


try:
    xl = pd.ExcelFile(fname)
except:
    print "No excel file"
    quit()

# Get power exchange
try:
    df = xl.parse("Power Exchange",header=None)
except:
    print "No price info"
    quit()
nperiods = int(df.iat[0,1])
PowerExchange = []
for i in range(nperiods):
    val = float(df.iat[4+i,1])
    PowerExchange.append(val)

# Get generator info
try:
    df = xl.parse("generators",header=None)
except:
    print "No generator info"
    quit()
ngens = int(df.iat[0,1])
genname = []
genPG = []
j = 2 
for i in range(ngens):
    val = str(df.iat[j,1])
    genname.append(val)
    j = j+2
    val1 = []
    for t in range(nperiods):
        val = float(df.iat[j,1])
        val1.append(val)
        j = j+1
    genPG.append(val1)

# Get loads  info
try:
    df = xl.parse("loads",header=None)
except:
    print "No loads info"
    quit()
nloads = int(df.iat[0,1])
loadname = []
loadPD = []
j = 2
for i in range(nloads):
        val = str(df.iat[j,1])
        loadname.append(val)
        j = j+2
        val1 = []
        for t in range(nperiods):
                val = float(df.iat[j,1])
                val1.append(val)
                j = j+1
        loadPD.append(val1)

# Get renewables  info
try:
    df = xl.parse("renewables",header=None)
except:
    print "No renewables info"
    quit()
nrens = int(df.iat[0,1])
renname = []
renPW = []
j = 2
for i in range(nrens):
        val = str(df.iat[j,1])
        renname.append(val)
        j = j+2
        val1 = []
        for t in range(nperiods):
                val = float(df.iat[j,1])
                val1.append(val)
                j = j+1
        renPW.append(val1)

# Get storages  info
try:
    df = xl.parse("storages",header=None)
except:
    print "No storages info"
    quit()
nstrgs = int(df.iat[0,1])
strgname = []
strgE = []
strgPSplus = []
strgPSminus = []
j = 2
for i in range(nstrgs):
        val = str(df.iat[j,1])
        strgname.append(val)
        j = j+2
        val1 = []
        val2 = []
        val3 = []
        for t in range(nperiods):
                val = float(df.iat[j,1])
                val1.append(val)
                val = float(df.iat[j,2])
                val2.append(val)
                val = float(df.iat[j,3])
                val3.append(val)
                j = j+1
        strgE.append(val1)
        strgPSplus.append(val2)
        strgPSminus.append(val3)

'''
convert them into json
'''
outputjson = {}
outputjson['PowerExchange'] = PowerExchange

# key by name
outputjson['generator'] = {}
for i in range(ngens):
    outputjson['generator'][genname[i]] = {
       'PG': genPG[i] 
    }

outputjson['load'] = {}
for i in range(nloads):
    outputjson['load'][loadname[i]] = {
       'PD': loadPD[i] 
    }

outputjson['solar'] = {}
for i in range(nrens):
    outputjson['solar'][renname[i]] = {
       'PW': renPW[i] 
    }

outputjson['storage'] = {}
for i in range(nstrgs):
    outputjson['storage'][strgname[i]] = {
       'E': strgE[i], 
       'PS+': strgPSplus[i], 
       'PS-': strgPSminus[i], 
    }


outfname = "./../data/cases/" + casename + "/jsondata/" + networktype + "/output/" + feedername + "_output.json"

with open(outfname, 'w') as outfile:
    json.dump(outputjson, outfile, indent=4)
# '''
# end of vis_data
# '''
